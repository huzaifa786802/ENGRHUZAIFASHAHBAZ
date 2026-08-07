import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, r2_score
# Function to train a Decision Tree Regressor
def train_decision_tree(x, y, max_depth=None):
    x = x.reshape(-1, 1)  # Reshape for sklearn
    model = DecisionTreeRegressor(max_depth=max_depth, random_state=42)
    model.fit(x, y)
    return model
# Function to predict new values
def predict_values(model, x_new):
    x_new = x_new.reshape(-1, 1)
    return model.predict(x_new)
# Function to evaluate model performance
def evaluate_model(y_actual, y_predicted):
    mse = mean_squared_error(y_actual, y_predicted)
    r2 = r2_score(y_actual, y_predicted)
    return mse, r2
# Function to plot Decision Tree Regression results
def plot_decision_tree_regression(x, y, model, x_new=None, y_new=None):
    x_grid = np.arange(min(x), max(x), 0.1).reshape(-1, 1)  # High-resolution X
    y_pred_grid = model.predict(x_grid)  # Predictions for smooth curve
    # Plot actual data
    plt.scatter(x, y, color="m", marker="o", s=30, label="Actual data")
    # Plot Decision Tree Regression line
    plt.plot(x_grid, y_pred_grid, color="g", linestyle="--", label="Decision Tree Fit")
    # Plot new predictions if provided
    if x_new is not None and y_new is not None:
        plt.scatter(x_new, y_new, color="r", marker="x", s=100, label="Predicted points")
    # Labels, legend, and title
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Decision Tree Regression')
    plt.legend()
    plt.show()
# Main function
def main():
    # Training data
    x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    y = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12])
    # Train Decision Tree Regressor
    model = train_decision_tree(x, y, max_depth=3)
    # Predict new values
    x_new = np.array([10, 11, 12])  # New X values
    y_new = predict_values(model, x_new)
    # Print predicted values
    print("Predicted values for new X points:")
    for i in range(len(x_new)):
        print(f"X = {x_new[i]}, Predicted Y = {y_new[i]:.2f}")
    # Compute predictions for original dataset (for evaluation)
    y_pred_original = predict_values(model, x)
    # Evaluate model performance
    mse, r2 = evaluate_model(y, y_pred_original)
    print(f"Mean Squared Error (MSE): {mse:.2f}")
    print(f"R-squared Value (R2): {r2:.2f}")
    # Plot Decision Tree Regression results
    plot_decision_tree_regression(x, y, model, x_new, y_new)
# Running the script
if __name__ == "__main__":
    main()