from tkinter import *
from tkinter import colorchooser

def color():
    color = colorchooser.askcolor()
    window.config(bg = color[1])
window = Tk()
button = Button(window, text="Chon mau", command=color)
button.pack()
window.mainloop()