def Rectangle(a,b):
    square = a * b
    return square

def Square(a):
    square = a**2
    return square

def Round(r):
    square = 3,14 * r**2
    return square

resultRectangle = Rectangle(5,4)
resultSquare = Square(5)
resultRound = Round(6)
print(f"Площадь прямоугольника: {resultRectangle}")
print(f"Площадь квадрата: {resultSquare}")
print(f"Площадь круга: {resultRound}")