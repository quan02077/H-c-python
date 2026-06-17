from tkinter import *
from tkinter import messagebox
from tkcalendar import DateEntry

def get_date():
    date = cal.get_date()
    messagebox.showinfo("Thông báo", f"Ngày được chọn: {date}")

root = Tk()
root.title("Ví dụ Date Entry")

cal = DateEntry(root, width=12, background='darkblue',
foreground='white', borderwidth=2)
cal.pack(padx=10, pady=10)

button = Button(root, text="Lấy ngày",
command=get_date)
button.pack(pady=5)

root.mainloop()
