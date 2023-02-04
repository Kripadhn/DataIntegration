import numpy as np
from sklearn.preprocessing import StandardScaler

# Load the data set into a numpy array
data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Define the normalization algorithm
scaler = StandardScaler()

# Perform the normalization
normalized_data = scaler.fit_transform(data)
