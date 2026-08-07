# Import required libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.svm import SVC
# Load dataset
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pd.read_csv(url, names=names)
# Split-out validation dataset
array = dataset.values
X = array[:, 0:4]  # Features
y = array[:, 4]    # Target variable
# Split the data into training and validation sets
X_train, X_validation, Y_train, Y_validation = train_test_split(X, y, test_size=0.20, random_state=1)
# Create and train the SVM model
model = SVC(gamma='auto')
model.fit(X_train, Y_train)
# Make predictions on the validation dataset
predictions = model.predict(X_validation)
# Evaluate the model
print("Accuracy Score:")
print(accuracy_score(Y_validation, predictions))
print("\nConfusion Matrix:")
print(confusion_matrix(Y_validation, predictions))
print("\nClassification Report:")
print(classification_report(Y_validation, predictions))