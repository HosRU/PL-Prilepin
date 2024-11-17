n = 3
a = []
for i in range(n):
    b = []
    for j in range(n):
        print('Введите [',i,',',j,']')
        b.append(int(input()))
    a.append(b)
print(a)

for i in range(n):
    for j in range(n):
        print(a[i][j], end=' ')
    print()