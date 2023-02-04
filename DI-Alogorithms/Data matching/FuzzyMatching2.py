from fuzzywuzzy import fuzz

# Load the two data sets into lists
list1 = ['John Doe', '123 Main St', 'johndoe@email.com']
list2 = ['John D', '123 Main St', 'johndoe@email.com']

# Define the attributes to compare
attributes = [0, 1, 2]

# Perform the fuzzy matching
matches = []
for i in range(len(list1)):
    if fuzz.token_sort_ratio(list1[i], list2[i]) > 70:
        matches.append(i)
