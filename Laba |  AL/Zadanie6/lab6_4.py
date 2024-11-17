text = "Выходили. Eтти. На. Охоту и ехали за ёлками. В лес".lower().split(" ")
for i in text: 
    if i.find("а") > 0: res = i.replace("а", "о"); print("Sybol: ", len(i), "res: ", res) 