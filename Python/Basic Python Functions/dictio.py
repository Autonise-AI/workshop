# A program to show the usage of dictionaries
# Notice that dictionary values can even be functions
# Understand the scope of a function
# Can play around this code by commenting some lines and seeing the changes/errors


x = {}
y = [1, 2, 3]

def function1(d):
	# for i in range(d):
	# 	print(i)
	print('Hello')
	newfunction()

def newfunction():
	print('first')
	print('Second')
	aurek()
	def aurek():
		print('innerfunction')
	

# aurek()
newfunction()
x['String'] = 'Hi'
x['Number'] = 12
x['List'] = y
x['something'] = function1

# x.keys() = ['String', 'Number']
for i in x.keys():
	if i == 'something':
		x[i](20)
	else:
		print(i, x[i])