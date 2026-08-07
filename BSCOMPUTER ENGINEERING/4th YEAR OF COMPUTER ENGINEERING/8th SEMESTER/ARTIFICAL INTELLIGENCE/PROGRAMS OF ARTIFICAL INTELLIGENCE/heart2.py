import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
# 1. Load the dataset
df = pd.read_csv("heart2.csv")
# Show the first few rows to understand the structure of heartdisease patients dataset
print("Initial Dataset Preview:")
print(df.head())
# Store the original labeled dataset
df_labeled = df.copy()
# Create a version without the target column (assuming the target column is named 'target')
if 'target' not in df.columns:
    raise ValueError("Target column 'target' not found in dataset.")
df_unlabeled = df.drop(columns=['target'])
# 2. Preprocessing: Check for missing values
print("\nChecking for missing values:")
print(df.isnull().sum())
# Feature scaling
scaler = StandardScaler()
X = df_labeled.drop(columns=['target'])
X_scaled = scaler.fit_transform(X)
# Reassign scaled data to a DataFrame for clarity
X_scaled_df = pd.DataFrame(X_scaled, columns=X.columns)
# Target variable
y = df_labeled['target']
# 3. Split the labeled data
X_train, X_test, y_train, y_test = train_test_split(X_scaled_df, y, test_size=0.2, random_state=42)
# 4. Implement KNN with k=5
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
# Predictions on the test set
y_pred = knn.predict(X_test)
# Evaluation
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
print(f"\nModel Accuracy: {accuracy:.2f}")
print("Confusion Matrix:")
print(conf_matrix)
# 5. Predict on the unlabeled version
df_unlabeled_scaled = scaler.transform(df_unlabeled)
predicted_labels = knn.predict(df_unlabeled_scaled)
# Display predicted labels
print("\nPredicted Labels for Unlabeled Dataset:")
print(predicted_labels)