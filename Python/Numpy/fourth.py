import numpy as np

# Showing versability of numpy in subtraction

x = np.arange(100).reshape([10, 10])*10 # an array having 10 rows and 10 columns, each having the value 10

y = np.ones([10])*3 # an array having 10 rows and each having the value 3

print(x-y) # numpy subtracts 3 from every column value

# Show the variations(Column variation, Row Variation)