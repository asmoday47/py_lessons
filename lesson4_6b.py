from itertools import cycle
from time import sleep

var_list = ["Nanananana", "It's a D, O, double G", "SNOOP DOGG!!!!"]

for i in cycle(var_list):
    print(i)
    sleep(1)
