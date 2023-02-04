import pandas as pd

# Load the data sources
df1 = pd.read_csv("data_source_1.csv")
df2 = pd.read_csv("data_source_2.csv")

# Specify the fields to match
match_fields = ["Name", "Address", "Phone Number"]

# Perform the exact match
exact_matches = pd.merge(df1, df2, on=match_fields, how='inner')

# Print the results
print(exact_matches)
