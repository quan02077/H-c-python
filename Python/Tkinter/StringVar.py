from tkinter import *

window = Tk()

ten_bien = StringVar() 

o_nhap_lieu = Entry(window, textvariable=ten_bien)
o_nhap_lieu.pack()

window.mainloop()