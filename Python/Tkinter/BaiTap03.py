from tkinter import *

def submit():
    user_input = entry.get()
    label1.config(text="You wrote: " + user_input)

window = Tk()
window.geometry("350x120")

label = Label(window, text="Are you a Geek?")
label.grid(row= 0, column= 0)

entry = Entry(window, width=20)
entry.grid(row= 0, column= 1)

button = Button(window, text="Submit", command=submit)
button.grid(row= 0, column= 2)

label1 = Label(window, text="")
label1.grid(row= 2, column= 1)

window.mainloop()
