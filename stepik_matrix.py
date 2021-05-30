'''
Напишите программу, на вход которой подаётся прямоугольная матрица
в виде последовательности строк.
После последней строки матрицы идёт строка, содержащая только строку "end"
(без кавычек, см. Sample Input).
Программа должна вывести матрицу того же размера, у которой каждый элемент
в позиции i, j равен сумме элементов первой матрицы на
позициях (i-1, j), (i+1, j), (i, j-1), (i, j+1).
У крайних символов соседний элемент находится с противоположной стороны матрицы.
В случае одной строки/столбца элемент сам себе является
соседом по соответствующему направлению.
Sample Input 1:
9 5 3
0 7 -1
-5 2 9
end
Sample Output 1:
3 21 22
10 6 19
20 16 -1
Sample Input 2:
1
end
Sample Output 2:
4

7 2 3 4
-1 4 12 1
-10 5 8 0
1 2 3 4
end

6 16 21 15
2 18 16 15
5 4 20 3
3 11 17 8

Решение:
Получаем строку "1 2 3"
Проверяем, не является ли она "end", если является - выводим результат
Если не является, создаём из неё список с целыми числами
- записываем список в основной список

[
0 [0, 1, 2]
1 [0, 1, 2]
2 [0, 1, 2]
]

[ [1] ]

[ [1, 1, 1][1, 1, 1][1, 1, 1] ]

[ [1,1,1] ]

[ [1][1][1] ]

'''
a = []
b = []
while True:
    a = input()
    if a == "end":
        break
    a = [int(i) for i in a.split()]
    b.append(a)
## print(b)
if len(b) != 1 or len(b[0]) != 1:
    for i in range(len(b)):
        for j in range(len(b[0])):
            up = b[(i - 1)%len(b)][j]
##            print(up)
            right = b[i][(j + 1)%len(b[0])]
##            print(right)
            down = b[(i + 1)%len(b)][j]
##            print(down)
            left = b[i][(j - 1)%len(b[0])]
##            print(left)
            print(up + right + down + left, end = "")
            if j != len(b[0]) - 1:
                print(" ", end = "")
            else:
                print()
else:
    print(b[0][0] * 4)

'''
a = None ## variable for user input
b = [] ## variable for matrix of integers
c = 0 ## iterator for counting inputs / number of rows
print(type(a), type(b)) ## checking types of a and b
while True:
    a = input() ## getting user input in string
    if a == "end": ## checking the end of matrix
        break
    c += 1
    a = a.split() ## splitting string into list
    print("a is ", a)
    b.append(a)
    print("b is ", b)
    print(c, "inputs made") ## checking the sum of inputs
print("a is ", a) ## checking the a value
print("b is ", b) ## checking the b value
for i in range(0, c - 1):
    for j in range(0, len(b[0]) - 1):
        b[i][j] = int(b[i - 1][j]) + int(b[i][j + 1]) + int(b[i + 1][j]) + int(b[i][j - 1])
print("b is ", b, "and b[0] length is ", len(b[0]))
'''


'''
a = []
b = []
c = []
while b != "end":
    b = input()
    c = b.split()
    if b != "end":
        a.append(c)
else:
    print(a)
    print(len(a[0]))
    print(b)
    print(len(b))
    print(c)
    print(len(c))
##    a[0][0] = int(a[0 + 1][0]) + int(a[0][-1]) + int(a[1][0]) + int(a[-1][0])
##    a[0][1] = int(a[0][0]) + int(a[0][2]) + int(a[1][1]) + int(a[2][1])
##    a[0][2] = int(a[0][1]) + int(a[0][2]) + int(a[1][0]) + int(a[2][0])
##    a[1][0] = int(a[0][1]) + int(a[0][2]) + int(a[1][0]) + int(a[2][0])
##    a[1][1] = int(a[0][1]) + int(a[0][2]) + int(a[1][0]) + int(a[2][0])
##    a[1][2] = int(a[0][1]) + int(a[0][2]) + int(a[1][0]) + int(a[2][0])
##    a[2][0] = int(a[0][1]) + int(a[0][2]) + int(a[1][0]) + int(a[2][0])
##    a[2][1] = int(a[0][1]) + int(a[0][2]) + int(a[1][0]) + int(a[2][0])
##    a[2][2] = int(a[0][1]) + int(a[0][2]) + int(a[1][0]) + int(a[2][0])
'''    

''' Solution from the web
a = ()
b = []
while a != ["end"]: 
    a = input().split()
    if a == ["end"]:
        break
    c = [int(item) for item in a]     
    b.append(c)
for i in b:
    for j in i:
        ii, bi = i.index(j), b.index(i)
        print (b[bi][(ii+1)%len(i)] + b[bi][ii-1] + b[(bi+1)%len(b)][ii] + b[bi-1][ii], end = " ")
      print()
      
for row in range(len(b)):
   for col in range(len(b[row])):
       используйте b[row][col-1] и т.д.
'''

'''
Оптимальное решение из базы решений Stepik
c = []
while True:
    a = [i for i in input().split()]
    if a == ['end']:
        break
    c.append(a)
n, m = len(c), len(c[0])
for i in range(n):
    for j in range(m):
        x = int(c[i][j-1]) + int(c[i][j+1-m]) + int(c[i-1][j]) + int(c[i+1-n][j])
        print(x, end=' ')
    print()
'''
