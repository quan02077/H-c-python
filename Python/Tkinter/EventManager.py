from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
from tkinter import colorchooser, messagebox
from datetime import datetime

def add():
    form = Toplevel(window)
    form.title("Add event")
    form.geometry("400x300")

    Label(form, text="ID sự kiện: ").grid(row=0, column=0, padx=10, pady=5, sticky=W)
    entry_ID = Entry(form)
    entry_ID.grid(row=0, column=1)

    Label(form, text="Tên sự kiện: ").grid(row=1, column=0, padx=10, pady=5, sticky=W)
    entry_name = Entry(form)
    entry_name.grid(row=1, column=1)

    Label(form, text="Ngày diễn ra: ").grid(row=2, column=0, padx=10, pady=5, sticky=W)
    entry_date = DateEntry(form, date_pattern="dd/mm/yyyy")
    entry_date.grid(row=2, column=1)

    Label(form, text="Địa điểm: ").grid(row=3, column=0, padx=10, pady=5, sticky=W)
    entry_place = Entry(form)
    entry_place.grid(row=3, column=1)

    Label(form, text="Màu sắc: ").grid(row=4, column=0, padx=10, pady=5, sticky=W)
    color_preview = Label(form, text="       ", bg="white", relief="solid")
    color_preview.grid(row=4, column=1, sticky=W)

    def choose_color():
        color = colorchooser.askcolor()[1]
        if color:
            color_preview.config(bg=color)

    Button(form, text="Chọn màu", command=choose_color).grid(row=4, column=2, padx=5)

    def save():
        tree.insert("", END,
                    text=entry_ID.get(),
                    values=(entry_name.get(), entry_date.get(), entry_place.get(), color_preview.cget("bg")))
        messagebox.showinfo("Thành công", "Thêm sinh viên thành công!")
        form.destroy()

    Button(form, text="Save", command=save).grid(row=5, column=0, pady=20)
    Button(form, text="Cancel", command=form.destroy).grid(row=5, column=1, pady=20)

    form.grab_set()


def edit():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Warning", "Hãy chọn sự kiện cần sửa!")
        return
    
    item = tree.item(selected)
    old_id = item["text"]
    old_name, old_date, old_place, old_color = item["values"]

    form = Toplevel(window)
    form.title("Add event")
    form.geometry("400x300")

    Label(form, text="ID sự kiện: ").grid(row=0, column=0, padx=10, pady=5, sticky=W)
    entry_ID = Entry(form)
    entry_ID.insert(0, old_id)
    entry_ID.grid(row=0, column=1)

    Label(form, text="Tên sự kiện: ").grid(row=1, column=0, padx=10, pady=5, sticky=W)
    entry_name = Entry(form)
    entry_name.insert(0, old_name)
    entry_name.grid(row=1, column=1)

    Label(form, text="Ngày diễn ra: ").grid(row=2, column=0, padx=10, pady=5, sticky=W)
    entry_date = DateEntry(form, date_pattern="dd/mm/yyyy")
    entry_date.set_date(datetime.strptime(old_date, "%d/%m/%Y"))
    entry_date.grid(row=2, column=1)

    Label(form, text="Địa điểm: ").grid(row=3, column=0, padx=10, pady=5, sticky=W)
    entry_place = Entry(form)
    entry_place.insert(0, old_place)
    entry_place.grid(row=3, column=1)

    Label(form, text="Màu sắc: ").grid(row=4, column=0, padx=10, pady=5, sticky=W)
    color_preview = Label(form, text="       ", bg=old_color, relief="solid")
    color_preview.grid(row=4, column=1, sticky=W)

    def choose_color():
        color = colorchooser.askcolor()[1]
        if color:
            color_preview.config(bg=color)

    Button(form, text="Chọn màu", command=choose_color).grid(row=4, column=2, padx=5)

    def update():
        tree.item(selected,
                    text=entry_ID.get(),
                    values=(entry_name.get(), entry_date.get(), entry_place.get(), color_preview.cget("bg")))
        messagebox.showinfo("Thành công", "Cập nhật thành công!")
        form.destroy()

    Button(form, text="Save", command=update).grid(row=5, column=0, pady=20)
    Button(form, text="Cancel", command=form.destroy).grid(row=5, column=1, pady=20)

    form.grab_set()

def delete():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Warning", "Hãy chọn sự kiện cần sửa!")
        return
    
    if messagebox.askyesno("Xác nhận", "Bạn chắc chắn muốn xoá sự kiện này?"):
        tree.delete(selected)
        messagebox.showinfo("Thông báo", "Đã xoá thành công!")


window = Tk()
window.title("Event Manager")
window.geometry("800x500")

tree = ttk.Treeview(window)

tree["columns"] = ["Tên sự kiện", "Ngày diễn ra", "Địa điểm", "Màu sắc"]

tree.column("#0", width=100, minwidth=100, stretch=False)
tree.column("Tên sự kiện", width=150, minwidth=150, stretch=False)
tree.column("Ngày diễn ra", width=100, minwidth=100, stretch=False)
tree.column("Địa điểm", width=120, minwidth=120, stretch=False)
tree.column("Màu sắc", width=80, minwidth=80, stretch=False)

tree.heading("#0", text="ID sự kiện", anchor=W)
tree.heading("Tên sự kiện", text="Tên sự kiện", anchor=W)
tree.heading("Ngày diễn ra", text="Ngày diễn ra", anchor=W)
tree.heading("Địa điểm", text="Địa điểm", anchor=W)
tree.heading("Màu sắc", text="Màu sắc", anchor=W)

scroll = Scrollbar(window, orient=VERTICAL, command=tree.yview)
tree.config(yscrollcommand=scroll.set)

tree.pack(side=LEFT, fill=BOTH, expand=True)
scroll.pack(side=RIGHT, fill=Y)

menubar = Menu(window)
window.config(menu=menubar)

event_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Event", menu=event_menu)

event_menu.add_command(label="Add event", command=add)
event_menu.add_command(label="Edit event", command=edit)
event_menu.add_command(label="Delete event", command=delete)
event_menu.add_separator()
event_menu.add_command(label="Quit", command=quit)

window.mainloop()
