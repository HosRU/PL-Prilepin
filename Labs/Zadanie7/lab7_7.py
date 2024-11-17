array = [2,4,6,8,16,3,5,7,9]

max = array[0]
for i in array:
    if i > max:
        max = i

print(f"Максимальный элемент: {max}; Порядковый номер: {array.index(max)}")