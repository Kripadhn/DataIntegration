import pandas as pd

# Load the data into a pandas DataFrame
df = pd.read_csv("data.csv")

# Normalize the values in a column to the range 0 to 1
df["column_name"] = (df["column_name"] - df["column_name"].min()) / (df["column_name"].max() - df["column_name"].min())

# Save the normalized data back to a CSV file
df.to_csv("normalized_data.csv", index=False)
