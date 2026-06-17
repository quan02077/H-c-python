from tkinter import *
from PIL import Image, ImageTk

def doi_hinh():
    global photo2
    photo2 = PhotoImage(file= "Smile.gif")
    label.config(image= photo2)

window = Tk()

image1 = Image.open("rickroll.jpg")
photo = ImageTk.PhotoImage(image= image1)

label = Label(window, image= photo)
label.pack()

button = Button(window, text= "Đổi hình", command= doi_hinh)
button.pack()

window.mainloop()