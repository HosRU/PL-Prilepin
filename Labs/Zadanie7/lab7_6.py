array = [2,17,6,8,16,3,5,19]
for i in array:
    if i < 15:
        array[array.index(i)] = i * 2
        
print(array)

    