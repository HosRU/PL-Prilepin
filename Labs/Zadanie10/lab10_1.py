import os
# print(os.getcwd())

text = []
with open("/home/artem/Тёмочка/PL-Prilepin/Labs/Zadanie10/Prilepin_Y242_vivod.txt", 'r') as file:
    for line in file:
        lines = line.strip()
        text.append(lines) 

with open("/home/artem/Тёмочка/PL-Prilepin/Labs/Zadanie10/Prilepin_Y242_vvod.txt", 'w') as file:
    file.write("Результат: \n")
    for i in text:
        file.write(f"{i} \n")