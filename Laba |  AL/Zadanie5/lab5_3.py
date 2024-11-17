def stepen(number: int):
    count: int = 0
    while count <= number:
        count = count + 1
        if(2**count <= number):
            print(2**count, count, "\n")

stepen(256)