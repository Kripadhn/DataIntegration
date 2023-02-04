import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Generating sample data
np.random.seed(0)
X = np.random.rand(100,2)

# Creating the KMeans model
kmeans = KMeans(n_clusters=3)
kmeans.fit(X)

# Getting the cluster labels
labels = kmeans.labels_

# Plotting the clusters
plt.scatter(X[:,0], X[:,1], c=labels)
plt.show()



# This code generates 100 random 2-dimensional points and fits them to a KMeans model with 3 clusters. 
# The labels_ attribute of 
# the model gives the cluster labels for each point and it's used to plot the points with different colors for each cluster.