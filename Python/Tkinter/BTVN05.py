from tkinter import *
mh= ["Kinh tế chính trị", "OOP", "Python"]

def display():
    text.delete("1.0", END)
    selectItem = listbox.curselection()
    select =""
    for i in selectItem:
        select += listbox.get(i) + "\n"
    text.insert(END, select)

window = Tk()

listbox = Listbox(window,bg=  "#f2e6c4",selectmode= MULTIPLE)
for i in range(len(mh)):
    listbox.insert(END, mh[i])
listbox.config(height= listbox.size(), font= ("Impact", 30), justify= 'center')
listbox.pack()

button = Button(window, text="Hiển thị chi tiết", command=display)
button.pack()

text = Text(window)
text.pack()

window.mainloop()