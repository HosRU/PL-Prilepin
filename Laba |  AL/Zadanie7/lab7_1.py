array = []
countArray = 6

for i in range(countArray):
    array.append(int(input()))

number = 0
for i in array:
    if(abs(i) < i+1): 
      number = i
      print(number)

array.reverse()
print(number)