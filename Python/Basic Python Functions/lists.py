# Show usage of lists, for-loop, enumerate

x = ['1', 1, 'asdf', "asdf", 1.23]
y = [0]*10

print('This is y', y)

y[0] += 1

print('This is updated y', y)

for x_i in x:
	print(x_i)

print('\n')  # Two new lines. One is by default

for no, x_i in enumerate(x):
	print(no, x_i)
