def Rectangle(a,b):
    square = a * b
    return square

for i in range(1,4):
    print(f"Введите стороны {i} прямоугольника \n")
    
    for j in range(1,2):
      a = int(input(f"Введите {j} сторону: "))
      b = int(input(f"Введите {j+1} сторону: "))
      res = Rectangle(a,b)
      print(f"Площадь {i} прямоугольника: {res}")



    