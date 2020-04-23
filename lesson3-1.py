def divider(x , y):
    if y == 0:
        return "Делить на ноль нельзя"
    else:
        return  x / y

x = int(input("Введите натуральное число"))
y = int(input("Введите натуральное число"))
print (divider(x,y))
