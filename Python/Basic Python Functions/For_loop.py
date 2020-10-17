# A program to display use of for loops, sys.argv, if else

import sys

# len(sys.argv) gives a length of the number of arguments passed after python in the command prompt
# Eg. if you ran the code as "python For_loop.py Hello"
# len(sys.argv) will be equal to 2(['For_loop.py', 'Hello'])



if len(sys.argv) != 1:
	# If multiple arguments are passed while running the program then these statements are executed
	# In python the for loop is different than what it was in c++.
	# The range function generates numbers from 0 to len(sys.argv) - 1
	# So i takes the values from 0 to len(sys.argv) - 1

	for i in range(len(sys.argv)):
		print(sys.argv[i], i)

else:
	# If only one argument is passed then these lines get executed

	for i in range(10):
		print(i)