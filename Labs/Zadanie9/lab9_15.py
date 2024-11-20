import random
quantity = 6
c = random.randint(1,9)
d = 3
matrix = []

for i in range(quantity):
    stringMatrix = []
    for j in range(quantity-1):
        stringMatrix.append(random.randint(1,9))
    matrix.append(stringMatrix)

# print(matrix)

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == c:
            matrix[i][j] *= d

# print(matrix)