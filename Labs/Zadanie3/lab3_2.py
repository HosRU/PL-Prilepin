numberTwo = int(input("Введите первое число: "))
numberThree = int(input("Введите второе число: "))
numberFour = int(input("Введите третье число: "))

if numberTwo < numberThree:
    if numberTwo < numberFour:
        result = numberTwo
    else:
        result = numberThree
else:
    if numberThree < numberFour:
        result = numberThree
    else:
        result = numberFour
print(result)