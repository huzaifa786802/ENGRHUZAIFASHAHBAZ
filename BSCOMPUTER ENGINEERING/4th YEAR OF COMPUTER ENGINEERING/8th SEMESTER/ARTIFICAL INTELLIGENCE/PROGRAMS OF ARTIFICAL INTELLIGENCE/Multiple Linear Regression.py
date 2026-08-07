import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
# Generate sample dataset (X: independent variables, y: dependent variable)
X = np.array([[1, 2], [2, 3], [3, 5], [4, 7], [5, 8],[6, 8], [7, 10], [8, 11], [9, 13], [10, 15]])  # Two independent variables
y = np.array([2, 3, 5, 6, 8, 8, 10, 11, 13, 15])  # Dependent variable
# Create and train the Multiple Linear Regression model
model = LinearRegression()
model.fit(X, y)
# Get regression coefficients
b_0 = model.intercept_  # Intercept (b_0)
b = model.coef_  # Coefficients (b_1, b_2, ...)
print(f"Regression Coefficients: b_0 = {b_0:.2f}, b_1 = {b[0]:.2f}, b_2 = {b[1]:.2f}")
# Predict values for the training set
y_pred = model.predict(X)
# Evaluate model performance
mse = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)
print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"R-squared Value (R2): {r2:.2f}")
# Predict values for new data points
X_new = np.array([[11, 16], [12, 18], [13, 20]])  # New independent variable values
y_new_pred = model.predict(X_new)
print("Predicted values for new data points:")
for i in range(len(X_new)):
    print(f"X = {X_new[i]}, Predicted Y = {y_new_pred[i]:.2f}")
# 3D Plot of Multiple Linear Regression (for two independent variables)
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
# Scatter plot of actual data
ax.scatter(X[:, 0], X[:, 1], y, color='m', marker='o', label="Actual data")
# Create a surface plot for regression plane
X1_range = np.linspace(X[:, 0].min(), X[:, 0].max(), 10)
X2_range = np.linspace(X[:, 1].min(), X[:, 1].max(), 10)
X1_grid, X2_grid = np.meshgrid(X1_range, X2_range)
Y_pred_grid = b_0 + b[0] * X1_grid + b[1] * X2_grid
ax.plot_surface(X1_grid, X2_grid, Y_pred_grid, color='cyan', alpha=0.5)
# Plot predicted new data points
ax.scatter(X_new[:, 0], X_new[:, 1], y_new_pred, color='r', marker='x', s=100, label="Predicted points")
# Labels and legend
ax.set_xlabel('X1')
ax.set_ylabel('X2')
ax.set_zlabel('Y')
ax.set_title('Multiple Linear Regression (3D)')
ax.legend()
# Show plot
plt.show()