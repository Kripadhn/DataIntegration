import pandas as pd

# Load the two data sets into pandas data frames
df1 = pd.read_csv('dataset1.csv')
df2 = pd.read_csv('dataset2.csv')

# Define the attributes to compare
attributes = ['name', 'address', 'email']

# Perform the exact matching
matches = df1[attributes].merge(df2[attributes], how='inner', on=attributes)
