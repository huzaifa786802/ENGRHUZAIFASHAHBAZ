import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import GridSearchCV
# Load the California housing dataset as an example regression dataset
housing = fetch_california_housing()
X = pd.DataFrame(housing.data, columns=housing.feature_names)
y = housing.target
# Display information about the dataset
print("Dataset Information:")
print(f"Number of samples: {X.shape[0]}")
print(f"Number of features: {X.shape[1]}")
print("\nFeature names:")
print(housing.feature_names)
print("\nTarget description:")
print(housing.DESCR.split('\n')[4])  # Extract target description from dataset description
# Show the first 5 rows of the dataset with features and target
data_with_target = X.copy()
data_with_target['Target (MedHouseValue)'] = y
print("\nFirst 5 rows of the dataset:")
print(data_with_target.head())
# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Scale the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
# Find the optimal value of K using GridSearchCV
param_grid = {'n_neighbors': np.arange(3, 21, 2)}
knn_grid = GridSearchCV(KNeighborsRegressor(), param_grid, cv=5, scoring='neg_mean_squared_error')
knn_grid.fit(X_train_scaled, y_train)
# Print the best parameter
best_k = knn_grid.best_params_['n_neighbors']
print(f"\nBest value of K: {best_k}")
# Train KNN regression model with the best K
knn_model = KNeighborsRegressor(n_neighbors=best_k)
knn_model.fit(X_train_scaled, y_train)
# Make predictions
y_pred = knn_model.predict(X_test_scaled)
# Evaluate the model using various metrics
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print("\nModel Evaluation Metrics:")
print(f"Mean Squared Error (MSE): {mse:.4f}")
print(f"Root Mean Squared Error (RMSE): {rmse:.4f}")
print(f"Mean Absolute Error (MAE): {mae:.4f}")
print(f"R-squared (R²): {r2:.4f}")
# Calculate additional metrics
explained_variance = 1 - (np.var(y_test - y_pred) / np.var(y_test))
mape = np.mean(np.abs((y_test - y_pred) / y_test)) * 100
print(f"Explained Variance: {explained_variance:.4f}")
print(f"Mean Absolute Percentage Error (MAPE): {mape:.4f}%")
# Visualize actual vs predicted values
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, alpha=0.5)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
plt.xlabel('Actual Values')
plt.ylabel('Predicted Values')
plt.title('KNN Regression: Actual vs Predicted Values')
plt.tight_layout()
plt.show()
# Visualize error distribution
errors = y_test - y_pred
plt.figure(figsize=(10, 6))
plt.hist(errors, bins=30)
plt.xlabel('Prediction Error')
plt.ylabel('Count')
plt.title('Distribution of Prediction Errors')
plt.axvline(x=0, color='r', linestyle='--')
plt.tight_layout()
plt.show()
# Visualize the effect of K on model performance
k_range = range(1, 31)
k_mse = []
k_r2 = []
for k in k_range:
    knn = KNeighborsRegressor(n_neighbors=k)
    knn.fit(X_train_scaled, y_train)
    y_pred_k = knn.predict(X_test_scaled)
    k_mse.append(mean_squared_error(y_test, y_pred_k))
    k_r2.append(r2_score(y_test, y_pred_k))
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.plot(k_range, k_mse)
plt.xlabel('Value of K')
plt.ylabel('MSE')
plt.title('MSE vs. K Value')
plt.subplot(1, 2, 2)
plt.plot(k_range, k_r2)
plt.xlabel('Value of K')
plt.ylabel('R²')
plt.title('R² vs. K Value')
plt.tight_layout()
plt.show()