import numpy as np

x =np.zeros([10, 10]) # An array of zeros having 10 rows and 10 columns

x[:, 0] = 1 # All rows and 0th column should become 1. : means All
print(x) # prints the value of x

print('\n') # Prints a new line on terminal

x[:, 2:5] = 2 # All rows and columns 2 to 5 should become 2, here 2:5 means 2 to 5
print(x) # prints x

print('\n') # Prints a new line on terminal

x[2, :] = 10 # row 2 and all columns should become 10
print(x)

print('\n') # Prints a new line on terminal

x = np.zeros([10, 10]) # reinitialises x with zeros

x[4:6, 3:5] = 1 # Rows 4 to 6 and columns 3 to 5 should become 1

print(x) # prints x

print('\n') # Prints a new line on terminal