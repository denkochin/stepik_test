'''
Имеется файл с данными по успеваемости абитуриентов. Он представляет из себя набор
строк, где в каждой строке записана следующая информация:
Фамилия;Оценка_по_математике;Оценка_по_физике;Оценка_по_русскому_языку
Поля внутри строки разделены точкой с запятой, оценки — целые числа.
Напишите программу, которая считывает исходный файл с подобной структурой и для
каждого абитуриента записывает его среднюю оценку по трём предметам на отдельной
строке, соответствующей этому абитуриенту, в файл с ответом.
Также вычислите средние баллы по математике, физике и русскому языку по всем
абитуриентам и добавьте полученные значения, разделённые пробелом, последней
строкой в файл с ответом.
В качестве ответа на задание прикрепите полученный файл со средними оценками
по каждому ученику и одной строкой со средними оценками по трём предметам.
Примечание. Для разбиения строки на части по символу ';' можно использовать метод

split следующим образом:
print('First;Second-1 Second-2;Third'.split(';'))
# ['First', 'Second-1 Second-2', 'Third']
Sample Input:

Петров;85;92;78
Сидоров;100;88;94
Иванов;58;72;85
Sample Output:

85.0
94.0
71.666666667
81.0 84.0 85.666666667
'''
import copy
s1 = ''
l2 = []
ave1 = 0
ave2 = 0
ave3 = 0
## считываем файл - получаем список строк
with open('dataset_3363_4.txt', 'r') as f:
    s1 = f.read().split()
## переводим в список списков
for i in range(len(s1)):
    s1[i] = s1[i].split(';')
## созздаем копию первого списка списков, чтобы его модифицировать
##for i in s1:
##    l2.append(i)
l2 = copy.deepcopy(s1)
##print(s1)
##print(l2)
##print()
## первый столбец наполняем именами из первого списка
## второй столбец наполняем средними значениями по ученику
for i in range(len(l2)):
##    print(i)
##l2[2][1] = 0
##    l2[i][0] = s1[i][0]
    l2[i][1] = (int(l2[i][1]) + int(l2[i][2]) + int(l2[i][3])) / 3 ##  round
##print(s1)
##print(l2)
##print()
## обрезаем лишние столбцы
for i in range(len(l2)):
    l2[i] = l2[i][:2]
##print(s1)
##print(l2)
##print()
for i in range(len(s1)):
    ave1 += int(s1[i][1])
##    print(ave1)
for i in range(len(s1)):
    ave2 += int(s1[i][2])
for i in range(len(s1)):
    ave3 += int(s1[i][3])
aver1 = ave1 / len(s1) ##  round
aver2 = ave2 / len(s1) ##  round
aver3 = ave3 / len(s1) ##  round
##print(ave1)
##print(len(s1))
##print(aver1)
aver1, aver2, aver3 = str(aver1), str(aver2), str(aver3)
##print('math average is ', aver1)
##print('physics average is ', aver2)
##print('russian average is ', aver3)
##print(l2[0][0], str(l2[0][1]))
for i in l2:
    i[1] = str(i[1])
##print(l2)
with open('dataset_3363_4_out.txt', 'w') as f:
##    f.writelines(l2)
    for i in l2:
##        f.write(i[0])
##        f.write(' ')
        f.write(str(i[1]))
        f.write('\n')
    f.write(str(aver1))
    f.write(' ')
    f.write(str(aver2))
    f.write(' ')
    f.write(str(aver3))

