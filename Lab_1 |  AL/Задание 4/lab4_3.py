numberOne = 29
numberTwo = 13

if numberOne % 2 == 0:
    for i in range(numberOne-1, numberTwo-1, -2):
        print(i)
else: 
    for i in range(numberOne, numberTwo-1, -2):
        print(i)
