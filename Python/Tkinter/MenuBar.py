from tkinter import *

def hello():
    print("Chao")
def doan():
    print("Cut ra ngoai!")
window = Tk()

menu = Menu(window)
window.config(menu= menu)
file_menu = Menu(menu, tearoff= 0)
menu.add_cascade(label= "File", menu= file_menu)
file_menu.add_command(label="Open", command=hello)
file_menu.add_separator()
file_menu.add_command(label="Exit", command= quit)

edit_menu = Menu(menu, tearoff= 0)
menu.add_cascade(label= "Edit", menu= edit_menu)
edit_menu.add_command(label= "Guess", command= doan)

window.mainloop()