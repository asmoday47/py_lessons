from random import randint

var_list = [0,0,0,0,0,0,0,0,0,0]
var_list2 = []
for i in range(10):
    var_list = [randint(0,100) for i in var_list]

for i in range(9):
    if var_list[i+1] > var_list[i]:
        var_list2.append(var_list[i+1])
    else:
        continue

print(var_list)
print(var_list2)