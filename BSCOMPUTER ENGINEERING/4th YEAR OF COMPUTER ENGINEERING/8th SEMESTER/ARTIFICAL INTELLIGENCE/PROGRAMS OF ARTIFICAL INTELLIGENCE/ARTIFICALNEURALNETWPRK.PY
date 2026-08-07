import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
# Step 1: Load the Iris dataset
iris = load_iris()
X = iris.data # Features (4 features per sample)
y = iris.target # Target classes (3 classes)
# Step 2: Preprocess the data (use only two classes for binary classification)
# We will classify class 0 (Setosa) vs class 1 (Versicolor)
X = X[y != 2] # Remove class 2 (Virginica)
y = y[y != 2] # Remove class 2 (Virginica)
# Step 3: Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Step 4: Standardize the data (helpful for ANN performance)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
# Step 5: Build the ANN model
model = Sequential()
# Input layer and first hidden layer with 8 neurons and ReLU activation
model.add(Dense(units=8, input_dim=X_train.shape[1], activation='relu'))
# Output layer with 1 neuron and sigmoid activation (for binary classification)
model.add(Dense(units=1, activation='sigmoid'))
# Step 6: Compile the model
model.compile(loss='binary_crossentropy', # For binary classification
optimizer='adam', # Optimizer
metrics=['accuracy']) # Evaluation metric
# Step 7: Train the model
history = model.fit(X_train, y_train, epochs=50, batch_size=10, validation_split=0.2)
# Step 8: Evaluate the model
y_pred_prob = model.predict(X_test)
y_pred = (y_pred_prob > 0.5).astype(int) # Convert probabilities to binary predictions
# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")
# Optional: Plotting training history (loss and accuracy)
import matplotlib.pyplot as plt
plt.figure(figsize=(12, 6))
# Plotting loss
plt.subplot(1, 2, 1)
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.title('Loss during Training')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
# Plotting accuracy
plt.subplot(1, 2, 2)
plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.title('Accuracy during Training')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.show()