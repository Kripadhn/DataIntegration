import pandas as pd

# create a sample dataframe with missing values
df = pd.DataFrame({'A': [1, 2, np.nan, 4],
                   'B': [5, np.nan, 7, 8],
                   'C': [9, 10, 11, 12]})

# Impute missing values with the mean of the column
df.fillna(df.mean(), inplace=True)

print(df)
