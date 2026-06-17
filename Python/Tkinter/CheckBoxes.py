from tkinter import *
from PIL import Image, ImageTk

def display():
    if (x.get() == 1) & (y.get() == 0):
        label.config(text= "I like Python!")
    elif (x.get() == 0) & (y.get() == 1):
        label.config(text="I like C sharp!")
    elif (x.get() == 1) & (y.get() == 1):
        label.config(text="I like both Python and C sharp!")
    else:
        label.config(text="I don't like either!")
window = Tk()
window.config(background= "#363d38")
x = IntVar()
y = IntVar()

check = Checkbutton(window, text="Python", variable=x, onvalue=1, offvalue= 0, command=display)
check.config(font=("Arial", 15))
check.config(fg= "#1bde55")
check.config(bg= "#363d38")
check.config(activebackground= "blue")
check.config(activeforeground= "pink")

image = Image.open("logo_python.png")
image = image.resize((60,60))
photo1 = ImageTk.PhotoImage(image=image)

check.config(image=photo1, compound="left")
check.config(anchor= W) #anchor dùng để đưa cái checkbox về phía tây, nam ,....
check.pack()

check1 = Checkbutton(window, text="C#", variable=y, onvalue=1, offvalue= 0, command=display)
check1.config(font=("Arial", 15))
check1.config(fg= "#1bde55")
check1.config(bg= "#363d38")
check1.config(activebackground= "blue")
check1.config(activeforeground= "pink")

image1 = Image.open("Csharp_Logo.png")
image1 = image1.resize((40,40)) #Dùng để resize lại hình kích thước hình ảnh
photo2 = ImageTk.PhotoImage(image=image1)

check1.config(image=photo2, compound="left")
check1.config(anchor= W)
check1.pack()

label = Label(window, text="")
label.pack()
window.mainloop()