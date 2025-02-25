# This code performs K-Means clustering on a synthetic dataset and visualizes the results for 2 and 4 clusters.  
# It also applies the Elbow Method to determine the optimal number of clusters based on inertia values.

# Importing necessary libraries
import matplotlib.pyplot as plt # type: ignore
import seaborn as sns # type: ignore
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

# Set Seaborn style
sns.set()

# Generating synthetic dataset with 4 cluster centers
x, y = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)

# Plot original data points
plt.figure(figsize=(6, 4))
plt.scatter(x[:, 0], x[:, 1], s=50, color='gray')
plt.title("Original Data Distribution")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.show()

# -------------- Clustering with 2 clusters --------------
kmeans_2 = KMeans(n_clusters=2, random_state=0)
y_kmeans_2 = kmeans_2.fit_predict(x)

# Plotting the clusters
plt.figure(figsize=(6, 4))
plt.scatter(x[:, 0], x[:, 1], c=y_kmeans_2, cmap='viridis', s=50)
plt.scatter(kmeans_2.cluster_centers_[:, 0], kmeans_2.cluster_centers_[:, 1], 
            c='red', s=200, alpha=0.5, label='Centroids')
plt.title("Clustering with 2 Clusters")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.legend()
plt.show()

# -------------- Clustering with 4 clusters --------------
kmeans_4 = KMeans(n_clusters=4, random_state=0)
y_kmeans_4 = kmeans_4.fit_predict(x)

# Plotting the clusters
plt.figure(figsize=(6, 4))
plt.scatter(x[:, 0], x[:, 1], c=y_kmeans_4, cmap='viridis', s=50)
plt.scatter(kmeans_4.cluster_centers_[:, 0], kmeans_4.cluster_centers_[:, 1], 
            c='red', s=200, alpha=0.5, label='Centroids')
plt.title("Clustering with 4 Clusters")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.legend()
plt.show()

# -------------- Finding Optimal Number of Clusters using Elbow Method --------------
inertia_values = []
cluster_range = range(1, 11) 

for k in cluster_range:
    kmeans = KMeans(n_clusters=k, random_state=0)
    kmeans.fit(x)
    inertia_values.append(kmeans.inertia_)

# Plot the Elbow Curve
plt.figure(figsize=(6, 4))
plt.plot(cluster_range, inertia_values, marker='o', linestyle='--', color='blue')
plt.title("Elbow Method for Optimal K")
plt.xlabel("Number of Clusters (K)")
plt.ylabel("Inertia (Within-Cluster Sum of Squares)")
plt.xticks(cluster_range)
plt.grid()
plt.show()