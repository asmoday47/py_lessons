from random import randint

var_list = [0,0,0,0,0,0,0,0,0,0]
var_list2 = []
for i in range(10):
    var_list = [randint(0,5) for i in var_list]

for i in var_list:
    if i in var_list2:
        continue
    else:
        var_list2.append(i)

print(var_list)
print(var_list2)
