# This code generates a synthetic dataset with a spiral-like distribution and applies K-Means clustering.  
# It then evaluates the effect of different K-Means parameters (n_init and max_iter) on clustering results.

# Importing required libraries
import numpy as np
from numpy import pi
import matplotlib.pyplot as plt # type: ignore
from sklearn.cluster import KMeans

# ---------------- Generate Spiral Dataset ----------------
N = 400
theta = np.sqrt(np.random.rand(N)) * 2 * pi  

# Creating first spiral (Cluster A)
r_a = 2 * theta + pi
data_a = np.array([np.cos(theta) * r_a, np.sin(theta) * r_a]).T
x_a = data_a + np.random.randn(N, 2)  

# Creating second spiral (Cluster B)
r_b = -2 * theta - pi
data_b = np.array([np.cos(theta) * r_b, np.sin(theta) * r_b]).T
x_b = data_b + np.random.randn(N, 2)  # Adding noise

# Merging both clusters
res_a = np.append(x_a, np.zeros((N, 1)), axis=1)  
res_b = np.append(x_b, np.ones((N, 1)), axis=1)  
res = np.append(res_a, res_b, axis=0)

# Shuffling the dataset
np.random.shuffle(res)

# Saving dataset to CSV file
np.savetxt("result.csv", res, delimiter=",", header="x,y,label", comments="", fmt='%.5f')

# ---------------- Visualizing Original Data ----------------
x = np.concatenate((x_a, x_b), axis=0)

plt.figure(figsize=(6, 6))
plt.scatter(x_a[:, 0], x_a[:, 1], label="Cluster A", alpha=0.5)
plt.scatter(x_b[:, 0], x_b[:, 1], label="Cluster B", alpha=0.5)
plt.title("Original Dataset")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.show()

# ---------------- K-Means Clustering (2 Clusters) ----------------
kmeans = KMeans(n_clusters=2, random_state=0)
y_kmeans = kmeans.fit_predict(x)

# Plot Clustering Results
plt.figure(figsize=(6, 6))
plt.scatter(x[:, 0], x[:, 1], c=y_kmeans, s=50, cmap='viridis', alpha=0.7)
centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='red', s=200, alpha=0.5, label="Centroids")
plt.title("K-Means Clustering (2 Clusters)")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.show()

# ---------------- K-Means Clustering with Parameters ----------------
kmeans = KMeans(n_clusters=2, n_init=10, max_iter=200, random_state=0)
y_kmeans = kmeans.fit_predict(x)

# Plot Clustering Results
plt.figure(figsize=(6, 6))
plt.scatter(x[:, 0], x[:, 1], c=y_kmeans, s=50, cmap='viridis', alpha=0.7)
centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='red', s=200, alpha=0.5, label="Centroids")
plt.title("K-Means Clustering with n_init=10, max_iter=200")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.show()