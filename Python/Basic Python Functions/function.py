# A basic program to show how to define functions

x = [1, 2, 3]


def lets_make_a_function(x, y=[2, 3, 4]):

	for no, (x_i, y_i) in enumerate(zip(x, y)):
		print(x_i, y_i)

	return 1, [3, 4]


t, s = lets_make_a_function(x)
