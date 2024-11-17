arrayOne = [1,3,5,7,9,11,13]
arrayTwo = [2,4,6,8,10,12,14]
arrayThree = [1,2,3,4,5,6,7,8,9]

def sumArray(array):
    sum = 0
    arithmetic = 0
    for i in array:
        sum += i

    arithmetic = int(sum / len(array))
    return f"Сумма: {sum}, Арифметическое: {arithmetic}"

sumArrayOne = sumArray(arrayOne)
sumArrayTwo = sumArray(arrayTwo)
sumArrayThree = sumArray(arrayThree)
print(f"Результат: {sumArrayOne}")
print(f"Результат: {sumArrayTwo}")
print(f"Результат: {sumArrayThree}")



