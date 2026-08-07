import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
# Function to train Support Vector Regression model
def train_svr(x, y, kernel_type='rbf', C=1.0, epsilon=0.1):
    # Reshape x for SVR (SVR expects a 2D array)
    x = x.reshape(-1, 1)
    # Standardize the dataset
    scaler = StandardScaler()
    x_scaled = scaler.fit_transform(x)
    # Train SVR model
    svr_model = SVR(kernel=kernel_type, C=C, epsilon=epsilon)
    svr_model.fit(x_scaled, y)
    return svr_model, scaler
# Function to predict values using trained SVR model
def predict_svr(model, scaler, x_new):
    x_new = x_new.reshape(-1, 1)  # Reshape input for SVR
    x_new_scaled = scaler.transform(x_new)  # Standardize new inputs
    return model.predict(x_new_scaled)
# Function to evaluate SVR model
def evaluate_regression(y_actual, y_predicted):
    mse = mean_squared_error(y_actual, y_predicted)
    r2 = r2_score(y_actual, y_predicted)
    return mse, r2
# Function to plot SVR regression results
def plot_svr(x, y, model, scaler, x_new=None, y_new=None):
    plt.scatter(x, y, color="m", marker="o", label="Actual data")
    # Generate smooth curve for SVR prediction
    x_range = np.linspace(x.min(), x.max(), 100).reshape(-1, 1)
    x_range_scaled = scaler.transform(x_range)
    y_svr = model.predict(x_range_scaled)
    plt.plot(x_range, y_svr, color="g", linestyle="--", label="SVR Prediction")
    # Plot predicted new points
    if x_new is not None and y_new is not None:
        plt.scatter(x_new, y_new, color="r", marker="x", s=100, label="Predicted Points")
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Support Vector Regression')
    plt.legend()
    plt.show()
# Main function
def main():
    # Training Data
    x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    y = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12])
    # Train SVR Model
    svr_model, scaler = train_svr(x, y, kernel_type='rbf', C=100, epsilon=0.1)
    # Predict new values
    x_new = np.array([10, 11, 12])
    y_new = predict_svr(svr_model, scaler, x_new)
    # Print predicted values
    print("Predicted values for new X points:")
    for i in range(len(x_new)):
        print(f"X = {x_new[i]}, Predicted Y = {y_new[i]:.2f}")
    # Compute predictions for evaluation
    y_pred_original = predict_svr(svr_model, scaler, x)
    # Evaluate SVR Model
    mse, r2 = evaluate_regression(y, y_pred_original)
    print(f"Mean Squared Error (MSE): {mse:.2f}")
    print(f"R-squared Value (R2): {r2:.2f}")
    # Plot results
    plot_svr(x, y, svr_model, scaler, x_new, y_new)
# Run the script
if __name__ == "__main__":
    main()