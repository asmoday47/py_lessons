def make_sum(var_list):
    global sum_end, sum_vars
    for i in var_list:
        if i.isdigit():
            sum_vars += int(i)

        else:
            sum_end = 1
            break
    return sum_vars

sum_end = 0
sum_vars = 0
while sum_end == 0:
    var_list = input("Введите числа через пробел").split()
    print(make_sum(var_list))