import numpy as np

x = np.random.randint(0, 200, size=100).reshape([20, 5]) # generates 100 random numbers from 0 to 200
# and reshapes them to 20 rows and 5 columns

print(x) # prints x

print('\n') # Prints a new line on terminal

y = np.ones([5, 10]) # creates array y having 5 rows 20 columns and initialised with the value 1

print(np.matmul(x, y)) # Does matrix multiplication of x, y

print('\n') # Prints a new line on terminal

print(np.matmul(x, y).shape) # Prints the shape(number of rows and columns) of the new array after matrix multiplication of x and y