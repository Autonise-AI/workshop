import time

cdef unsigned long long int SIZE = 10000000
cdef double start

def timeMe():
    cdef unsigned long long int total = 0
    cdef int i
    for i in range(SIZE):
        total = total + i

    return total


start = time.time()
timeMe()
print(time.time() - start)
