import pandas as pd

# Load the data set into a pandas data frame
df = pd.read_csv('dataset.csv')

# Convert the categorical variable 'color' into numerical variables
df = pd.get_dummies(df, columns=['color'])
