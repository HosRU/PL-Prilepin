import random
quantity = 6
c = random.randint(1,4)
d = 3
matrix = []

for i in range(quantity):
    stringMatrix = []
    for j in range(quantity-1):
        stringMatrix.append(random.randint(1,12))
    matrix.append(stringMatrix)

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == c:
            matrix[i][j] *= d


with open("/home/artem/Тёмочка/PL-Prilepin/Labs/Zadanie10/Prilepin_Y242_vivod.txt", 'w') as file:
    for stringMatrix in matrix:
            for elemMatrix in stringMatrix:
                file.write(f"{elemMatrix} ")
            file.write("\n")
        