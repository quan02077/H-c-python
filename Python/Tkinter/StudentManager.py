from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
from tkinter import messagebox
from datetime import datetime

def add():
    form = Toplevel(window)
    form.title("Thêm sinh viên")
    form.geometry("400x380")

    Label(form, text="Mã SV:").grid(row=0, column=0, padx=10, pady=5, sticky=W)
    entry_masv = Entry(form)
    entry_masv.grid(row=0, column=1, pady=5)

    Label(form, text="Họ tên:").grid(row=1, column=0, padx=10, pady=5, sticky=W)
    entry_hoten = Entry(form, width=30)
    entry_hoten.grid(row=1, column=1, pady=5)

    Label(form, text="Tuổi:").grid(row=2, column=0, padx=10, pady=5, sticky=W)
    entry_tuoi = Entry(form)
    entry_tuoi.grid(row=2, column=1, pady=5)

    Label(form, text="Giới tính:").grid(row=3, column=0, padx=10, pady=5, sticky=W)
    gioitinh_var = StringVar(value="Nam")
    Radiobutton(form, text="Nam", variable=gioitinh_var, value="Nam").grid(row=3, column=1, sticky=W)
    Radiobutton(form, text="Nữ", variable=gioitinh_var, value="Nữ").grid(row=3, column=1, sticky=E)

    Label(form, text="Lớp:").grid(row=4, column=0, padx=10, pady=5, sticky=W)
    entry_lop = Entry(form)
    entry_lop.grid(row=4, column=1, pady=5)

    Label(form, text="Ngày sinh:").grid(row=5, column=0, padx=10, pady=5, sticky=W)
    entry_ngaysinh = DateEntry(form, date_pattern="dd/mm/yyyy")
    entry_ngaysinh.grid(row=5, column=1, pady=5)

    Label(form, text="Điểm TB:").grid(row=6, column=0, padx=10, pady=5, sticky=W)
    entry_dtb = Entry(form)
    entry_dtb.grid(row=6, column=1, pady=5)

    def save_student():
        if validate(entry_hoten.get(), entry_tuoi.get(), gioitinh_var.get(),
                    entry_lop.get(), entry_ngaysinh.get(), entry_dtb.get()):

            tree.insert("", "end",
                        text=entry_masv.get(),
                        values=(entry_hoten.get(), entry_tuoi.get(), gioitinh_var.get(),
                                entry_lop.get(), entry_ngaysinh.get(), entry_dtb.get()))

            messagebox.showinfo("Thành công", "Thêm sinh viên thành công!")
            form.destroy()

    Button(form, text="Lưu", command=save_student).grid(row=7, column=0, pady=15)
    Button(form, text="Hủy", command=form.destroy).grid(row=7, column=1, pady=15)
    form.grab_set()

def edit():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Thông báo", "Vui lòng chọn sinh viên cần sửa!")
        return
    
    item = tree.item(selected)
    masv = item["text"]
    hoten, tuoi, gioitinh, lop, ngaysinh, dtb = item["values"]

    form = Toplevel(window)
    form.title("Sửa thông tin sinh viên")
    form.geometry("300x380")

    Label(form, text="Mã SV:").grid(row=0, column=0, padx=10, pady=5, sticky=W)
    entry_masv = Entry(form)
    entry_masv.insert(0, masv)
    entry_masv.grid(row=0, column=1)

    Label(form, text="Họ tên:").grid(row=1, column=0, padx=10, pady=5, sticky=W)
    entry_hoten = Entry(form, width=30)
    entry_hoten.insert(0, hoten)
    entry_hoten.grid(row=1, column=1)

    Label(form, text="Tuổi:").grid(row=2, column=0, padx=10, pady=5, sticky=W)
    entry_tuoi = Entry(form)
    entry_tuoi.insert(0, tuoi)
    entry_tuoi.grid(row=2, column=1)

    Label(form, text="Giới tính:").grid(row=3, column=0, padx=10, pady=5, sticky=W)
    gioitinh_var = StringVar(value=gioitinh)
    Radiobutton(form, text="Nam", variable=gioitinh_var, value="Nam").grid(row=3, column=1, sticky=W)
    Radiobutton(form, text="Nữ", variable=gioitinh_var, value="Nữ").grid(row=3, column=1, sticky=E)

    Label(form, text="Lớp:").grid(row=4, column=0, padx=10, pady=5, sticky=W)
    entry_lop = Entry(form)
    entry_lop.insert(0, lop)
    entry_lop.grid(row=4, column=1)

    Label(form, text="Ngày sinh:").grid(row=5, column=0, padx=10, pady=5, sticky=W)
    entry_ngaysinh = DateEntry(form, date_pattern="dd/mm/yyyy")
    entry_ngaysinh.set_date(ngaysinh)
    entry_ngaysinh.grid(row=5, column=1)

    Label(form, text="Điểm TB:").grid(row=6, column=0, padx=10, pady=5, sticky=W)
    entry_dtb = Entry(form)
    entry_dtb.insert(0, dtb)
    entry_dtb.grid(row=6, column=1)

    def update_student():
        if validate(entry_hoten.get(), entry_tuoi.get(), gioitinh_var.get(),
                    entry_lop.get(), entry_ngaysinh.get(), entry_dtb.get()):

            tree.item(selected, text=entry_masv.get(),
                      values=(entry_hoten.get(), entry_tuoi.get(), gioitinh_var.get(),
                              entry_lop.get(), entry_ngaysinh.get(), entry_dtb.get()))

            messagebox.showinfo("Thành công", "Cập nhật thành công!")
            form.destroy()

    Button(form, text="Cập nhật", command=update_student).grid(row=7, column=0, pady=15)
    Button(form, text="Hủy", command=form.destroy).grid(row=7, column=1, pady=15)
    form.grab_set()

def delete():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Thông báo", "Vui lòng chọn sinh viên để xoá!")
        return
    
    if messagebox.askyesno("Xác nhận", "Bạn chắc chắn muốn xoá sinh viên này?"):
        tree.delete(selected)
        messagebox.showinfo("Thông báo", "Đã xoá thành công!")

def validate(name, age, gender, lop, birthday, gpa):
    if name.strip() == "":
        messagebox.showwarning("Lỗi", "Họ tên không được để trống!")
        return False

    if not age.isdigit() or int(age) <= 0:
        messagebox.showwarning("Lỗi", "Tuổi phải là số nguyên dương!")
        return False

    if gender not in ["Nam", "Nữ"]:
        messagebox.showwarning("Lỗi", "Vui lòng chọn giới tính!")
        return False

    if lop.strip() == "":
        messagebox.showwarning("Lỗi", "Lớp không được để trống!")
        return False

    try:
        birthday_date = datetime.strptime(birthday, "%d/%m/%Y")
        if birthday_date > datetime.today():
            messagebox.showwarning("Lỗi", "Ngày sinh không được lớn hơn ngày hiện tại!")
            return False
    except:
        messagebox.showwarning("Lỗi", "Ngày sinh không hợp lệ!")
        return False

    try:
        score = float(gpa)
        if not (0 <= score <= 10):
            raise ValueError
    except:
        messagebox.showwarning("Lỗi", "Điểm TB phải là số từ 0 đến 10!")
        return False

    return True


window = Tk()
window.geometry("800x500")
window.title("Student Manager")

tree = ttk.Treeview(window)
tree["columns"] = ["Họ tên", "Tuổi", "Giới tính", "Lớp", "Ngày sinh", "Điểm TB"]

tree.column("#0", width=100, minwidth=100)
tree.column("Họ tên", width=120, minwidth=120)
tree.column("Tuổi", width=60, minwidth=60)
tree.column("Giới tính", width=80, minwidth=80)
tree.column("Lớp", width=80, minwidth=80)
tree.column("Ngày sinh", width=100, minwidth=100)
tree.column("Điểm TB", width=80, minwidth=80)

tree.heading("#0", text="Mã SV", anchor=W)
tree.heading("Họ tên", text="Họ tên", anchor=W)
tree.heading("Tuổi", text="Tuổi", anchor=W)
tree.heading("Giới tính", text="Giới tính", anchor=W)
tree.heading("Lớp", text="Lớp", anchor=W)
tree.heading("Ngày sinh", text="Ngày sinh", anchor=W)
tree.heading("Điểm TB", text="Điểm TB", anchor=W)

scroll = Scrollbar(window, orient=VERTICAL, command=tree.yview)
tree.configure(yscrollcommand=scroll.set)

tree.pack(side=LEFT, fill=BOTH, expand=True)
scroll.pack(side=RIGHT, fill=Y)

menubar = Menu(window)
window.config(menu=menubar)
action_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Action", menu=action_menu)
action_menu.add_command(label="Add", command=add)
action_menu.add_command(label="Edit", command=edit)
action_menu.add_command(label="Delete", command=delete)
action_menu.add_command(label="Exit", command=quit)

window.mainloop()
