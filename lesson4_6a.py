from itertools import count
from time import sleep

var = int(input("Введите целое число"))

for i in count(var):
    print(i)
    sleep(1)
    
