from random import randint


#ЗАДАНИЕ: 1
def Sum(numOne, numTwo):
    return int(numOne + numTwo)
print(Sum(5,6))


#ЗАДАНИЕ: 2
def a(a,b):
    return int((1/2)*a*b)
print(a(12,8))


#ЗАДАНИЕ: 3
#minute = int(input("Введите количество минут: "))

def Day(minute):
    if(minute > 60):
        hour = int(minute / 60)
        minute = int(minute % 60)
        return hour, minute
    else:
        return minute

#print(Day(minute))


# ЗАДАНИЕ: 9
# n =X; m =Y

lom = int(input("ЦИФРУ: 1. Ломать поперёк; 2. Ломать вдоль : "))
def ChokChok(n,m,k):
    if(lom == 1):
        ostM = randint(0,m)
        result = int(n*ostM)
        if(k == result):
           return "Да"
        else:
           return "Нет"
    if(lom == 2):
        ostN = randint(0,n)
        result = int(m*ostN)
        if(k == result):
            return "Да"
        else:
            return "Нет"
print(ChokChok(4,6,8))
    
    

