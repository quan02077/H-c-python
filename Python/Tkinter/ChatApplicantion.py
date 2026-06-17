from tkinter import * 

def send():
    tin_nhan = entry_tinNhan.get()
    if tin_nhan.strip() != "": #Strip() dùng để xóa khoảng trắng, nếu khác khoảng trắng thì sẽ in ra text_display
         text_display.insert(END, f"You: {tin_nhan}\n")
         entry_tinNhan.delete(0,END)
        
window = Tk()
window.geometry("400x300")

text_display = Text(window, width= 40, height= 15)
text_display.grid(row= 0, column= 0, padx= 10)

entry_tinNhan = Entry(width= 40)
entry_tinNhan.grid(row= 1, column= 0, pady= 20)

button = Button(window, text="Send", command= send)
button.grid(row=1, column= 1)

window.mainloop()