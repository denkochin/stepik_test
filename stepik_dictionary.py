'''
Простейшая система проверки орфографии может быть основана на использовании
списка известных слов.
Если введённое слово не найдено в этом списке, оно помечается как "ошибка".

Попробуем написать подобную систему.

На вход программе первой строкой передаётся количество d известных нам слов,
после чего на dd строках указываются эти слова. Затем передаётся количество l
строк текста для проверки, после чего ll строк текста.

Выведите уникальные "ошибки" в произвольном порядке. Работу производите без учёта
регистра.

Sample Input:

4
champions
we
are
Stepik
3
We are the champignons
We Are The Champions
Stepic
Sample Output:

stepic
champignons
the
'''
d = int(input())
d2 = set()
l2 = []
w = None
for word in range(d):
    d2.add(input().lower())
##print('dictionary is', d2)
l = int(input())
for word in range(l):
    word = input().split()
##    print('string is', word)
    for i in word:
##        l2.append(i.lower())
##        print('uppercase word is', i)
        if i.lower() not in d2:
##            print('-----output is', i)
            l2.append(i.lower())
##print('final list is', l2)
##print(set(l2))
for word in set(l2):
    if word not in d2:
        print(word)
'''
d = int(input())
d2 = set()
l2 = []
l2_low = []
for word in range(d):
    d2.add(input().lower())
##print(d2)
l = int(input())
for word in range(l):
    word = input().split()
    for i in word:
        l2.append(i)
        l2_low.append(i.lower())
        
##print(l2)
##for word in set(l2):
##    word = word.lower()
##    print(word)
##    if word.lower() not in d2:
##        print('*')
##print(l2_low)
##    if word not in d2:
##        print(word)
'''
