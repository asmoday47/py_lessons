#7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
#Пример строки файла: firm_1 ООО 10000 5000.
#Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
#Если фирма получила убытки, в расчет средней прибыли ее не включать.
#Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
#Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
#Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#Итоговый список сохранить в виде json-объекта в соответствующий файл.
#Пример json-объекта:
#[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

#Подсказка: использовать менеджеры контекста.

import json

profit_avg = 0
i = 0
firmlist = {}
with open("lesson5_7.txt","r", encoding="utf-8") as rdfile:
    for line in rdfile:
        splitline = line.split()
        profit = int(splitline[2]) - int(splitline[3])
        if profit > 0:
            i += 1
            profit_avg += profit
        firmlist.update({splitline[0]:profit})
    profit_dict = {"average_profit": profit_avg / i}


imp_list = [firmlist,profit_dict]

with open("lesson5_7.json","w", encoding="utf-8") as wrfile:
    json.dump(imp_list,wrfile)