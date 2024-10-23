text = "Выходили. Eтти. На. Охоту и ехали за ёлками. В лес".split(" ")
count = 0
for i in text:
    if i.find(".") > 0: i.replace(".", ""); count+= 1
print("Число удалённых точек: ", count)