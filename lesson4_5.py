from functools import reduce

def func_mult(x,y):
    z = x * y
    return z

var_list = [i for i in range(100,1001,2)]
print (reduce(func_mult, var_list))
