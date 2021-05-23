import numpy as np

# Using axis of numpy

x = np.ones([10, 20])  # Creates an array having 10 rows and 20 columns, initialised with value 1

print(np.sum(x, axis=0))  # Takes the sum of x along the rows and prints

print('\n')  # Prints a new line on terminal

print(np.sum(x, axis=1))  # Takes the sum of x along the columns and prints

print('\n')  # Prints a new line on terminal
