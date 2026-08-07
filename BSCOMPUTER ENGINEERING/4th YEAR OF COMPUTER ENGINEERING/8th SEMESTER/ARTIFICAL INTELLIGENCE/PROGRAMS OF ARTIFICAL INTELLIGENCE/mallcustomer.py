import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random as rd
from sklearn.preprocessing import StandardScaler

# Load the dataset
dataset = pd.read_csv('Mall_Customers.csv')

# Select the relevant columns (Annual Income, Spending Score, and Age)
X = dataset.iloc[:, [3, 4, 2]].values

# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Number of training examples and features
m, n = X_scaled.shape

# Number of iterations
n_iter = 100

# Number of clusters
K = 5

# Randomly initialize centroids
def initialize_centroids(X, K):
    m, n = X.shape
    Centroids = np.zeros((n, K))
    for k in range(K):
        # Randomly select K unique data points as initial centroids
        centroid_idx = rd.randint(0, m-1)
        Centroids[:, k] = X[centroid_idx]
    return Centroids

# K-means clustering algorithm
def kmeans_clustering(X, K, n_iter):
    # Randomly initialize centroids
    Centroids = initialize_centroids(X, K)
    
    for _ in range(n_iter):
        # Calculate Euclidean distances
        EuclideanDistance = np.zeros((m, K))
        for k in range(K):
            EuclideanDistance[:, k] = np.sum((X - Centroids[:, k]) ** 2, axis=1)
        
        # Assign points to nearest centroid
        C = np.argmin(EuclideanDistance, axis=1)
        
        # Update centroids
        for k in range(K):
            Centroids[:, k] = np.mean(X[C == k], axis=0)
    
    return C, Centroids

# Perform clustering
C, Centroids = kmeans_clustering(X_scaled, K, n_iter)

# Visualize the clustered data
plt.figure(figsize=(15, 5))

# Color palette for clusters
colors = ['red', 'blue', 'green', 'cyan', 'magenta']
labels = [f'Cluster {i+1}' for i in range(K)]

# Plot 1: Income vs Spending Score
plt.subplot(131)
for k in range(K):
    cluster_points = X[C == k]
    plt.scatter(cluster_points[:, 0], cluster_points[:, 1], 
                c=colors[k], label=labels[k], alpha=0.7)
plt.scatter(Centroids[0, :], Centroids[1, :], 
            c='yellow', marker='x', s=200, linewidths=3)
plt.xlabel('Annual Income')
plt.ylabel('Spending Score')
plt.title('Clustering: Income vs Spending')
plt.legend()

# Plot 2: Income vs Age
plt.subplot(132)
for k in range(K):
    cluster_points = X[C == k]
    plt.scatter(cluster_points[:, 0], cluster_points[:, 2], 
                c=colors[k], label=labels[k], alpha=0.7)
plt.scatter(Centroids[0, :], Centroids[2, :], 
            c='yellow', marker='x', s=200, linewidths=3)
plt.xlabel('Annual Income')
plt.ylabel('Age')
plt.title('Clustering: Income vs Age')
plt.legend()

# Plot 3: Age vs Spending Score
plt.subplot(133)
for k in range(K):
    cluster_points = X[C == k]
    plt.scatter(cluster_points[:, 2], cluster_points[:, 1], 
                c=colors[k], label=labels[k], alpha=0.7)
plt.scatter(Centroids[2, :], Centroids[1, :], 
            c='yellow', marker='x', s=200, linewidths=3)
plt.xlabel('Age')
plt.ylabel('Spending Score')
plt.title('Clustering: Age vs Spending')
plt.legend()

plt.tight_layout()
plt.show()

# Elbow Method
wcss = []
for k in range(1, 11):
    # Perform K-means clustering
    kmeans = kmeans_clustering(X_scaled, k, n_iter)[0]
    
    # Calculate Within Cluster Sum of Squares (WCSS)
    wcss_k = 0
    for i in range(k):
        cluster_points = X_scaled[kmeans == i]
        wcss_k += np.sum((cluster_points - np.mean(cluster_points, axis=0)) ** 2)
    wcss.append(wcss_k)

# Plot Elbow Method
plt.plot(range(1, 11), wcss, marker='o')
plt.title('Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()

# Cluster Analysis
print("Cluster Analysis:")
for k in range(K):
    cluster_points = X[C == k]
    print(f"\nCluster {k+1}:")
    print(f"Number of Customers: {len(cluster_points)}")
    print(f"Average Annual Income: {cluster_points[:, 0].mean():.2f}")
    print(f"Average Spending Score: {cluster_points[:, 1].mean():.2f}")
    print(f"Average Age: {cluster_points[:, 2].mean():.2f}")