from tkinter import * 
import requests 
import json 
 
def clicked(event): 
    api = f'https://api.github.com/users/{entry.get()}' 
    user_data = requests.get(api).json() 
    company = user_data['company'] 
    created_at = user_data['created_at'] 
    email = user_data['email'] 
    id = user_data['id'] 
    name = user_data['name'] 
    url = user_data['url'] 
    json_data = {'company': company, 'created_at': created_at, 'email': email, 'id': id, 'name': name, 'url': url} 
    with open('Labs/Zadanie11/res.json', 'w') as f: 
        json.dump(json_data, f) 
 
window = Tk() 
window.title("Практическая работа 11") 
window.geometry("700x450") 
 
base_lbl = Label(text="Введите последнюю цифру зачётной книжки") 
base_lbl.place(relx=.5, rely=.4, anchor="center")  
 
entry = Entry(window, width=40) 
entry.place(relx=.5, rely=.5, anchor="center") 
 
btn = Button(text="Создать Архив с данными") 
btn.place(relx=.5, rely=.6, anchor="center") 
btn.bind("<Button-1>", clicked) 
 
window.mainloop()