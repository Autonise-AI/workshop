import numpy as np

class firsttime():

	def __init__(self, x=1, y=1):

		# This is the constructor and is invoked when the object is made

		self.x = x
		self.y = y
		self.z = np.arange(100)

	def __str__(self):

		#  when you run the command print(s), this is the function which is called

		return str(self.x)+' '+str(self.y)

	def __getitem__(self, index):

		# When s[0] is done then __getitem__ is called with index=0

		return self.z[index]

	def letssum(self):

		# A function of the class

		return np.sum(self.z)


s = firsttime(x=10, y=10)

print(s)

for i in range(10):
	print(s[i])

print(s.letssum())