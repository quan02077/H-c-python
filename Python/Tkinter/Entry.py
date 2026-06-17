from tkinter import *
def submit():
    username = entry.get()
    label.config(text= username) #Nhập dữ liệu
def delete():
    entry.delete(0, END) #Xóa dòng người dùng vừa nhập
def backspace():
    entry.delete(len(entry.get())-1,END) #Xóa từng kí tự một
window = Tk()
submit = Button(window, text="Submit", command= submit)
submit.pack(side= RIGHT)

delete = Button(window, text="Delete", command= delete)
delete.pack(side= RIGHT)

backspace = Button(window, text="Backspace", command= backspace)
backspace.pack(side= RIGHT)

out = Button(window, text="Quit", command=window.quit)
out.pack(side= RIGHT)  

entry = Entry()
entry.config(font=("Ink Free", 50))
entry.config(bg="#1f262e")
entry.config(fg="#1bde55")
#entry.insert(0, "Vai chuong") #Them van ban mac dinh
#entry.config(state= DISABLED) #Active or Disable
entry.config(width= 30)
#entry.config(show="*") #Khi ta nhập bất cứ thứ gì thì nó sẽ thay thế bằng dấu *
entry.pack()

label = Label(window, text= "")
label.pack()
window.mainloop()