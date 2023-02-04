import pandas as pd

# Load the data into a pandas DataFrame
df = pd.read_csv("data.csv")

# Add a new column "City" based on the postal code
df['City'] = df['Postal Code'].apply(lambda x: 'London' if x.startswith('L') else 'New York')

# Add a new column "Population" based on the city
df['Population'] = df.apply(lambda x: 8000000 if x['City'] == 'London' else 20000000, axis=1)

# Print the enriched data
print(df.head())


# This code uses the pandas library to load a CSV file into a DataFrame and add two new columns, "City" and "Population". 
# The "City" column is added based on the value of the "Postal Code" column, and the "Population" column is added based on 
# the value of the "City" column. The final 
# result is a DataFrame with additional information about the location and population of each row in the original data set.