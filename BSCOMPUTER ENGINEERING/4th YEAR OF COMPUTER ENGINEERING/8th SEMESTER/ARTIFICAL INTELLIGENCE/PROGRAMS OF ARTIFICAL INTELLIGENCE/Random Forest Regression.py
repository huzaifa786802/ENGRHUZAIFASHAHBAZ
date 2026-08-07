import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
# Generating sample data
np.random.seed(42)
X = np.sort(10 * np.random.rand(100, 1), axis=0)  # Random X values
y = np.sin(X).ravel() + np.random.normal(0, 0.1, X.shape[0])  # Non-linear function with noise
# Splitting data into training and testing sets
train_size = int(0.8 * len(X))
X_train, X_test = X[:train_size], X[train_size:]
y_train, y_test = y[:train_size], y[train_size:]
# Creating and training the Random Forest Regressor
rf_regressor = RandomForestRegressor(n_estimators=100, random_state=42)
rf_regressor.fit(X_train, y_train)
# Making predictions
y_pred_train = rf_regressor.predict(X_train)
y_pred_test = rf_regressor.predict(X_test)
# Evaluating the model
train_mse = mean_squared_error(y_train, y_pred_train)
test_mse = mean_squared_error(y_test, y_pred_test)
train_r2 = r2_score(y_train, y_pred_train)
test_r2 = r2_score(y_test, y_pred_test)
# Printing evaluation metrics
print(f"Train MSE: {train_mse:.4f}, Train R2: {train_r2:.4f}")
print(f"Test MSE: {test_mse:.4f}, Test R2: {test_r2:.4f}")
# Plotting the results
X_grid = np.linspace(0, 10, 500).reshape(-1, 1)  # More points for smoother curve
y_pred_grid = rf_regressor.predict(X_grid)

plt.scatter(X, y, color="blue", label="Actual Data")
plt.plot(X_grid, y_pred_grid, color="red", linewidth=2, label="Random Forest Regression")
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Random Forest Regression Model")
plt.legend()
plt.show()