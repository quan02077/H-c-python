from tkinter import *
def add():
    listbox.insert(END, entry.get())
    entry.delete(0, END)
def delete():
    listbox.delete(listbox.curselection())

window = Tk()
window.geometry("350x220")

listbox = Listbox(window, height= 10, width= 50)
listbox.pack()

entry = Entry()
entry.pack(pady=(10, 5),padx=10)

add_button = Button(window, text= "Add", command= add)
add_button.pack(side= LEFT)

delete_button = Button(window, text= "Delete", command= delete)
delete_button.pack(side= LEFT)

window.mainloop()