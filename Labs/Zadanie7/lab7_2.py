array = [2,4,0,6,8,0,16,3,0,5,7,0,9]

sum = 0
for i in array: sum += i

for j in array:
    if j == 0:
        array[array.index(j)] += sum / len(array)
print(array)