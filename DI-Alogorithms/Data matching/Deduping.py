import pandas as pd

# Load the data set into a pandas data frame
df = pd.read_csv('dataset.csv')

# Define the attributes to compare
attributes = ['name', 'address', 'email']

# Perform the deduping
deduped = df.drop_duplicates(subset=attributes)
