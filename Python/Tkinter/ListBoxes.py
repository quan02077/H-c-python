from tkinter import *

food = ["Banh mi", "Pho", "Hu Tieu"]
def submit():
    selecitem = listbox.curselection() #Gán listbox.curselection() cho selecitem
    selection = "" #Gán selection bằng rỗng

    for index in selecitem: 
        selection += listbox.get(index) + "\n" #duyệt để lấy từng giá trị đã chọn gắn vào selection
    label.config(text= "Ban chon: " + selection) #Dùng hàm label.config() để gán selection cho text và in trên window

    #label.config(text= "Ban chon: " + listbox.get(listbox.curselection())) #Nếu để hàm listbox.curselection() thì nó sẽ in ra index còn thêm listbox.get() thì nó sẽ in ra giá trị

def add():
    listbox.insert(listbox.size(), entryBox.get()) #listbox.size() để xác định vị trí thêm vào, entryBox.get() gọi hàm nhập để insert
    listbox.config(height= listbox.size())

def delete():
    for index in listbox.curselection():
        listbox.delete(index)
    #listbox.delete(listbox.curselection()) #listbox.curselection chọn vào giá trị đó để xóa
    listbox.config(height= listbox.size())

window = Tk()

listbox = Listbox(window, height= 5, width= 10, background= "#f2e5aa", selectmode= MULTIPLE)
for i in range(len(food)):
    listbox.insert(END, food[i]) #Thêm vào listbox bằng mảng
#listbox.insert(END, "Pho")
#listbox.insert(END, "Banh Mi")
#listbox.insert(END, "Hu Tieu")
listbox.config(font=("Impact", 30), justify= CENTER)
listbox.config(height= listbox.size()) #Hàm này dùng để chỉnh chiều cao linh hoạt hơn 
listbox.pack()

entryBox = Entry(window)
entryBox.pack()

submitButton = Button(window, text= "Submit", command= submit)
submitButton.pack()

addButton = Button(window, text="Add", command= add)
addButton.pack()

deleteButton = Button(window, text= "Delete", command= delete)
deleteButton.pack()

label = Label(window, text= "")
label.pack()
window.mainloop()