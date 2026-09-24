from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Sample data
X = [
    [1, 2],
    [1, 3],
    [2, 2],
    [2, 3],
    [8, 7],
    [8, 8],
    [9, 7],
    [9, 8]
]

# Create K-Means model
kmeans = KMeans(n_clusters=2, random_state=42, n_init=10)

# Train the model
kmeans.fit(X)

# Get cluster labels
labels = kmeans.labels_

# Get cluster centers
centers = kmeans.cluster_centers_

# Display cluster labels
print("Cluster labels:")
print(labels)

# Display cluster centers
print("\nCluster centers:")
print(centers)

# Display graph
plt.scatter(
    [x[0] for x in X],
    [x[1] for x in X],
    c=labels
)

# Plot cluster centers
plt.scatter(
    centers[:, 0],
    centers[:, 1],
    marker="X",
    s=200
)

plt.xlabel("X")
plt.ylabel("Y")
plt.title("K-Means Clustering")
plt.show()