from tkinter import *

def convert():
    kg = float(text.get("1.0", END)) #Ép kiểu cho số mình vừa nhập
    gram = kg * 1000
    pound = kg * 2,20462
    ounce = kg * 35.274
    
    t1.delete(0, END) #Để xóa số trong ô entry để dọn chỗ cho số mới vào
    t1.insert(END, gram) #Lấy số gram sau khi convert insert vào ô entry 
    t2.delete(0, END)
    t2.insert(END, pound)
    t3.delete(0, END)
    t3.insert(END, ounce)

window = Tk()
window.title("Chuyen doi khoi luong!")
window.geometry("458x125")

label = Label(window, text= "Enter the weight in Kg: ")
label.grid(row= 0, column= 0, pady = 30)

text = Text(window, height= 1, width= 20)
text.grid(row= 0, column= 1, padx = 20)

button = Button(window, text= "Convert", command= convert)
button.grid(row= 0, column= 2)

label1 = Label(window, text= "Gram")
label1.grid(row=1, column=0)
t1 = Entry(window) #Tạo 1 ô entry để khi convert số sẽ vào đó
t1.grid(row=2, column=0)

label2 = Label(window, text= "Pound")
label2.grid(row=1, column=1)
t2 = Entry(window) #Tạo 1 ô entry để khi convert số sẽ vào đó
t2.grid(row=2, column=1)

label3 = Label(window, text= "Ounce")
label3.grid(row=1, column=2)
t3 = Entry(window) #Tạo 1 ô entry để khi convert số sẽ vào đó
t3.grid(row=2, column=2)

window.mainloop()