import math

def Sixth(a):
    square = ((3*math.sqrt(3))/2)*a**2
    return square

res = Sixth(6)
print(f"Площадь равна: {int(res)}")