import pandas as pd

# Load data from multiple sources
data1 = pd.read_csv("source1.csv")
data2 = pd.read_csv("source2.csv")
data3 = pd.read_csv("source3.csv")

# Merge data into a single DataFrame
consolidated_data = pd.concat([data1, data2, data3], axis=0)

# Remove duplicates based on a key column
consolidated_data = consolidated_data.drop_duplicates(subset='id')

# Save consolidated data to a file
consolidated_data.to_csv("consolidated_data.csv", index=False)
