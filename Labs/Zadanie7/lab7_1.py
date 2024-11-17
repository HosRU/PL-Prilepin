# array = [2,4,6,8,16,3,5,7,9]
array = [int(input("Ввод циферок: \n")) for num in range(8)]

max = array[0]
for item in array: 
    if item > max: max = item
print(f"Максимальный элемент массива: {max}") 

# array.reverse()

newArray = [num for num in array[::-1]]
print(newArray)
    
   
    

