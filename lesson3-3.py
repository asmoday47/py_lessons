def my_func(var1,var2,var3):
    return(max(var1+var2,var2+var3,var1+var3))

var1 = float(input("Введите первое число"))
var2 = float(input("Введите второе число"))
var3 = float(input("Введите третье число"))

print(my_func(var1,var2,var3))