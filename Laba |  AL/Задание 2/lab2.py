import math
numOne = int(input("Вводи x: "))
numTwo = int(input("Вводи t: "))
result = ((9*math.pi*numTwo+10*math.cos(numOne))/(math.sqrt(numTwo)-math.fabs(math.sin(numTwo))))*math.pow(math.e,numOne)
print("z:{0:.3f}".format(result))
