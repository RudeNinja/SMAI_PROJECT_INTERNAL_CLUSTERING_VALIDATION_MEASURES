import numpy as np 
def Kmeans(X, k, max_iter=10):
    # X is a 2D array of shape (n_samples, n_features)
    # k is the number of clusters
    # max_iter is the maximum number of iterations
    # returns a 1D array of shape (n_samples,) containing the cluster labels
    n_samples, n_features = X.shape
    # Initialize the centroids
    centroids = X[np.random.choice(n_samples, k, replace=False), :]
    old_centroids = centroids.copy()
    for _ in range(max_iter):
        # Compute the distance between each sample and each centroid
        distances = np.zeros((n_samples, k))
        for i in range(k):
            distances[:, i] = np.linalg.norm(X - centroids[i], axis=1)
        # Assign each sample to the closest centroid
        labels = np.argmin(distances, axis=1)
        # Update the centroids
        for i in range(k):
            centroids[i] = np.mean(X[labels == i], axis=0)
        # Check for convergence
        if np.all(centroids == old_centroids):
            break
        old_centroids = centroids.copy()
    return centroids,labels;
