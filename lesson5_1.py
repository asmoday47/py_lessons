#1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
#Об окончании ввода данных свидетельствует пустая строка.

with open("lesson5_1.txt","w",encoding="utf-8") as wrfile:
    while True:
        line = input("Введите строку")
        if line =="":
            break
        else:
            wrfile.write(line+"\n")
