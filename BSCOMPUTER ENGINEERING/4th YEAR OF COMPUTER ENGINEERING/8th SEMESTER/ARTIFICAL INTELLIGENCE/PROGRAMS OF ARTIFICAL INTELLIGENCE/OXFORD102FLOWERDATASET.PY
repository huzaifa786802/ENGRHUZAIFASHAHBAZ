#use transfer learning to classify images of flowers into different categories using a pre-trained model like MobileNetV2 or any other pre-trained model
#(i) Load apre-trained model(excluding top layers)
#(ii)Add your own classification head.
#(iii)Train only the top layers on a small dataset.
#(iv)Show Accuracy and performance
#(v)Oxford 102 FLower Dataset
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
import torchvision
from torchvision import datasets, models, transforms
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, classification_report
import os
import time
from collections import defaultdict
import requests
import tarfile
from PIL import Image
import scipy.io
# Set random seeds for reproducibility
SEED = 123
BATCH_SIZE = 32
IMG_SIZE = 224
NUM_CLASSES = 102
NUM_WORKERS = 4

torch.manual_seed(SEED)
np.random.seed(SEED)
if torch.cuda.is_available():
    torch.cuda.manual_seed(SEED)

# Check for GPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"PyTorch version: {torch.__version__}")
print(f"Device: {device}")
if torch.cuda.is_available():
    print(f"GPU: {torch.cuda.get_device_name(0)}")

# ------------------------------------------------------
# STEP 1: DOWNLOAD AND PREPARE OXFORD 102 FLOWER DATASET
# ------------------------------------------------------
print("\n🌸 Setting up Oxford 102 Flower Dataset...")

def download_oxford_flowers():
    """Download and extract Oxford 102 Flower dataset"""
    os.makedirs('data', exist_ok=True)
    
    # URLs for the dataset
    image_url = "https://www.robots.ox.ac.uk/~vgg/data/flowers/102/102flowers.tgz"
    labels_url = "https://www.robots.ox.ac.uk/~vgg/data/flowers/102/imagelabels.mat"
    splits_url = "https://www.robots.ox.ac.uk/~vgg/data/flowers/102/setid.mat"
    
    # Download files if they don't exist
    files_to_download = [
        (image_url, "data/102flowers.tgz"),
        (labels_url, "data/imagelabels.mat"),
        (splits_url, "data/setid.mat")
    ]
    
    for url, filepath in files_to_download:
        if not os.path.exists(filepath):
            print(f"Downloading {os.path.basename(filepath)}...")
            response = requests.get(url)
            with open(filepath, 'wb') as f:
                f.write(response.content)
    
    # Extract images if not already extracted
    if not os.path.exists("data/jpg"):
        print("Extracting images...")
        with tarfile.open("data/102flowers.tgz", 'r:gz') as tar:
            tar.extractall("data")
    
    print("✅ Dataset ready!")

def prepare_dataset_splits():
    """Organize dataset into train/val/test splits"""
    # Load labels and splits
    labels = scipy.io.loadmat('data/imagelabels.mat')['labels'][0]
    splits = scipy.io.loadmat('data/setid.mat')
    
    train_ids = splits['trnid'][0]
    val_ids = splits['valid'][0]
    test_ids = splits['tstid'][0]
    
    # Create directories
    for split in ['train', 'val', 'test']:
        for class_id in range(1, NUM_CLASSES + 1):
            os.makedirs(f'data/{split}/{class_id:03d}', exist_ok=True)
    
    # Move images to appropriate directories
    def move_images(ids, split_name):
        for img_id in ids:
            src_path = f'data/jpg/image_{img_id:05d}.jpg'
            if os.path.exists(src_path):
                class_id = labels[img_id - 1]  # labels are 1-indexed
                dst_path = f'data/{split_name}/{class_id:03d}/image_{img_id:05d}.jpg'
                if not os.path.exists(dst_path):
                    os.link(src_path, dst_path)  # Create hard link
    
    print("Organizing dataset splits...")
    move_images(train_ids, 'train')
    move_images(val_ids, 'val')
    move_images(test_ids, 'test')
    
    print(f"Train images: {len(train_ids)}")
    print(f"Validation images: {len(val_ids)}")
    print(f"Test images: {len(test_ids)}")

# Download and prepare dataset
try:
    download_oxford_flowers()
    prepare_dataset_splits()
except Exception as e:
    print(f"❌ Error setting up dataset: {e}")
    print("You may need to download the dataset manually or check internet connection")

# ------------------------------------------------------
# STEP 2: DATA TRANSFORMS AND LOADERS
# ------------------------------------------------------
print("\n🔄 Setting up data transforms and loaders...")

# Data transforms
train_transforms = transforms.Compose([
    transforms.Resize((IMG_SIZE, IMG_SIZE)),
    transforms.RandomHorizontalFlip(p=0.5),
    transforms.RandomRotation(degrees=10),
    transforms.ColorJitter(brightness=0.1, contrast=0.1, saturation=0.1, hue=0.1),
    transforms.RandomAffine(degrees=0, translate=(0.1, 0.1), scale=(0.9, 1.1)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

val_test_transforms = transforms.Compose([
    transforms.Resize((IMG_SIZE, IMG_SIZE)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

# Create datasets
train_dataset = datasets.ImageFolder('data/train', transform=train_transforms)
val_dataset = datasets.ImageFolder('data/val', transform=val_test_transforms)
test_dataset = datasets.ImageFolder('data/test', transform=val_test_transforms)

# Create data loaders
train_loader = DataLoader(train_dataset, batch_size=BATCH_SIZE, shuffle=True, 
                         num_workers=NUM_WORKERS, pin_memory=True)
val_loader = DataLoader(val_dataset, batch_size=BATCH_SIZE, shuffle=False, 
                       num_workers=NUM_WORKERS, pin_memory=True)
test_loader = DataLoader(test_dataset, batch_size=BATCH_SIZE, shuffle=False, 
                        num_workers=NUM_WORKERS, pin_memory=True)

print(f"Training samples: {len(train_dataset)}")
print(f"Validation samples: {len(val_dataset)}")
print(f"Test samples: {len(test_dataset)}")

# ------------------------------------------------------
# STEP 3: BUILD MODEL (TRANSFER LEARNING WITH MOBILENETV2)
# ------------------------------------------------------
print("\n🏗️ Building transfer learning model with MobileNetV2...")

class FlowerClassifier(nn.Module):
    def __init__(self, num_classes=NUM_CLASSES, dropout_rate=0.3):
        super(FlowerClassifier, self).__init__()
        
        # Load pre-trained MobileNetV2
        self.backbone = models.mobilenet_v2(pretrained=True)
        
        # Freeze backbone parameters
        for param in self.backbone.parameters():
            param.requires_grad = False
        
        # Replace classifier
        num_features = self.backbone.classifier[1].in_features
        self.backbone.classifier = nn.Sequential(
            nn.Dropout(dropout_rate),
            nn.Linear(num_features, num_classes)
        )
    
    def forward(self, x):
        return self.backbone(x)
    
    def unfreeze_layers(self, num_layers_to_unfreeze=30):
        """Unfreeze the last few layers for fine-tuning"""
        # Get all parameters
        all_params = list(self.backbone.parameters())
        
        # Unfreeze the last num_layers_to_unfreeze parameters
        for param in all_params[-num_layers_to_unfreeze:]:
            param.requires_grad = True
        
        print(f"Unfroze last {num_layers_to_unfreeze} parameters")

# Create model
model = FlowerClassifier(num_classes=NUM_CLASSES)
model = model.to(device)

# Count parameters
total_params = sum(p.numel() for p in model.parameters())
trainable_params = sum(p.numel() for p in model.parameters() if p.requires_grad)

print(f"Total parameters: {total_params:,}")
print(f"Trainable parameters: {trainable_params:,}")
print(f"Frozen parameters: {total_params - trainable_params:,}")

# ------------------------------------------------------
# STEP 4: TRAINING FUNCTIONS
# ------------------------------------------------------

def train_epoch(model, loader, criterion, optimizer, device):
    """Train for one epoch"""
    model.train()
    running_loss = 0.0
    correct = 0
    total = 0
    
    for inputs, labels in loader:
        inputs, labels = inputs.to(device), labels.to(device)
        
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        
        running_loss += loss.item()
        _, predicted = torch.max(outputs.data, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()
    
    epoch_loss = running_loss / len(loader)
    epoch_acc = 100 * correct / total
    return epoch_loss, epoch_acc

def validate(model, loader, criterion, device):
    """Validate the model"""
    model.eval()
    running_loss = 0.0
    correct = 0
    total = 0
    top5_correct = 0
    
    with torch.no_grad():
        for inputs, labels in loader:
            inputs, labels = inputs.to(device), labels.to(device)
            
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            
            running_loss += loss.item()
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
            
            # Top-5 accuracy
            _, top5_pred = torch.topk(outputs, 5, dim=1)
            top5_correct += sum([labels[i] in top5_pred[i] for i in range(labels.size(0))])
    
    epoch_loss = running_loss / len(loader)
    epoch_acc = 100 * correct / total
    top5_acc = 100 * top5_correct / total
    return epoch_loss, epoch_acc, top5_acc

# ------------------------------------------------------
# STEP 5: PHASE 1 - TRAIN CLASSIFICATION HEAD ONLY
# ------------------------------------------------------
print("\n🎯 Phase 1: Training classification head only...")

criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=1e-3, weight_decay=1e-4)
scheduler = optim.lr_scheduler.ReduceLROnPlateau(optimizer, mode='min', factor=0.5, patience=2)

# Training loop
num_epochs_phase1 = 10
train_losses, train_accs = [], []
val_losses, val_accs, val_top5_accs = [], [], []
best_val_acc = 0.0

print("Starting Phase 1 training...")
start_time = time.time()

for epoch in range(num_epochs_phase1):
    # Train
    train_loss, train_acc = train_epoch(model, train_loader, criterion, optimizer, device)
    
    # Validate
    val_loss, val_acc, val_top5_acc = validate(model, val_loader, criterion, device)
    
    # Update scheduler
    scheduler.step(val_loss)
    
    # Save best model
    if val_acc > best_val_acc:
        best_val_acc = val_acc
        torch.save(model.state_dict(), 'best_model_phase1.pth')
    
    # Store metrics
    train_losses.append(train_loss)
    train_accs.append(train_acc)
    val_losses.append(val_loss)
    val_accs.append(val_acc)
    val_top5_accs.append(val_top5_acc)
    
    print(f'Epoch [{epoch+1}/{num_epochs_phase1}] '
          f'Train Loss: {train_loss:.4f}, Train Acc: {train_acc:.2f}% | '
          f'Val Loss: {val_loss:.4f}, Val Acc: {val_acc:.2f}%, Top-5: {val_top5_acc:.2f}%')

phase1_time = time.time() - start_time
print(f"Phase 1 completed in {phase1_time:.2f} seconds")

# ------------------------------------------------------
# STEP 6: PHASE 2 - FINE-TUNING
# ------------------------------------------------------
print("\n🔧 Phase 2: Fine-tuning with unfrozen layers...")

# Load best model from phase 1
model.load_state_dict(torch.load('best_model_phase1.pth'))

# Unfreeze some layers
model.unfreeze_layers(num_layers_to_unfreeze=30)

# New optimizer with lower learning rate
optimizer = optim.Adam(model.parameters(), lr=1e-5, weight_decay=1e-4)
scheduler = optim.lr_scheduler.ReduceLROnPlateau(optimizer, mode='min', factor=0.5, patience=2)

# Fine-tuning loop
num_epochs_phase2 = 5
phase1_epochs = len(train_losses)

print("Starting Phase 2 fine-tuning...")
start_time = time.time()

for epoch in range(num_epochs_phase2):
    # Train
    train_loss, train_acc = train_epoch(model, train_loader, criterion, optimizer, device)
    
    # Validate
    val_loss, val_acc, val_top5_acc = validate(model, val_loader, criterion, device)
    
    # Update scheduler
    scheduler.step(val_loss)
    
    # Save best model
    if val_acc > best_val_acc:
        best_val_acc = val_acc
        torch.save(model.state_dict(), 'best_model_final.pth')
    
    # Store metrics
    train_losses.append(train_loss)
    train_accs.append(train_acc)
    val_losses.append(val_loss)
    val_accs.append(val_acc)
    val_top5_accs.append(val_top5_acc)
    
    print(f'Epoch [{epoch+1}/{num_epochs_phase2}] '
          f'Train Loss: {train_loss:.4f}, Train Acc: {train_acc:.2f}% | '
          f'Val Loss: {val_loss:.4f}, Val Acc: {val_acc:.2f}%, Top-5: {val_top5_acc:.2f}%')

phase2_time = time.time() - start_time
print(f"Phase 2 completed in {phase2_time:.2f} seconds")

# ------------------------------------------------------
# STEP 7: EVALUATE ON TEST SET
# ------------------------------------------------------
print("\n📊 Evaluating model on test set...")

# Load best model
model.load_state_dict(torch.load('best_model_final.pth'))

# Test evaluation
test_loss, test_acc, test_top5_acc = validate(model, test_loader, criterion, device)

print(f"\n🎯 Final Test Results:")
print(f"   Test Loss: {test_loss:.4f}")
print(f"   Test Accuracy: {test_acc:.2f}%")
print(f"   Top-5 Accuracy: {test_top5_acc:.2f}%")

# ------------------------------------------------------
# STEP 8: GENERATE PREDICTIONS FOR ANALYSIS
# ------------------------------------------------------
print("\n🔍 Generating predictions for detailed analysis...")

def get_predictions(model, loader, device):
    """Generate predictions for all samples"""
    model.eval()
    all_preds = []
    all_labels = []
    all_probs = []
    
    with torch.no_grad():
        for inputs, labels in loader:
            inputs, labels = inputs.to(device), labels.to(device)
            outputs = model(inputs)
            probabilities = torch.nn.functional.softmax(outputs, dim=1)
            _, predicted = torch.max(outputs, 1)
            
            all_preds.extend(predicted.cpu().numpy())
            all_labels.extend(labels.cpu().numpy())
            all_probs.extend(probabilities.cpu().numpy())
    
    return np.array(all_labels), np.array(all_preds), np.array(all_probs)

y_true, y_pred, y_pred_proba = get_predictions(model, test_loader, device)

# ------------------------------------------------------
# STEP 9: VISUALIZATION AND ANALYSIS
# ------------------------------------------------------

def plot_training_history(train_losses, train_accs, val_losses, val_accs, phase1_epochs):
    """Plot training history"""
    epochs = range(1, len(train_losses) + 1)
    
    plt.figure(figsize=(15, 5))
    
    # Accuracy plot
    plt.subplot(1, 2, 1)
    plt.plot(epochs, train_accs, 'b-', label='Training Accuracy')
    plt.plot(epochs, val_accs, 'r-', label='Validation Accuracy')
    plt.axvline(x=phase1_epochs, color='g', linestyle='--', alpha=0.7, label='Fine-tuning Start')
    plt.title('Model Accuracy')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy (%)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Loss plot
    plt.subplot(1, 2, 2)
    plt.plot(epochs, train_losses, 'b-', label='Training Loss')
    plt.plot(epochs, val_losses, 'r-', label='Validation Loss')
    plt.axvline(x=phase1_epochs, color='g', linestyle='--', alpha=0.7, label='Fine-tuning Start')
    plt.title('Model Loss')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()

print("📈 Plotting training history...")
plot_training_history(train_losses, train_accs, val_losses, val_accs, phase1_epochs)

# Confusion Matrix
print("\n📊 Generating confusion matrix...")
cm = confusion_matrix(y_true, y_pred)

plt.figure(figsize=(12, 10))
sns.heatmap(cm, cmap="Blues", cbar=True, square=True, 
            xticklabels=False, yticklabels=False)
plt.title(f"Confusion Matrix - {NUM_CLASSES} Flower Classes")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

# Classification Report
print("\n📋 Detailed Classification Report:")
print("="*60)
report = classification_report(y_true, y_pred, digits=4, output_dict=True)

# Display summary statistics
print(f"Overall Accuracy: {report['accuracy']:.4f}")
print(f"Macro Average Precision: {report['macro avg']['precision']:.4f}")
print(f"Macro Average Recall: {report['macro avg']['recall']:.4f}")
print(f"Macro Average F1-Score: {report['macro avg']['f1-score']:.4f}")
print(f"Weighted Average Precision: {report['weighted avg']['precision']:.4f}")
print(f"Weighted Average Recall: {report['weighted avg']['recall']:.4f}")
print(f"Weighted Average F1-Score: {report['weighted avg']['f1-score']:.4f}")

# Show per-class performance
print("\n🏆 Top 5 Best Performing Classes:")
class_performance = []
for i in range(NUM_CLASSES):
    if str(i) in report:
        class_performance.append((i, report[str(i)]['f1-score']))

class_performance.sort(key=lambda x: x[1], reverse=True)

for i, (class_id, f1_score) in enumerate(class_performance[:5]):
    print(f"  {i+1}. Class {class_id}: F1-Score = {f1_score:.4f}")

print("\n📉 Bottom 5 Performing Classes:")
for i, (class_id, f1_score) in enumerate(class_performance[-5:]):
    print(f"  {i+1}. Class {class_id}: F1-Score = {f1_score:.4f}")

# Model complexity analysis
total_params = sum(p.numel() for p in model.parameters())
trainable_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
non_trainable_params = total_params - trainable_params

print(f"\n🔧 Model Complexity:")
print(f"Total parameters: {total_params:,}")
print(f"Trainable parameters: {trainable_params:,}")
print(f"Non-trainable parameters: {non_trainable_params:,}")
print(f"Trainable ratio: {(trainable_params/total_params)*100:.2f}%")

print(f"\n⏱️ Training Time:")
print(f"Phase 1 (Head only): {phase1_time:.2f} seconds")
print(f"Phase 2 (Fine-tuning): {phase2_time:.2f} seconds")
print(f"Total training time: {phase1_time + phase2_time:.2f} seconds")

print("\n✅ Analysis complete!")
print("\n💡 Key Insights:")
print("- Transfer learning with MobileNetV2 provides excellent baseline performance")
print("- Fine-tuning improves model accuracy significantly")
print("- Data augmentation helps prevent overfitting")
print("- PyTorch provides flexible and efficient training workflow")
print("- The model achieves good performance with relatively few trainable parameters")

# Save final model
print(f"\n💾 Saving final model...")
torch.save({
    'model_state_dict': model.state_dict(),
    'model_architecture': 'MobileNetV2',
    'num_classes': NUM_CLASSES,
    'test_accuracy': test_acc,
    'test_top5_accuracy': test_top5_acc
}, 'flower_classifier_mobilenetv2_pytorch.pth')
print("Model saved as 'flower_classifier_mobilenetv2_pytorch.pth'")