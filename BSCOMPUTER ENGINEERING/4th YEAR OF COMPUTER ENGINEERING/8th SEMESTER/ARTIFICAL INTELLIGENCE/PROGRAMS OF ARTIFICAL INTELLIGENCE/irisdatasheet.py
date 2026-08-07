import numpy as np
import matplotlib.pyplot as plt 
from matplotlib.colors import ListedColormap
from scipy.stats import mode
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.datasets import load_iris
from numpy.random import randint
# Function Definitions
# Euclidean Distance Function
def euclidean(p1, p2):
    return np.sqrt(np.sum((p1 - p2) ** 2))
# KNN Prediction Function
def predict(x_train, y_train, x_input, k):
    op_labels = []
    for item in x_input:
        point_dist = [(euclidean(x_train[j], item), y_train[j]) for j in range(len(x_train))]
        point_dist.sort(key=lambda x: x[0])  # Sort by distance
        k_nearest_labels = [label for _, label in point_dist[:k]]
        most_common = mode(k_nearest_labels, keepdims=True)  # Majority voting
        op_labels.append(most_common.mode[0])
    return np.array(op_labels)
# Load Dataset
iris = load_iris()
X = iris.data
y = iris.target
feature_names = iris.feature_names
target_names = iris.target_names
# Train-Test Split
np.random.seed(42)  # For reproducibility
train_indices = randint(0, 150, 100)
test_indices = np.array([i for i in range(150) if i not in train_indices])[:50]
X_train, y_train = X[train_indices], y[train_indices]
X_test, y_test = X[test_indices], y[test_indices]
# Apply KNN
k = 7  # Number of neighbors
y_pred = predict(X_train, y_train, X_test, k)
# Compute Accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.4f}")
# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(cm)
# Data Visualization
# Select only two features for visualization (Sepal Length & Sepal Width)
feature_idx = [0, 1]
X_train_2d, X_test_2d = X_train[:, feature_idx], X_test[:, feature_idx]
# Create Mesh Grid for Decision Boundary
h = 0.02  # Step size
x_min, x_max = X[:, feature_idx[0]].min() - 1, X[:, feature_idx[0]].max() + 1
y_min, y_max = X[:, feature_idx[1]].min() - 1, X[:, feature_idx[1]].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
# Predict for Each Grid Point
Z = predict(X_train_2d, y_train, np.c_[xx.ravel(), yy.ravel()], k)
Z = Z.reshape(xx.shape)
# Define Color Maps
cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])
# Plot Figures
plt.figure(figsize=(12, 10))
# 1. KNN Decision Boundary
plt.subplot(2, 2, 1)
plt.contourf(xx, yy, Z, alpha=0.4, cmap=cmap_light)
plt.scatter(X_train_2d[:, 0], X_train_2d[:, 1], c=y_train, cmap=cmap_bold, edgecolor='k', s=40)
plt.scatter(X_test_2d[:, 0], X_test_2d[:, 1], c=y_test, cmap=cmap_bold, marker='*', s=100, edgecolor='k')
plt.xlabel(feature_names[feature_idx[0]])
plt.ylabel(feature_names[feature_idx[1]])
plt.title(f'KNN Decision Boundary (k={k})')
plt.legend(['Training data', 'Test data'])
# 2. Iris Dataset Distribution (Sepal Length vs Sepal Width)
plt.subplot(2, 2, 2)
for i, color in zip(range(3), ['red', 'green', 'blue']):
    plt.scatter(X[y == i, 0], X[y == i, 1], color=color, alpha=0.7, label=target_names[i])
plt.xlabel(feature_names[0])
plt.ylabel(feature_names[1])
plt.title('Iris Dataset: Sepal Length vs Sepal Width')
plt.legend()
# 3. Correct vs Incorrect Predictions
plt.subplot(2, 2, 3)
correct = y_pred == y_test
plt.scatter(X_test_2d[correct, 0], X_test_2d[correct, 1], c=y_test[correct], cmap=cmap_bold, marker='o', s=80, edgecolor='k', label='Correct')
plt.scatter(X_test_2d[~correct, 0], X_test_2d[~correct, 1], c=y_test[~correct], cmap=cmap_bold, marker='x', s=100, edgecolor='k', label='Incorrect')
plt.xlabel(feature_names[feature_idx[0]])
plt.ylabel(feature_names[feature_idx[1]])
plt.title(f'KNN Predictions: Correct vs Incorrect (k={k})')
plt.legend()
# 4. Accuracy vs k values
plt.subplot(2, 2, 4)
k_values = range(1, 15, 2)
accuracy_values = [accuracy_score(y_test, predict(X_train, y_train, X_test, k_val)) for k_val in k_values]
plt.plot(k_values, accuracy_values, 'o-', color='blue')
plt.axvline(x=k, color='red', linestyle='--', label=f'k={k}')
plt.xlabel('k value')
plt.ylabel('Accuracy')
plt.title('Accuracy vs k value')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
# Print Accuracy for Different k Values
print("\nAccuracy for different k values:")
for k_val, acc in zip(k_values, accuracy_values):
    print(f"k = {k_val}: {acc:.4f}")