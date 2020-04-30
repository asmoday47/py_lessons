#4. Создать (не программно) текстовый файл со следующим содержимым:
#One — 1
#Two — 2
#Three — 3
#Four — 4
#Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

#Создаем словарь-переводчик
trlate = {"One":"Один","Two":"Два","Three":"Три","Four":"Четыре"}

#Заменяем слова и записываем в новый файл
with open("lesson5_4.txt",'r',encoding="utf-8") as file1:
    with open("lesson5_4a.txt",'w',encoding="utf-8") as file2:
        for line in file1:
            i = 0
            splitline = line.split()
            for el in splitline:
                for word in trlate:
                    if el == word:
                        splitline[i] = trlate.get(word)
                i += 1
            file2.write(' '.join(splitline)+"\n")
