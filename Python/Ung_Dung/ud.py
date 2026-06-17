# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk, messagebox
import json
import os

FILE_JSON = "dangky_hoithao.json"

# ------------------------------------------------------------
# HÀM XỬ LÝ CSV
# ------------------------------------------------------------
def save_to_csv(data):
    if os.path.isfile(FILE_JSON):
        with open(FILE_JSON, "r", encoding="utf-8") as f:
            ds = json.load(f)
    else:
        ds = []

    ds.append(data)

    with open(FILE_JSON, "w", encoding="utf-8") as f:
        json.dump(ds, f, ensure_ascii=False, indent=4)

def load_csv_to_tree(tree):
    if not os.path.isfile(FILE_JSON):
         return
    with open(FILE_JSON, "r", encoding="utf-8") as f:
        ds = json.load(f)

# ------------------------------------------------------------
# HÀM TÍNH BMI
# ------------------------------------------------------------
def tinh_bmi(weight, height_cm):
    h = height_cm / 100
    return round(weight / (h * h), 2)

def xep_loai_bmi(bmi):
    if bmi < 18.5: return "Gầy"
    if bmi < 25: return "Bình thường"
    if bmi < 30: return "Thừa cân"
    return "Béo phì"

# ------------------------------------------------------------
# TẠO GIAO DIỆN
# ------------------------------------------------------------
root = tk.Tk()
root.title("Ứng dụng đăng ký hội thảo")
root.geometry("900x550")

# ------------------------------------------------------------
# KHUNG NHẬP LIỆU
# ------------------------------------------------------------
frame = tk.LabelFrame(root, text="Thông tin sinh viên")
frame.pack(fill="x", padx=10, pady=10)

labels = ["MSSV", "Họ tên", "Năm sinh", "Cân nặng (kg)", "Chiều cao (cm)"]
entries = {}

for i, text in enumerate(labels):
    tk.Label(frame, text=text, font=("Arial", 10)).grid(row=i, column=0, padx=5, pady=5, sticky="w")
    entry = tk.Entry(frame, width=25)
    entry.grid(row=i, column=1, padx=5, pady=5)
    entries[text] = entry

# Combobox lớp
tk.Label(frame, text="Lớp").grid(row=0, column=2)
cb_lop = ttk.Combobox(frame, values=["15DHTH01", "15DHTH04", "15DHTH05", "15DHTH06"], width=20, state="readonly")
cb_lop.grid(row=0, column=3)

# Listbox môn học
tk.Label(frame, text="Môn đăng ký").grid(row=1, column=2)
list_mon = tk.Listbox(frame, selectmode="multiple", height=4)
for m in ["Bóng đá", "Cầu lông", "Bóng chuyền", "Bóng rổ"]:
    list_mon.insert(tk.END, m)
list_mon.grid(row=1, column=3)

# ------------------------------------------------------------
# TREEVIEW
# ------------------------------------------------------------
cols = ("MSSV", "Họ tên", "Năm sinh", "Cân nặng", "Chiều cao", "Lớp", "Môn", "BMI")
tree = ttk.Treeview(root, columns=cols, show="headings", height=12)
for col in cols:
    tree.heading(col, text=col)
    tree.column(col, width=110)

tree.pack(fill="both", padx=10, pady=10)

load_csv_to_tree(tree)

# ------------------------------------------------------------
# NÚT XỬ LÝ
# ------------------------------------------------------------
def them_sinh_vien():
    try:
        mssv = entries["MSSV"].get()
        hoten = entries["Họ tên"].get()
        namsinh = int(entries["Năm sinh"].get())
        cannang = float(entries["Cân nặng (kg)"].get())
        chieucao = float(entries["Chiều cao (cm)"].get())
        lop = cb_lop.get()
        mon_selected = [list_mon.get(i) for i in list_mon.curselection()]

        # Kiểm tra lỗi nhập
        if len(mssv) != 10 or not mssv.isdigit():
            messagebox.showerror("Lỗi", "MSSV phải là 8 chữ số!")
            return
        if cannang <= 0 or chieucao <= 0:
            messagebox.showerror("Lỗi", "Cân nặng và chiều cao phải > 0!")
            return
        if namsinh < 1980 or namsinh > 2023:
            messagebox.showerror("Lỗi", "Năm sinh không hợp lệ!")
            return
        if not lop:
            messagebox.showerror("Lỗi", "Chưa chọn lớp!")
            return
        if not mon_selected:
            messagebox.showerror("Lỗi", "Chưa chọn môn đăng ký!")
            return

        bmi = tinh_bmi(cannang, chieucao)

        row = [mssv, hoten, namsinh, cannang, chieucao, lop, "; ".join(mon_selected), bmi]

        tree.insert("", tk.END, values=row)
        save_to_csv(row)

        messagebox.showinfo("Thành công", f"Thêm sinh viên thành công!\nBMI = {bmi} ({xep_loai_bmi(bmi)})")

    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập đúng định dạng số!")

def xoa_sinh_vien():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Chú ý", "Chưa chọn sinh viên để xoá!")
        return
    tree.delete(selected)

def sap_xep_theo_mssv():
    items = list(tree.get_children())
    rows = []
    for item in items:
        rows.append(tree.item(item)["values"])
    rows.sort(key=lambda x: x[0])
    for item in items:
        tree.delete(item)
    for r in rows:
        tree.insert("", tk.END, values=r)

def reset():
    for entry in entries.values():
        entry.delete(0, tk.END)
    cb_lop.set('')
    list_mon.selection_clear(0, tk.END)

btn_frame = tk.Frame(root)
btn_frame.pack()

tk.Button(btn_frame, text="Thêm", width=12, command=them_sinh_vien).grid(row=0, column=0, padx=10, pady=5)
tk.Button(btn_frame, text="Xoá", width=12, command=xoa_sinh_vien).grid(row=0, column=1, padx=10, pady=5)
tk.Button(btn_frame, text="Sắp xếp MSSV", width=15, command=sap_xep_theo_mssv).grid(row=0, column=2, padx=10, pady=5)
tk.Button(btn_frame, text="Reset", width=15, command=reset).grid(row=0, column=3, padx=10, pady=5)

root.mainloop()
