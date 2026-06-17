from tkinter import *
from tkinter import messagebox

def click():
    #messagebox.showinfo("Thong bao", "Ahihi! Do ngoc")
    #messagebox.showwarning("Thong bao", "Ahihi! Do ngoc")
    #messagebox.showerror("Thong bao", "Ahihi! Do ngoc")

    #if messagebox.askokcancel("Chon", "May muon gi!"):
        #print("Danh nhau")
    #else:
        #print("Huh?")

    traloi = messagebox.askquestion("May muon gi", "Chon hay khong")
    if traloi == "yes":
        print("May muon")
    else:
        print("May khong")

window = Tk()

button = Button(window, command= click, text="Click me!")
button.pack()

window.mainloop()