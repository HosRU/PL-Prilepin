# array = [9,7,5,4,16,12,10,8,6]
array = [int(input("Ввод циферок: \n")) for num in range(8)]

min = array[0]
for item in array: 
    if item < min: min = item
print(f"Минимальный элемент массива: {min}. Его индекс равен: {array.index(min)}") 