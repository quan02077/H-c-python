from tkinter import *

def submit():
    input = text.get("1.0", END)
    label.config(text= input)

window = Tk()

text = Text(window, bg= "#f2e6c4", fg= "#9342db", font= ("Ink Free", 25))
text.pack()

button = Button(window, text= "Submit", command= submit)
button.pack()

label = Label(window, text= "")
label.pack()

window.mainloop()