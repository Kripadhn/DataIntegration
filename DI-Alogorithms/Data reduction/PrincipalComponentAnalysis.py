from sklearn.decomposition import PCA
import pandas as pd

# Load the data
data = pd.read_csv("data.csv")

# Perform PCA
pca = PCA(n_components=2)
pca.fit(data)

# Project data onto the new, reduced feature space
reduced_data = pca.transform(data)
