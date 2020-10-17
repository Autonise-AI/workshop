# Show usage of lists, for-loop, enumerate

x = ['1', 1, 'asdf', "asdf", 1.23]

for x_i in x:
	print(x_i)

print('\n')

for no, x_i in enumerate(x):
	print(no, x_i)