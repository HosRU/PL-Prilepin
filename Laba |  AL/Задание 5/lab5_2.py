def delitel(number: int):
    count:int = 1
    while count <= number:
        count = count + 1
        if number % count == 0:
            print(count)

delitel(289)