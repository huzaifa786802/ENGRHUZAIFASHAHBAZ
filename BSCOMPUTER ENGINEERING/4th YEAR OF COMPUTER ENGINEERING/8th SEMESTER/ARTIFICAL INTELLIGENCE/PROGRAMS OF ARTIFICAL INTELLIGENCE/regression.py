# Import necessary libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score, KFold
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
# Load dataset
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pd.read_csv(url, names=names)
# Select features (X) and target variable (y)
X = dataset[['sepal-width', 'petal-length', 'petal-width']]  # Independent variables
y = dataset['sepal-length']  # Dependent variable (continuous)
# Split dataset into training and testing
X_train, X_validation, y_train, y_validation = train_test_split(X, y, test_size=0.20, random_state=1)
# Train Linear Regression Model
lin_model = LinearRegression()
lin_model.fit(X_train, y_train)
lin_predictions = lin_model.predict(X_validation)
# Train Polynomial Regression (Degree 2)
poly_model = make_pipeline(PolynomialFeatures(degree=2), LinearRegression())
poly_model.fit(X_train, y_train)
poly_predictions = poly_model.predict(X_validation)
# Evaluate Models
def evaluate_model(name, y_true, y_pred):
    print(f"🔹 {name} Model Performance:")
    print(f"   - Mean Absolute Error (MAE): {mean_absolute_error(y_true, y_pred):.4f}")
    print(f"   - Mean Squared Error (MSE): {mean_squared_error(y_true, y_pred):.4f}")
    print(f"   - R-squared Score (R²): {r2_score(y_true, y_pred):.4f}")
    print("-" * 40)
evaluate_model("Linear Regression", y_validation, lin_predictions)
evaluate_model("Polynomial Regression", y_validation, poly_predictions)