import time

SIZE = 10000000


def timeMe():
	total = 0
	for i in range(SIZE):
		total += i


start = time.time()
timeMe()
print(time.time() - start)
