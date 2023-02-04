from fuzzywuzzy import fuzz

# Load the data sources
df1 = pd.read_csv("data_source_1.csv")
df2 = pd.read_csv("data_source_2.csv")

# Specify the fields to match
match_fields = ["Name", "Address", "Phone Number"]

# Define a function to perform the fuzzy match
def fuzzy_match(row1, row2):
    score = 0
    for field in match_fields:
        score += fuzz.token_sort_ratio(row1[field], row2[field])
    return score / len(match_fields)

# Perform the fuzzy match
fuzzy_matches = []
for i, row1 in df1.iterrows():
    best_match = None
    best_score = 0
    for j, row2 in df2.iterrows():
        score = fuzzy_match(row1, row2)
        if score > best_score:
            best_match = row2
            best_score = score
    if best_score > 0.8:
        fuzzy_matches.append((row1, best_match))

# Print the results
for match in fuzzy_matches:
    print(match)
