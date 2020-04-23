def upper_maker(inc_str):
    inc_str = inc_str.capitalize()
    return inc_str

oneword = input("Введите одно слово")
print(upper_maker(oneword))

fewwords = input("Введите несколько слов через пробел").split()
for i in fewwords:
    print(upper_maker(i), end=' ')
