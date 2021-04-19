a = []
b = []
c = []
while True:
    a = input() # вводим строку
    if a == "end":
        break # если строка равна "end", прерываем цикл
    a = [int(i) for i in a.split()] # итерируем по каждой строке, переводя элементы из str в int
    b.append(a) # формируем матрицу b из строк, введённых пользователем: это исходная матрица
print(b)
if len(b) != 1 or len(b[0]) != 1:
    for i in range(-len(b), 0):
        for j in range(-len(b[i]), 0):
            up = b[i + len(b[0]) - 1][j]
##            print(up)
            right = b[i][j + len(b) + 1]
##            print(right)
            down = b[i + len(b[0]) + 1][j]
##            print(down)
            left = b[i][j + len(b) - 1]
##            print(left)
            print(up + right + down + left, end = " ")
            if j == -len(b[0]) - 1:
                print()
else:
    print(b[0][0] * 4)
