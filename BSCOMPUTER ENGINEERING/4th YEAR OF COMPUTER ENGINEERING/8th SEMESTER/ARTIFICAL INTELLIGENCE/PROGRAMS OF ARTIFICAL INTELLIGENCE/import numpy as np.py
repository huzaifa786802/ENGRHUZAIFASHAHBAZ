import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random as rd
# Load the dataset
dataset = pd.read_csv('Mall_Customers.csv')
# Select the relevant columns (Annual Income and Spending Score)
X = dataset.iloc[:, [3, 4]].values
# Number of training examples and features
m = X.shape[0]  # Number of data points
n = X.shape[1]  # Number of features
# Number of iterations
n_iter = 100
# Number of clusters
K = 5
# Step 1: Randomly initialize the centroids
Centroids = np.array([]).reshape(n, 0)
for i in range(K):
    rand = rd.randint(0, m - 1)
    Centroids = np.c_[Centroids, X[rand]]
# Step 2: K-means clustering algorithm
for i in range(n_iter):
    # Step 2.a: Calculate the Euclidean distance for each point
    EuclidianDistance = np.array([]).reshape(m, 0)
    for k in range(K):
        tempDist = np.sum((X - Centroids[:, k]) ** 2, axis=1)
        EuclidianDistance = np.c_[EuclidianDistance, tempDist]
    # Assign each point to the nearest cluster
    C = np.argmin(EuclidianDistance, axis=1) + 1
    # Step 2.b: Group points into clusters and update centroids
    Y = {}
    for k in range(K):
        Y[k + 1] = np.array([]).reshape(2, 0)
    for i in range(m):
        Y[C[i]] = np.c_[Y[C[i]], X[i]]
    for k in range(K):
        Y[k + 1] = Y[k + 1].T
    for k in range(K):
        Centroids[:, k] = np.mean(Y[k + 1], axis=0)
Output = Y
# Visualize the unclustered data
plt.scatter(X[:, 0], X[:, 1], c='black', label='Unclustered Data')
plt.xlabel('Income')
plt.ylabel('Spending Score')
plt.legend()
plt.title('Plot of Data Points')
plt.show()
# Visualize the clustered data
color = ['red', 'blue', 'green', 'cyan', 'magenta']
labels = ['Cluster 1', 'Cluster 2', 'Cluster 3', 'Cluster 4', 'Cluster 5']
for k in range(K):
    plt.scatter(Output[k + 1][:, 0], Output[k + 1][:, 1], c=color[k], label=labels[k])
plt.scatter(Centroids[0, :], Centroids[1, :], s=300, c='yellow', label='Centroids')
plt.xlabel('Income')
plt.ylabel('Spending Score')
plt.legend()
plt.title('Clustered Data')
plt.show()
# Step 3: Determine the optimal number of clusters using the Elbow method
WCSS = []  # Within-Cluster Sum of Squares
for i in range(1, 11):  # Try clusters from 1 to 10
    K = i
    Centroids = np.array([]).reshape(n, 0)
    for i in range(K):
        rand = rd.randint(0, m - 1)
        Centroids = np.c_[Centroids, X[rand]]
    for i in range(n_iter):
        EuclidianDistance = np.array([]).reshape(m, 0)
        for k in range(K):
            tempDist = np.sum((X - Centroids[:, k]) ** 2, axis=1)
            EuclidianDistance = np.c_[EuclidianDistance, tempDist]
        C = np.argmin(EuclidianDistance, axis=1) + 1
        Y = {}
        for k in range(K):
            Y[k + 1] = np.array([]).reshape(2, 0)
        for i in range(m):
            Y[C[i]] = np.c_[Y[C[i]], X[i]]
        for k in range(K):
            Y[k + 1] = Y[k + 1].T
        for k in range(K):
            Centroids[:, k] = np.mean(Y[k + 1], axis=0)
    # Calculate WCSS (Within-Cluster Sum of Squares)
    WCSS.append(np.sum(np.min(EuclidianDistance, axis=1)))
# Plot the WCSS vs. number of clusters to find the "elbow"
plt.plot(range(1, 11), WCSS, marker='o')
plt.title('Elbow Method for Optimal K')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()