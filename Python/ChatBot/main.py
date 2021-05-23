from fuzzywuzzy import fuzz
import numpy as np

y = {
	'Hello': 'Hi! This is Arnold!',
	'Bye': 'Aww! Sad to see you go!'
}

keys = list(y.keys())

threshold = 50

while True:
	x = input()
	select = [fuzz.partial_ratio(x, i) for i in keys]
	argmax = np.argmax(select)
	if select[argmax] < threshold:
		print('I do not understand', threshold, select[argmax])
	else:
		print(y[keys[argmax]])
	if keys[argmax] == 'Bye':
		break
