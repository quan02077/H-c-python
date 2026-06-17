import tkinter as tk
from tkinter import ttk
root = tk.Tk()
root.title("Ví dụ TreeView")
# Tạo TreeView
tree = ttk.Treeview(root)
tree["columns"] = ("Name", "Age")
# Đặt tên cho các cột
tree.column("#0", width=100, minwidth=100, stretch=tk.NO)
tree.column("Name", width=100, minwidth=100,
stretch=tk.NO)
tree.column("Age", width=100, minwidth=100, stretch=tk.NO)
# Thêm tiêu đề cho các cột
tree.heading("#0", text="ID", anchor=tk.W)
tree.heading("Name", text="Name", anchor=tk.W)
tree.heading("Age", text="Age", anchor=tk.W)
tree.insert("", "end", text="1", values=("John Doe",
"30"))
tree.insert("", "end", text="2", values=("Jane Smith",
"25"))
tree.insert("", "end", text="3", values=("Bob Johnson",
"35"))
tree.pack()
root.mainloop()