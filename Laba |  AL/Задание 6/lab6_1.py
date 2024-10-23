text = "Выходили етти на охоту и ехали за ёлками в лес.".split(" ")
count = 0
for i in text:
    if i[0] == 'е': count+= 1
    
print("Слов на е: ", count) 