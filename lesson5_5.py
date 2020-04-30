#5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

from functools import reduce

#Создаем функцию для использования с reduce
def func_sum(x,y):
    z = int(x) + int(y)
    return z

#Создаем и наполняем файл
with open("lesson5_5.txt","w",encoding="utf-8") as wrfile:
    line = input("Введите числа через пробел")
    wrfile.write(line)

#Считаем сумму
with open("lesson5_5.txt","r",encoding="utf-8") as rdfile:
    for line in rdfile:
        var_list = line.split()
        print (reduce(func_sum,var_list))
