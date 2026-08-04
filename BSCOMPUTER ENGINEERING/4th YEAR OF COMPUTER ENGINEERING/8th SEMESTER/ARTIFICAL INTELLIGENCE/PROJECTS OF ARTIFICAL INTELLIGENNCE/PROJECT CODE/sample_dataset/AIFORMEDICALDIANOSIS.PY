import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Conv2D, MaxPooling2D, Dropout, BatchNormalization
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
import heapq
# -------------------- Load and Preprocess Images --------------------
def load_images_from_folder(folder, img_size=64):
    """
    Load images from a folder structure where each subfolder represents a class
    Returns images, labels, and a mapping of class names to numeric labels
    """
    images = []
    labels = []
    label_map = {}  # String labels to numbers
    label_counter = 0
    # Check if folder exists
    if not os.path.exists(folder):
        print(f"Error: Folder '{folder}' does not exist!")
        return np.array([]), np.array([]), {}
    for label_name in os.listdir(folder):
        label_folder = os.path.join(folder, label_name)
        if os.path.isdir(label_folder):
            if label_name not in label_map:
                label_map[label_name] = label_counter
                label_counter += 1
            print(f"Loading images from class: {label_name}")
            file_count = 0
            for filename in os.listdir(label_folder):
                img_path = os.path.join(label_folder, filename)
                try:
                    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
                    if img is not None:
                        img = cv2.resize(img, (img_size, img_size))
                        images.append(img)
                        labels.append(label_map[label_name])
                        file_count += 1
                except Exception as e:
                    print(f"Error loading {img_path}: {e}")
            print(f"  - Loaded {file_count} images")
    # Create reverse mapping (numeric to string)
    reverse_label_map = {v: k for k, v in label_map.items()}
    print(f"Total images loaded: {len(images)}")
    print(f"Classes found: {list(label_map.keys())}")
    return np.array(images), np.array(labels), label_map, reverse_label_map
# -------------------- ANN Model --------------------
def build_ann(input_shape, num_classes):
    """Build a simple Artificial Neural Network"""
    model = Sequential([
        Flatten(input_shape=input_shape),
        Dense(128, activation='relu'),
        Dropout(0.2),  # Add dropout for regularization
        Dense(64, activation='relu'),
        Dense(num_classes, activation='softmax')
    ])
    model.summary()
    return model
# -------------------- CNN Model --------------------
def build_cnn(input_shape, num_classes):
    """Build a Convolutional Neural Network"""
    model = Sequential([
        Conv2D(32, (3,3), activation='relu', padding='same', input_shape=input_shape),
        MaxPooling2D(pool_size=(2,2)),
        Conv2D(64, (3,3), activation='relu', padding='same'),
        MaxPooling2D(pool_size=(2,2)),
        Conv2D(128, (3,3), activation='relu', padding='same'),
        MaxPooling2D(pool_size=(2,2)),
        Flatten(),
        Dense(128, activation='relu'),
        Dropout(0.3),
        Dense(num_classes, activation='softmax')
    ])
    model.summary()
    return model
# -------------------- BNN (Simulated via Binary Activation) --------------------
def build_bnn(input_shape, num_classes):
    """
    Build a network that simulates some aspects of Binary Neural Networks
    Note: This is not a true BNN as it doesn't use binary weights
    """
    model = Sequential([
        Flatten(input_shape=input_shape),
        Dense(128, activation='relu'),
        BatchNormalization(),
        Dense(64, activation='relu'),
        BatchNormalization(),
        Dense(num_classes, activation='softmax')
    ])
    model.summary()
    return model
# -------------------- Graph Search Algorithms --------------------
def dfs(graph, start, goal, visited=None):
    """Depth-First Search algorithm for graph traversal"""
    if visited is None:
        visited = set()
    visited.add(start)
    if start == goal:
        return [start]
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            path = dfs(graph, neighbor, goal, visited)
            if path:
                return [start] + path 
    return None
def bfs(graph, start, goal):
    """Breadth-First Search algorithm for graph traversal"""
    visited = set()
    queue = [[start]]
    if start == goal:
        return [start]
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node == goal:
            return path
        elif node not in visited:
            for neighbor in graph.get(node, []):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
            visited.add(node)
    return None
def best_first_search(graph, start, goal, heuristic):
    """Best-First Search algorithm using a heuristic function"""
    visited = set()
    heap = [(heuristic.get(start, float('inf')), [start])]
    while heap:
        _, path = heapq.heappop(heap)
        node = path[-1]
        if node == goal:
            return path
        if node not in visited:
            visited.add(node)
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    new_path = path + [neighbor]
                    heapq.heappush(heap, (heuristic.get(neighbor, float('inf')), new_path))     
    return None
def beam_search(graph, start, goal, heuristic, beam_width=2):
    """Beam Search algorithm with specified beam width"""
    if start == goal:
        return [start]
    queue = [[start]]
    visited = set([start])
    while queue:
        # Sort by heuristic value and keep only up to beam_width paths
        queue.sort(key=lambda path: heuristic.get(path[-1], float('inf')))
        queue = queue[:beam_width]
        next_queue = []
        for path in queue:
            node = path[-1]
            if node == goal:
                return path
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    new_path = list(path)
                    new_path.append(neighbor)
                    next_queue.append(new_path)
        queue = next_queue
        if not queue:  # If queue is empty, no path exists
            break
    return None
# -------------------- Evaluation Function --------------------
def evaluate_model(model, x_test, y_test, class_names=None):
    """Evaluate model performance and display metrics and visualizations"""
    # Get predictions
    y_pred_prob = model.predict(x_test)
    y_pred_classes = np.argmax(y_pred_prob, axis=1)
    y_test_classes = np.argmax(y_test, axis=1)
    # Print classification report
    if class_names:
        target_names = [class_names.get(i, f"Class {i}") for i in range(len(np.unique(y_test_classes)))]
        print("\nClassification Report:")
        print(classification_report(y_test_classes, y_pred_classes, target_names=target_names))
    else:
        print("\nClassification Report:")
        print(classification_report(y_test_classes, y_pred_classes))
    # Print confusion matrix
    cm = confusion_matrix(y_test_classes, y_pred_classes)
    print("\nConfusion Matrix:")
    print(cm)
    # Plot confusion matrix as heatmap
    plt.figure(figsize=(10, 8))
    plt.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)
    plt.title('Confusion Matrix')
    plt.colorbar()
    if class_names:
        tick_marks = np.arange(len(np.unique(y_test_classes)))
        class_labels = [class_names.get(i, f"Class {i}") for i in range(len(np.unique(y_test_classes)))]
        plt.xticks(tick_marks, class_labels, rotation=45)
        plt.yticks(tick_marks, class_labels)
    plt.tight_layout()
    plt.ylabel('True Label')
    plt.xlabel('Predicted Label')
    plt.show()
    # Plot sample misclassifications
    misclassified = np.where(y_pred_classes != y_test_classes)[0]
    if len(misclassified) > 0:
        n_display = min(5, len(misclassified))
        plt.figure(figsize=(15, 3))
        for i, idx in enumerate(misclassified[:n_display]):
            plt.subplot(1, n_display, i+1)
            # If grayscale image
            if x_test[idx].shape[-1] == 1:
                plt.imshow(x_test[idx].reshape(x_test[idx].shape[0], x_test[idx].shape[1]), cmap='gray')
            else:
                plt.imshow(x_test[idx])
            true_class = y_test_classes[idx]
            pred_class = y_pred_classes[idx]
            
            if class_names:
                true_label = class_names.get(true_class, f"Class {true_class}")
                pred_label = class_names.get(pred_class, f"Class {pred_class}")
                plt.title(f"True: {true_label}\nPred: {pred_label}")
            else:
                plt.title(f"True: {true_class}\nPred: {pred_class}")
            plt.axis('off')
        plt.tight_layout()
        plt.show()
    
    return y_pred_classes, y_test_classes

# -------------------- Create Sample Dataset --------------------
def create_sample_dataset(output_folder='sample_dataset', num_classes=3, samples_per_class=50, img_size=64):
    """Create a sample dataset for demonstration purposes"""
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        
    shapes = ['circle', 'square', 'triangle']
    
    for i in range(min(num_classes, len(shapes))):
        class_folder = os.path.join(output_folder, shapes[i])
        if not os.path.exists(class_folder):
            os.makedirs(class_folder)
        
        print(f"Creating {samples_per_class} {shapes[i]} images...")
        
        for j in range(samples_per_class):
            # Create a blank image
            img = np.zeros((img_size, img_size), dtype=np.uint8)
            
            # Add some randomness to position and size
            center_x = np.random.randint(img_size//4, 3*img_size//4)
            center_y = np.random.randint(img_size//4, 3*img_size//4)
            size = np.random.randint(img_size//4, img_size//2)
            
            # Draw shape based on class
            if shapes[i] == 'circle':
                cv2.circle(img, (center_x, center_y), size//2, 255, -1)
            elif shapes[i] == 'square':
                x1 = max(0, center_x - size//2)
                y1 = max(0, center_y - size//2)
                x2 = min(img_size-1, center_x + size//2)
                y2 = min(img_size-1, center_y + size//2)
                cv2.rectangle(img, (x1, y1), (x2, y2), 255, -1)
            elif shapes[i] == 'triangle':
                points = np.array([
                    [center_x, center_y - size//2],
                    [center_x - size//2, center_y + size//2],
                    [center_x + size//2, center_y + size//2]
                ])
                cv2.fillPoly(img, [points], 255)
            # Add some noise
            noise = np.random.normal(0, 15, img.shape).astype(np.uint8)
            img = cv2.add(img, noise)
            # Save image
            cv2.imwrite(os.path.join(class_folder, f"{shapes[i]}_{j}.png"), img)
    print(f"Sample dataset created at {output_folder}")
    return output_folder
# -------------------- Main Function --------------------
def main():
    # 1. Create sample dataset if needed
    use_sample_data = True
    if use_sample_data:
        image_folder = create_sample_dataset(num_classes=3, samples_per_class=100)
    else:
        # Use your own dataset path here
        image_folder = 'path_to_your_dataset'  
    # 2. Load Dataset
    images, labels, label_map, reverse_label_map = load_images_from_folder(image_folder)
    if len(images) == 0:
        print("No images loaded. Exiting...")
        return
    # Normalize images
    images = images / 255.0
    # Add channel dimension for grayscale images
    images = np.expand_dims(images, axis=-1)
    # One-hot encode labels
    labels_categorical = to_categorical(labels)
    # Split dataset
    x_train, x_test, y_train, y_test = train_test_split(images, labels_categorical, test_size=0.2, random_state=42)
    print(f"\nDataset split: {x_train.shape[0]} training samples, {x_test.shape[0]} test samples")
    print(f"Image shape: {x_train.shape[1:]}")
    input_shape = x_train.shape[1:]
    num_classes = y_train.shape[1]
    # 3. Run neural network training and evaluation
    run_neural_networks = True
    if run_neural_networks:
        # Build and Train ANN
        print("\n" + "="*50)
        print("TRAINING ARTIFICIAL NEURAL NETWORK (ANN)")
        print("="*50)
        ann = build_ann(input_shape, num_classes)
        ann.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
        ann_history = ann.fit(
            x_train, y_train, 
            epochs=10, 
            batch_size=32,
            validation_data=(x_test, y_test),
            verbose=1
        )
        print("\n" + "="*50)
        print("ANN EVALUATION")
        print("="*50)
        ann_results = evaluate_model(ann, x_test, y_test, reverse_label_map)
        # Plot training history
        plt.figure(figsize=(12, 4))
        plt.subplot(1, 2, 1)
        plt.plot(ann_history.history['accuracy'], label='Train Accuracy')
        plt.plot(ann_history.history['val_accuracy'], label='Validation Accuracy')
        plt.title('ANN Accuracy')
        plt.xlabel('Epoch')
        plt.ylabel('Accuracy')
        plt.legend()
        plt.subplot(1, 2, 2)
        plt.plot(ann_history.history['loss'], label='Train Loss')
        plt.plot(ann_history.history['val_loss'], label='Validation Loss')
        plt.title('ANN Loss')
        plt.xlabel('Epoch')
        plt.ylabel('Loss')
        plt.legend()
        plt.tight_layout()
        plt.show()
        # Build and Train CNN
        print("\n" + "="*50)
        print("TRAINING CONVOLUTIONAL NEURAL NETWORK (CNN)")
        print("="*50)
        cnn = build_cnn(input_shape, num_classes)
        cnn.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
        cnn_history = cnn.fit(
            x_train, y_train, 
            epochs=10, 
            batch_size=32,
            validation_data=(x_test, y_test),
            verbose=1
        )
        print("\n" + "="*50)
        print("CNN EVALUATION")
        print("="*50)
        cnn_results = evaluate_model(cnn, x_test, y_test, reverse_label_map)
        # Plot training history
        plt.figure(figsize=(12, 4))
        plt.subplot(1, 2, 1)
        plt.plot(cnn_history.history['accuracy'], label='Train Accuracy')
        plt.plot(cnn_history.history['val_accuracy'], label='Validation Accuracy')
        plt.title('CNN Accuracy')
        plt.xlabel('Epoch')
        plt.ylabel('Accuracy')
        plt.legend()
        plt.subplot(1, 2, 2)
        plt.plot(cnn_history.history['loss'], label='Train Loss')
        plt.plot(cnn_history.history['val_loss'], label='Validation Loss')
        plt.title('CNN Loss')
        plt.xlabel('Epoch')
        plt.ylabel('Loss')
        plt.legend()
        plt.tight_layout()
        plt.show()
        # Build and Train BNN (simulated)
        print("\n" + "="*50)
        print("TRAINING BINARY NEURAL NETWORK (BNN SIMULATION)")
        print("="*50)
        bnn = build_bnn(input_shape, num_classes)
        bnn.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
        bnn_history = bnn.fit(
            x_train, y_train, 
            epochs=10, 
            batch_size=32,
            validation_data=(x_test, y_test),
            verbose=1
        )
        print("\n" + "="*50)
        print("BNN EVALUATION")
        print("="*50)
        bnn_results = evaluate_model(bnn, x_test, y_test, reverse_label_map)
        # Plot training history
        plt.figure(figsize=(12, 4))
        plt.subplot(1, 2, 1)
        plt.plot(bnn_history.history['accuracy'], label='Train Accuracy')
        plt.plot(bnn_history.history['val_accuracy'], label='Validation Accuracy')
        plt.title('BNN Accuracy')
        plt.xlabel('Epoch')
        plt.ylabel('Accuracy')
        plt.legend()
        plt.subplot(1, 2, 2)
        plt.plot(bnn_history.history['loss'], label='Train Loss')
        plt.plot(bnn_history.history['val_loss'], label='Validation Loss')
        plt.title('BNN Loss')
        plt.xlabel('Epoch')
        plt.ylabel('Loss')
        plt.legend()
        plt.tight_layout()
        plt.show()
        # Compare models
        plt.figure(figsize=(12, 5))
        plt.subplot(1, 2, 1)
        plt.plot(ann_history.history['val_accuracy'], label='ANN')
        plt.plot(cnn_history.history['val_accuracy'], label='CNN')
        plt.plot(bnn_history.history['val_accuracy'], label='BNN')
        plt.title('Model Comparison - Validation Accuracy')
        plt.xlabel('Epoch')
        plt.ylabel('Accuracy')
        plt.legend()
        plt.subplot(1, 2, 2)
        plt.plot(ann_history.history['val_loss'], label='ANN')
        plt.plot(cnn_history.history['val_loss'], label='CNN')
        plt.plot(bnn_history.history['val_loss'], label='BNN')
        plt.title('Model Comparison - Validation Loss')
        plt.xlabel('Epoch')
        plt.ylabel('Loss')
        plt.legend()
        plt.tight_layout()
        plt.show()
    # 4. Graph Algorithms (Example for Decision Flow)
    run_graph_algorithms = True
    if run_graph_algorithms:
        print("\n" + "="*50)
        print("GRAPH SEARCH ALGORITHMS")
        print("="*50)
        # Define a sample graph
        graph = {
            'Start': ['A', 'B'],
            'A': ['C', 'D'],
            'B': ['E'],
            'C': ['F'],
            'D': [],
            'E': ['G'],
            'F': [],
            'G': ['Goal'],
            'Goal': []
        }
        # Heuristic values (estimated distance to goal)
        heuristic = {'Start': 6, 'A': 4, 'B': 3, 'C': 3, 'D': 4, 'E': 2, 'F': 2, 'G': 1, 'Goal': 0}
        # Visualize the graph
        plt.figure(figsize=(10, 6))
        # Node positions (manually defined for this example)
        positions = {
            'Start': (1, 4),
            'A': (3, 6),
            'B': (3, 2),
            'C': (5, 7),
            'D': (5, 5),
            'E': (5, 2),
            'F': (7, 7),
            'G': (7, 2),
            'Goal': (9, 4)
        }
        # Draw nodes
        for node, pos in positions.items():
            plt.plot(pos[0], pos[1], 'o', markersize=20, color='lightblue')
            plt.text(pos[0], pos[1], f"{node}\n(h={heuristic.get(node, 'N/A')})", 
                     ha='center', va='center', fontweight='bold')
        # Draw edges
        for node, neighbors in graph.items():
            for neighbor in neighbors:
                plt.plot([positions[node][0], positions[neighbor][0]],
                         [positions[node][1], positions[neighbor][1]], 'k-', alpha=0.6)
        plt.title("Example Graph with Heuristic Values")
        plt.axis('off')
        plt.tight_layout()
        plt.show()
        # Execute graph search algorithms
        dfs_path = dfs(graph, 'Start', 'Goal')
        bfs_path = bfs(graph, 'Start', 'Goal')
        best_first_path = best_first_search(graph, 'Start', 'Goal', heuristic)
        beam_path = beam_search(graph, 'Start', 'Goal', heuristic, beam_width=2)
        # Print results
        print("\nGraph Search Results:")
        print(f"DFS Path: {dfs_path}")
        print(f"BFS Path: {bfs_path}")
        print(f"Best-First Search Path: {best_first_path}")
        print(f"Beam Search Path (width=2): {beam_path}")
        # Visualize search paths
        algorithms = {
            'DFS': dfs_path,
            'BFS': bfs_path,
            'Best-First Search': best_first_path,
            'Beam Search (width=2)': beam_path
        }
        plt.figure(figsize=(15, 10))
        for i, (name, path) in enumerate(algorithms.items(), 1):
            plt.subplot(2, 2, i)
            # Draw nodes
            for node, pos in positions.items():
                if node in path:
                    color = 'lightgreen'
                    if node == 'Start':
                        color = 'green'
                    elif node == 'Goal':
                        color = 'red'
                else:
                    color = 'lightblue'
                plt.plot(pos[0], pos[1], 'o', markersize=20, color=color)
                plt.text(pos[0], pos[1], node, ha='center', va='center', fontweight='bold')
            # Draw edges
            for node, neighbors in graph.items():
                for neighbor in neighbors:
                    if node in path and neighbor in path and path.index(neighbor) == path.index(node) + 1:
                        plt.plot([positions[node][0], positions[neighbor][0]],
                                 [positions[node][1], positions[neighbor][1]], 'r-', linewidth=2.5)
                    else:
                        plt.plot([positions[node][0], positions[neighbor][0]],
                                 [positions[node][1], positions[neighbor][1]], 'k-', alpha=0.3)
            plt.title(f"{name}: {' → '.join(path) if path else 'No path found'}")
            plt.axis('off')
        plt.tight_layout()
        plt.show()
if __name__ == '__main__':
    main()