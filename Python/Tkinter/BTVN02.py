from tkinter import *
from tkinter import messagebox

def login():
    user_email = entry_email.get()
    user_password = entry_password.get()
    if user_email == "" or user_password == "":
        messagebox.showerror("Thông báo", "Hãy nhập đầy đủ thông tin!")
    else:
        message = f"Email: {user_email}\nPassword: {user_password}"
    messagebox.showinfo("Thông tin đăng nhập", message)

window = Tk()
window.geometry("450x200")

email = Label(window, text= "Email")
email.grid(row=0, column=2)

entry_email = Entry(width= 50)
entry_email.grid(row=0, column= 3)

password = Label(window, text= "Password")
password.grid(row= 1, column=2)

entry_password = Entry(width= 50, show= "*")
entry_password.grid(row=1, column= 3)

button = Button(window, text= "Đăng Nhập", command=login)
button.grid(row= 2, column=3)


window.mainloop()