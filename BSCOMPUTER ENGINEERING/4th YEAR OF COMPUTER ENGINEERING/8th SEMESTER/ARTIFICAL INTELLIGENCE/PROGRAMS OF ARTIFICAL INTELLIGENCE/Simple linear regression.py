import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score
# Function to estimate regression coefficients
def estimate_coef(x, y):
    n = np.size(x)  # Number of data points
    m_x, m_y = np.mean(x), np.mean(y)  # Mean of x and y
    # Cross-deviation and deviation about x
    SS_xy = np.sum(y * x) - n * m_y * m_x
    SS_xx = np.sum(x * x) - n * m_x * m_x
    # Regression coefficients
    b_1 = SS_xy / SS_xx
    b_0 = m_y - b_1 * m_x
    return (b_0, b_1)
# Function to predict new data points
def predict_new_values(x_new, b):
    return b[0] + b[1] * x_new  # Regression formula Y = b0 + b1*X
# Function to evaluate regression performance
def evaluate_regression(y_actual, y_predicted):
    mse = mean_squared_error(y_actual, y_predicted)
    r2 = r2_score(y_actual, y_predicted)
    return mse, r2
# Function to plot regression line, original data, and new predictions
def plot_regression_line(x, y, b, x_new=None, y_new=None):
    # Scatter plot for actual data
    plt.scatter(x, y, color="m", marker="o", s=30, label="Actual data")
    # Extend regression line to cover new X values
    x_extended = np.append(x, x_new) if x_new is not None else x
    y_pred_extended = b[0] + b[1] * x_extended
    plt.plot(x_extended, y_pred_extended, color="g", linestyle="--", label="Regression line")
    # Plot predicted new data points if provided
    if x_new is not None and y_new is not None:
        plt.scatter(x_new, y_new, color="r", marker="x", s=100, label="Predicted points")
    # Labels, legend, and title
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Linear Regression')
    plt.legend()
    # Show plot
    plt.show()
# Main function
def main():
    # Training data
    x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    y = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12])
    # Estimate coefficients
    b = estimate_coef(x, y)
    print(f"Regression Coefficients: b_0 = {b[0]:.2f}, b_1 = {b[1]:.2f}")
    # Predicting values for new data points
    x_new = np.array([10, 11, 12])  # New X values
    y_new = predict_new_values(x_new, b)
    # Printing predicted values
    print("Predicted values for new X points:")
    for i in range(len(x_new)):
        print(f"X = {x_new[i]}, Predicted Y = {y_new[i]:.2f}")
    # Compute predicted values for original dataset (for evaluation)
    y_pred_original = predict_new_values(x, b)
    # Evaluate regression performance
    mse, r2 = evaluate_regression(y, y_pred_original)
    print(f"Mean Squared Error (MSE): {mse:.2f}")
    print(f"R-squared Value (R2): {r2:.2f}")
    # Plot regression line with actual data and predicted new points
    plot_regression_line(x, y, b, x_new, y_new)
# Running the script
if __name__ == "__main__":
    main()