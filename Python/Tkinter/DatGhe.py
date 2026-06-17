from tkinter import *

window = Tk()
window.title("Đặt ghế hội trường")


def doi_mau(button):
    if button["bg"] == "SystemButtonFace":  
        button.config(bg="lightgreen")      
    else:
        button.config(bg="SystemButtonFace") 

row = 0
col = 0
for i in range(1, 31):   
    btn = Button(window, text=f"Seat {i}", width=10, height=2)
    btn.grid(row=row, column=col, padx=5, pady=5)
    btn.config(command=lambda b=btn: doi_mau(b))  
    col += 1
    if col == 6:  
        col = 0
        row += 1

window.mainloop()