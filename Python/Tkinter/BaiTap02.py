from tkinter import *
from tkinter import messagebox

def message():
    messagebox.showinfo("Thông báo", "Bạn đã nhấn vào nút!")

window = Tk()
window.title("Chào mừng đến với Tkinter!")
#window.geometry(("450x250"))

button = Button(window, text= "Nhấn vào đây", command= message)
button.pack()

window.mainloop()