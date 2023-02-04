import numpy as np
import skfuzzy as fuzz

# Define the input variables
x = np.arange(0, 11, 1)
y = np.arange(0, 11, 1)

# Define the membership functions for the variables
x_mf = fuzz.trimf(x, [0, 5, 10])
y_mf = fuzz.trimf(y, [0, 5, 10])

# Perform the fuzzy integration
fuzzy_result = np.fmin(x_mf, y_mf)

# Defuzzification to get the crisp value
defuzz_result = np.mean(x[fuzzy_result == np.max(fuzzy_result)])

print("Fuzzy Result: ", fuzzy_result)
print("Defuzzified Result: ", defuzz_result)
