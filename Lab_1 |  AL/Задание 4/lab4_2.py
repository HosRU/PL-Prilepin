numberOne = 66
numberTwo = 26

if numberOne < numberTwo:
    for i in range(numberOne, numberTwo+1):
        print(i)
else: 
    for i in range(numberOne, numberTwo-1, -1):
        print(i, end=",")