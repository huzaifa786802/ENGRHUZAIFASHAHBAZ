import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
# Function to perform Polynomial Regression
def polynomial_regression(x, y, degree):
    # Reshaping x to a 2D array if it's not already
    if len(x.shape) == 1:
        x = x.reshape(-1, 1)
    # Transforming x into polynomial features
    poly = PolynomialFeatures(degree=degree)
    x_poly = poly.fit_transform(x)
    # Fitting the transformed features into Linear Regression model
    model = LinearRegression()
    model.fit(x_poly, y)
    # Predicting values
    y_pred = model.predict(x_poly)
    # Model Evaluation
    mse = mean_squared_error(y, y_pred)
    r2 = r2_score(y, y_pred)
    return model, poly, mse, r2, y_pred
# Function to plot Polynomial Regression curve
def plot_polynomial_regression(x, y, model, poly, degree, y_pred=None):
    # Create a new figure
    plt.figure(figsize=(10, 6))
    # Scatter plot of original data
    plt.scatter(x, y, color='red', marker='o', label="Actual data")
    # Optionally plot the predicted points
    if y_pred is not None:
        plt.scatter(x, y_pred, color='green', marker='x', label="Predicted points")
    # Generating smooth curve for polynomial regression
    x_smooth = np.linspace(min(x), max(x), 100).reshape(-1, 1)
    y_smooth = model.predict(poly.transform(x_smooth))
    # Plot the regression curve
    plt.plot(x_smooth, y_smooth, color='blue', linestyle='--', label=f'Polynomial Regression (degree={degree})')
    # Labels and legend
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title(f'Polynomial Regression (Degree {degree})')
    plt.legend()
    plt.grid(True, alpha=0.3)
    return plt
# Function to evaluate models with different polynomial degrees
def evaluate_polynomial_degrees(x, y, max_degree=5):
    results = []
    for degree in range(1, max_degree + 1):
        model, poly, mse, r2, y_pred = polynomial_regression(x, y, degree)
        results.append({
            'degree': degree,
            'model': model,
            'poly': poly,
            'mse': mse,
            'r2': r2,
            'y_pred': y_pred
        })
    return results
# Main function
def main():
    # Training Data
    x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])  # X values
    y = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12])  # Corresponding Y values
    # Optional: Split data into training and testing sets
    # x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
    # Try different polynomial degrees
    results = evaluate_polynomial_degrees(x, y, max_degree=4)
    # Print Results for each degree
    for result in results:
        degree = result['degree']
        mse = result['mse']
        r2 = result['r2']
        print(f"\nPolynomial Regression (Degree {degree})")
        print(f"Mean Squared Error (MSE): {mse:.4f}")
        print(f"R-squared Value (R²): {r2:.4f}")
    # Plot the regression curve for the best model (based on R²)
    best_model = max(results, key=lambda x: x['r2'])
    best_degree = best_model['degree']
    print(f"\nBest model: Polynomial Regression (Degree {best_degree})")
    plt = plot_polynomial_regression(
        x, y, 
        best_model['model'], 
        best_model['poly'], 
        best_degree,
        best_model['y_pred']
    )
    # Display coefficient values for the best model
    model = best_model['model']
    print(f"\nIntercept: {model.intercept_:.4f}")
    print("Coefficients:", end=" ")
    for i, coef in enumerate(model.coef_):
        if i > 0:  # Skip the intercept term that PolynomialFeatures adds
            print(f"{coef:.4f}", end=" ")
    print()
    plt.show()
# Running the script
if __name__ == "__main__":
    main()