import numpy as np

# Basics of numpy

x = np.zeros([10, 10])  # Creates an array of size 10 initialised with the value 0

y = np.ones([10])  # Creates an array of size 10 initialised with the value 1

z = [1, 2, 3, 4, 5.1]  # A list

z = np.array(z)  # Converts the list z into an array

print(x)  # Prints x

print('\n')  # Prints a new line on terminal

print(y)  # Prints y

print('\n')  # Prints a new line on terminal

print(z.astype(np.int32))  # Converts the type of z from float(fraction) to integers

print('\n')  # Prints a new line on terminal

print(x + 4)  # Adds 4 to every element of x

print('\n')  # Prints a new line on terminal

print(y * 5)  # Multiplies 5 to every element of y

print('\n')  # Prints a new line on terminal

print(x + y + 2)  # Does element wise addition of x and y and 2

print('\n')  # Prints a new line on terminal

print((x + 3) * y)  # Adds 3 to every element of x and then does element wise multiplication with y

print('\n')  # Prints a new line on terminal

# Element wise means if we have 

# x = [1, 2, 3, 4, 5]
# y = [2, 3, 4, 6, 7]

# x + y (element wise sum) = [1+2, 2+3, 3+4, 4+6, 5+7] = [3, 5, 7, 10, 12]
