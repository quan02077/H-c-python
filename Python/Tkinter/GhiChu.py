from tkinter import *
from tkinter import filedialog
from tkinter import colorchooser
from tkinter import messagebox
def Save():
    file = filedialog.asksaveasfile(initialdir="E:\\Python\\Tkinter", 
                                    defaultextension= ".txt", 
                                    filetypes= (("Text file", "*.txt"), ("All files", "*.*")))
    if file:
        filetext = str(text.get("1.0", END))
        file.write(filetext)
        file.close()
    else:
        message = messagebox.showerror("Erorrs", "Không lưu được file")

def Open():
    filepath = filedialog.askopenfilename(initialdir="E:\\Python\\Tkinter", 
                                      title= "Open file", 
                                      filetypes= (("Text file", "*.txt"), ("All files", "*.*")))
    if filepath:
        file = open(filepath, 'r')
        text.delete("1.0", END)
        text.insert("1.0", file.read())
        file.close()
    else:
        message = messagebox.showerror("Erorrs", "Không mở được file")

def color():
   color = colorchooser.askcolor(title= "Color chooser")
   text.config(bg= color[1])

window = Tk()
window.geometry("600x400")
window.title("Simple Note")
window.config(background= "white")

text = Text(window)
text.pack()

menubar = Menu(window)
window.config(menu= menubar)
file_menu = Menu(menubar, tearoff= 0)
menubar.add_cascade(label= "File", menu= file_menu)
file_menu.add_command(label= "Save", command= Save)
file_menu.add_command(label= "Open", command= Open)

format_menu = Menu(menubar, tearoff= 0)
menubar.add_cascade(label= "Format", menu= format_menu)
format_menu.add_command(label= "Color", command= color)

window.mainloop()