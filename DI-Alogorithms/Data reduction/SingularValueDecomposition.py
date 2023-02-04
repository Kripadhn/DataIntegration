import numpy as np

# Load the data
data = np.loadtxt("data.csv", delimiter=",")

# Perform SVD
U, s, VT = np.linalg.svd(data)

# Reduce the number of features
k = 2
S = np.zeros((k, k))
S[:k, :k] = np.diag(s[:k])
reduced_data = U[:, :k].dot(S[:k, :k])
