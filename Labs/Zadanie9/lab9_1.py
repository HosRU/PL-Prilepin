import random
quantity = 6
matrix = []

for i in range(quantity):
    stringMatrix = []
    for j in range(quantity):
        stringMatrix.append(random.randint(1,9))
    matrix.append(stringMatrix)

for i in range(quantity):
    for j in range(quantity):
        print(matrix[i][j], end=' ')
    print()

sum = 0
for i in range(quantity):
    for j in range(i+1, quantity):
        sum += matrix[i][j]

print(f"Сумма чисел над главной диагональю: {sum}")

        

