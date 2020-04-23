def my_func1(x,y):
    return x ** y

def my_func2(x,y):
    z = 1
    for i in range(abs(y)):
        z = z / x
    return z


x = float(input("Введите положительное число"))
y = int(input("Введите целое отрицательное число"))

print(my_func1(x,y)),
print(my_func2(x,y))