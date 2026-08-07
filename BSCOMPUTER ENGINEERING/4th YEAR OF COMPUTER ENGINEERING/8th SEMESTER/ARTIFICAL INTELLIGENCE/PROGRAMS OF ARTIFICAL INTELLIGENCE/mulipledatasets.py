import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris, load_wine, load_breast_cancer, fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix
from sklearn.metrics import classification_report
# Set random seed for reproducibility
np.random.seed(42)
# Function to load and preprocess classification datasets
def load_classification_dataset(dataset_name):
    if dataset_name == 'iris':
        data = load_iris()
        X = pd.DataFrame(data.data, columns=data.feature_names)
        y = pd.Series(data.target, name='target')
        class_names = data.target_names
    elif dataset_name == 'wine':
        data = load_wine()
        X = pd.DataFrame(data.data, columns=data.feature_names)
        y = pd.Series(data.target, name='target')
        class_names = data.target_names
    elif dataset_name == 'breast_cancer':
        data = load_breast_cancer()
        X = pd.DataFrame(data.data, columns=data.feature_names)
        y = pd.Series(data.target, name='target')
        class_names = data.target_names
    return X, y, class_names
# Function to evaluate classifiers and collect metrics
def evaluate_classifier(X, y, class_names, dataset_name):
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    # Standardize features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    # Initialize models
    models = {
        'Logistic Regression': LogisticRegression(max_iter=1000, random_state=42),
        'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42)
    }
    results = {}
    # Train and evaluate each model
    for name, model in models.items():
        model.fit(X_train_scaled, y_train)
        y_pred = model.predict(X_test_scaled)
        # For multi-class, use 'macro' averaging
        avg_method = 'macro' if len(class_names) > 2 else 'binary'
        # Calculate metrics
        metrics = {
            'accuracy': accuracy_score(y_test, y_pred),
            'precision': precision_score(y_test, y_pred, average=avg_method),
            'recall': recall_score(y_test, y_pred, average=avg_method),
            'f1': f1_score(y_test, y_pred, average=avg_method)
        }
        # Add ROC AUC for binary classification
        if len(class_names) == 2:
            y_prob = model.predict_proba(X_test_scaled)[:, 1]
            metrics['roc_auc'] = roc_auc_score(y_test, y_prob)
        # Add confusion matrix
        metrics['confusion_matrix'] = confusion_matrix(y_test, y_pred)
        # Add classification report
        metrics['classification_report'] = classification_report(y_test, y_pred, target_names=class_names)
        results[name] = metrics
    return results
# Main execution
def main():
    # List of datasets to analyze
    datasets = ['iris', 'wine', 'breast_cancer']
    all_results = {}
    # Process each dataset
    for dataset_name in datasets:
        print(f"\n{'='*50}")
        print(f"Dataset: {dataset_name.upper()}")
        print(f"{'='*50}")
        # Load and prepare data
        X, y, class_names = load_classification_dataset(dataset_name)
        # Display data info
        print(f"\nData shape: {X.shape}")
        print(f"Number of classes: {len(class_names)}")
        print(f"Class names: {class_names}")
        print(f"Class distribution: {np.bincount(y)}")
        # Display data head
        print("\nFeatures (first 5 rows):")
        print(X.head())
        print("\nLabels (first 5 values):")
        print(y.head())
        # Train and evaluate models
        results = evaluate_classifier(X, y, class_names, dataset_name)
        all_results[dataset_name] = results
        # Print results
        for model_name, metrics in results.items():
            print(f"\nModel: {model_name}")
            print(f"Accuracy: {metrics['accuracy']:.4f}")
            print(f"Precision: {metrics['precision']:.4f}")
            print(f"Recall: {metrics['recall']:.4f}")
            print(f"F1 Score: {metrics['f1']:.4f}")
            if 'roc_auc' in metrics:
                print(f"ROC AUC: {metrics['roc_auc']:.4f}")
            print("\nConfusion Matrix:")
            print(metrics['confusion_matrix'])
            print("\nClassification Report:")
            print(metrics['classification_report'])
    # Visualize results
    plot_comparison(all_results)
# Function to create comparison plots
def plot_comparison(all_results):
    metrics_to_plot = ['accuracy', 'precision', 'recall', 'f1']
    datasets = list(all_results.keys())
    models = list(all_results[datasets[0]].keys())
    # Create a figure with subplots
    fig, axes = plt.subplots(len(metrics_to_plot), 1, figsize=(12, 16))
    # Set spacing between subplots
    plt.subplots_adjust(hspace=0.4)
    # Plot each metric
    for i, metric in enumerate(metrics_to_plot):
        ax = axes[i]
        # Prepare data for plotting
        x = np.arange(len(datasets))
        width = 0.35
        # Plot bars for each model
        for j, model in enumerate(models):
            values = [all_results[dataset][model][metric] for dataset in datasets]
            ax.bar(x + j*width, values, width, label=model)
        # Customize the plot
        ax.set_title(f'{metric.capitalize()} Comparison')
        ax.set_xlabel('Dataset')
        ax.set_ylabel(metric.capitalize())
        ax.set_xticks(x + width/2)
        ax.set_xticklabels(datasets)
        ax.legend()
        # Add values on top of bars
        for j, model in enumerate(models):
            values = [all_results[dataset][model][metric] for dataset in datasets]
            for k, v in enumerate(values):
                ax.text(x[k] + j*width, v + 0.01, f'{v:.3f}', ha='center', va='bottom', fontsize=8)
    plt.suptitle('Performance Metrics Comparison Across Datasets', fontsize=16)
    plt.tight_layout(rect=[0, 0, 1, 0.97])
    plt.show()
# Run the program
if __name__ == "__main__":
    main()