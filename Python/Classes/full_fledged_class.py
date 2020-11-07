import numpy as np


class firstTime:

	def __init__(self, x=1, y=1):

		# This is the constructor and is invoked when the object is created

		self.x = x
		self.y = y
		self.z = [1, 2, 3, 4, 5, 6, 7, 8, 9]

	def __str__(self):

		#  when you run the command print(s), this is the function which is called

		return str(self.x)+' '+str(self.y)

	def __getitem__(self, index):
		# When s[0] is done then __getitem__ is called with index=0

		return self.z[index]

	def __len__(self):

		# When s[0] is done then __getitem__ is called with index=0

		return 1000

	def letsSum(self):

		# A function of the class

		return sum(self.z)


s = firstTime(x=10, y=10)

print(s)

for i in range(10):
	print(s[i])

print(s.letsSum())

print('Length of s: ', len(s), 'Same as: ', s.__len__())
