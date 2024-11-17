array = [2,4,6,8,10,12,3,5,7,9,11,13]

sum = 0
for i in array:
    if array.index(i) % 2 != 0:
        sum += i
        print(f"Индекс: {array.index(i)}, число: {i}")

print(f"Массив: {array}", f"Сумма: {sum}" )

