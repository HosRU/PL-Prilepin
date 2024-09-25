print("№1")
number = int(input("Введите число: "))
if number > 0:
    print("Ваше число больше 0...")
elif number == 0:
    print("Ваше число равно 0")
else:
    print("Ваше число отрицательное")

print("№2")
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
