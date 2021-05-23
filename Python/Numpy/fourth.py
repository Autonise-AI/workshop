import numpy as np

# Showing versatility of numpy in subtraction

x = np.arange(100).reshape([10, 10])  # an array having 10 rows and 10 columns

y = np.ones([10])*3  # an array having 10 rows and each having the value 3

print(x-y)  # numpy subtracts 3 from every column value

# Show the variations(Column variation, Row Variation)
