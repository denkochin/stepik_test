'''
Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
Первое слово в тексте последнего файла: "We".

Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора.

Все файлы располагаются в каталоге по адресу:
https://stepic.org/media/attachments/course67/3.6.3/

Загрузите содержимое ﻿последнего файла из набора, как ответ на это задание.
'''
import requests
url = 'https://stepic.org/media/attachments/course67/3.6.3/699991.txt'
oldfile = url[-10:]
r = requests.get(url)
newfile = r.text
while 'We' not in newfile:
    r = requests.get(url)
    oldfile = url[-10:]
    print(oldfile)
    newfile = r.text
    print(newfile)
    url = url.replace(oldfile, newfile)
    print(url)
