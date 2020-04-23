from math import factorial
from itertools import count
from time import sleep

def fibo_gen():
    for el in count(1):
        yield factorial(el)

j = 0
for i in fibo_gen():
    if j <15:
        print(i)
        j += 1
        sleep(1)
        continue
    else: break
