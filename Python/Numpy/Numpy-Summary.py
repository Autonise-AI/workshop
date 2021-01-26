import numpy as np

# Constant Value Initialization

x = np.zeros([100, 100])  # Initialize a 2-D array of zeros of dtype - np.float64
x = np.zeros_like(x)  # Initialize a 2-D array with zeros having dtype and shape similar to given array
x = np.ones([100, 100])  # Initialize a 2-D array of ones of dtype - np.float64
x = np.ones_like(x)  # Initialize a 2-D array with ones having dtype and shape similar to given array

# Increasing Value Iterator Generation
x = np.arange(10, 100, 5)  # Initialize a iterator which generates values starting from 10 till 10 with a step size of 5

# Random Distribution sampling
x = np.random.uniform(low=0, high=1, size=(100, 100))  # Generate random numbers from the uniform distribution
x = np.random.randn(100, 100)  # Generate random numbers from the normal gaussian distribution
x = np.random.normal(loc=0, scale=1, size=(100, 100))  # Generate random numbers from the gaussian distribution


aranged_100 = np.arange(0, 100, 1).reshape([10, 10])
"""
[[ 0  1  2  3  4  5  6  7  8  9]
 [10 11 12 13 14 15 16 17 18 19]
 [20 21 22 23 24 25 26 27 28 29]
 [30 31 32 33 34 35 36 37 38 39]
 [40 41 42 43 44 45 46 47 48 49]
 [50 51 52 53 54 55 56 57 58 59]
 [60 61 62 63 64 65 66 67 68 69]
 [70 71 72 73 74 75 76 77 78 79]
 [80 81 82 83 84 85 86 87 88 89]
 [90 91 92 93 94 95 96 97 98 99]]
"""


cropped_sliced = aranged_100[5:10, 0:5]
"""
[[50 51 52 53 54]
 [60 61 62 63 64]
 [70 71 72 73 74]
 [80 81 82 83 84]
 [90 91 92 93 94]]
"""

# print(cropped_sliced + 10)

"""
[[ 60  61  62  63  64]
 [ 70  71  72  73  74]
 [ 80  81  82  83  84]
 [ 90  91  92  93  94]
 [100 101 102 103 104]]
"""

x = np.zeros([5, 5])
x[np.arange(5), np.arange(5)] = 1
print(x)

"""
[[1. 0. 0. 0. 0.]
 [0. 1. 0. 0. 0.]
 [0. 0. 1. 0. 0.]
 [0. 0. 0. 1. 0.]
 [0. 0. 0. 0. 1.]]
"""
