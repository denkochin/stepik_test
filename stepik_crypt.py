'''
Напишите программу, которая умеет шифровать и расшифровывать шифр подстановки.
Программа принимает на вход две строки одинаковой длины, на первой строке записаны
символы исходного алфавита, на второй строке — символы конечного алфавита, после чего
идёт строка, которую нужно зашифровать переданным ключом, и ещё одна строка, которую
нужно расшифровать.
Пусть, например, на вход программе передано:
abcd
*d%#
abacabadaba
#*%*d*%
Это значит, что символ a исходного сообщения заменяется на символ * в шифре,
b заменяется на d, c — на % и d — на #.
Нужно зашифровать строку abacabadaba и расшифровать строку #*%*d*% с помощью
этого шифра. Получаем следующие строки, которые и передаём на вывод программы:
*d*%*d*#*d*
dacabac
Sample Input 1:

abcd
*d%#
abacabadaba
#*%*d*%
Sample Output 1:

*d*%*d*#*d*
dacabac
Sample Input 2:

dcba
badc
dcba
badc
Sample Output 2:

badc
dcba
'''
a, b, tocrypt, todecrypt = input(), input(), input(), input()
c, d = str.maketrans(a, b), str.maketrans(b, a)
'''
dict(zip(names, ages)) makes dict from strings 
{'Harry': 60, 'Dick': 35, 'Tom': 50}
'''
print(tocrypt.translate(c), '\n', todecrypt.translate(d), sep='')

