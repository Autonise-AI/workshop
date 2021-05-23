import numpy as np

# Iterate over the entire numpy array 

x = np.arange(100).reshape([10, 10])  # Generate an array having numbers from 0 to 99([0, 1, ... 99])
# and reshape into size ([10, 10])

print(x)  # Prints x

print('\n')  # Prints a new line on terminal

x[x < 50] = 0  # Converts all elements of x which is less than 50 into 0

print(x)  # Prints x

print('\n')  # Prints a new line on terminal

x[x > 50] = 1  # Converts all elements of x which are greater than 50 to 1

print(x)  # Prints x

print('\n')  # Prints a new line on terminal

# Overwriting x

x = [i for i in range(20) if i % 2 == 0]  # x is now a list which has even numbers
# Can read this statement as x is a list of i's such that i belongs to 0 to 20 and remainder of i with 2 = 0

print(x)  # Prints x

print('\n')  # Prints a new line on terminal
