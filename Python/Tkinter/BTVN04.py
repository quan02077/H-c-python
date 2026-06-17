from tkinter import *
from tkinter import messagebox
gt = ["Nam", "Nữ"]

def apply():
    if not (y.get() or a.get() or b.get()):
        messagebox.showerror("Thông báo", "Phải chọn ít nhất 1 sở thích!")
    else:
        ketqua = "Giới tính: " + gt[x.get()] + "\n"
        ketqua += "Sở thích:  "
        if(y.get()): ketqua+= "thể thao "
        if(a.get()): ketqua+= "đọc sách "
        if(b.get()): ketqua+= "nghe nhạc "
        messagebox.showinfo("Thông tin vừa chọn", ketqua)

window = Tk()

x = IntVar()
y = BooleanVar()
a = BooleanVar()
b = BooleanVar()
for i in range(len(gt)):
    gioiTinh = Radiobutton(window, text= gt[i], variable= x, value= i)
    gioiTinh.pack()

theThao = Checkbutton(window, text= "Thể thao", variable= y)
doSach = Checkbutton(window, text= "Đọc sách", variable= a)
ngheNhac = Checkbutton(window, text= "Nghe nhạc", variable= b)
theThao.pack()
doSach.pack()
ngheNhac.pack()

button = Button(window, text= "Xác nhận", command= apply)
button.pack()

window.mainloop()