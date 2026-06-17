# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import messagebox, ttk
import os
from PIL import Image, ImageTk
from user_data import load_data, save_data
from datetime import datetime
from tkcalendar import DateEntry
from bs4 import BeautifulSoup
import requests
import random
from tkvideo import tkvideo

class ToDoApp:
    def __init__(self, root, username, email, password):
        self.root = root
        self.username = username
        self.email = email
        self.password = password

        self.win = tk.Toplevel(self.root)
        self.win.title("Focus")
        self.win.state("zoomed")
        self.win.configure(bg="#F1F3E0")

        if os.path.isfile("logo.jpg"):
            self.photo = Image.open("logo.jpg")
            self.logo = ImageTk.PhotoImage(self.photo)
            self.win.iconphoto(False, self.logo)

        if os.path.isfile("cr7.jpg"):
            self.cr7 = Image.open("cr7.jpg")
            self.cr7_resize = self.cr7.resize((48,48))
            self.cr7_cry = ImageTk.PhotoImage(self.cr7_resize)

        if os.path.isfile("messi.jpg"):
            self.messi = Image.open("messi.jpg")
            self.messi_resize = self.messi.resize((48,48))
            self.messi_cry = ImageTk.PhotoImage(self.messi_resize) 

        # Tên app
        self.label_frame = tk.Frame(self.win, bg="#F1F3E0")
        self.label_frame.pack(fill= "x", pady=10)

        self.label_frame.columnconfigure(0, weight=1)
        self.label_frame.columnconfigure(1, weight=1)
        self.label_frame.columnconfigure(2, weight=1)

        self.app_name_label = tk.Label(self.label_frame, text="Focus",bg="#F1F3E0", image=self.cr7_cry, compound= "right",
                                       font=("TechnicBold", 40, "bold"))
        self.app_name_label.grid(row=0, column=0, sticky="w", pady=10)

        hour = datetime.now().hour

        if hour < 12:
            loi_chao = "Chào buổi sáng"
        elif hour < 18:
            loi_chao = "Chào buổi chiều"
        else:
            loi_chao = "Chào buổi tối"

        self.username_label = tk.Label(self.label_frame, text= f"{loi_chao} người anh em", bg="#F1F3E0", font=("Arial", 14, "bold"))
        self.username_label.grid(row=0, column=1, padx=10)

        self.logout_btn = tk.Button(self.label_frame, text="Đăng xuất",bg="#ff5757", fg= "white", image=self.messi_cry, compound= "left",
                                    font=("Arial", 10, "bold"),
                                    command=self.logout)
        self.logout_btn.grid(row=0, column=3, sticky="e", padx=10)

        self.calen = tk.LabelFrame(self.label_frame, text= "Lịch", bg="#F1F3E0", font=("Arial", 12, "bold"))
        self.calen.grid(row=0, column=0, sticky= "n", padx=140, pady=30)

        DateEntry(self.calen, font=("Arial", 12, "bold"), width=12, borderwidth=2).pack(padx=10, pady=10)

        self.tools = Tools(self.win, self.username, self.email, self.password)

        self.quote = Quote(self.win)

        self.note = Note(self.win, self.username)

    def logout(self):
        self.win.destroy()
        self.root.deiconify()

class Tools:
    def __init__(self, parent, username, email, password):
        self.parent = parent
        self.username = username
        self.email = email
        self.password = password

        self.main_area = tk.Frame(self.parent, bg="#F1F3E0")
        self.main_area.pack(fill="both", expand=True)

        self.left_panel = tk.Frame(self.main_area, bg="#F1F3E0")
        self.left_panel.pack(side="left", padx=10, pady=10)

        self.center_panel = tk.Frame(self.main_area, bg="#F1F3E0")
        self.center_panel.pack(side="left", expand=True, padx=10, pady=10)

        self.frame_tools = tk.LabelFrame(self.left_panel, text="Công cụ", bg="#F1F3E0", font=("Arial", 10, "bold"),padx=10, pady=10)
        self.frame_tools.pack(anchor= "w", padx=10, pady=10)
        
        tk.Button(self.frame_tools, text="Thêm", bg="#328E6E", fg= "white", font=("Arial", 10, "bold"), width= 30,
                  command=self.add_task).pack(fill="x", pady=4)
        tk.Button(self.frame_tools, text="Cập nhật", bg="#328E6E", fg= "white", font=("Arial", 10, "bold"), width= 30, 
                  command=self.update_task).pack(fill="x", pady=4)
        tk.Button(self.frame_tools, text="Xóa", bg="#328E6E", fg= "white", font=("Arial", 10, "bold"), width= 30, 
                  command=self.delete_task).pack(fill="x", pady=4)
        tk.Button(self.frame_tools, text="Tìm kiếm", bg="#328E6E", fg= "white", font=("Arial", 10, "bold"), width= 30, 
                  command=self.search_task).pack(fill="x", pady=4)
        tk.Button(self.frame_tools, text="Sắp xếp theo độ ưu tiên", bg="#328E6E", fg= "white", font=("Arial", 10, "bold"), width= 30, 
                  command=self.sort_task_priority).pack(fill="x", pady=4) 
        tk.Button(self.frame_tools, text="Sắp xếp theo ngày hết hạn", bg="#328E6E", fg= "white", font=("Arial", 10, "bold"), width= 30, 
                  command=self.sort_task_deadline).pack(fill="x", pady=4)
        tk.Button(self.frame_tools, text="Reset", bg="#328E6E", fg= "white", font=("Arial", 10, "bold"), width= 30,
                  command=self.reset_task).pack(fill="x", pady=4)
        tk.Button(self.frame_tools, text="Xem thông tin người dùng", bg="#328E6E", fg= "white", font=("Arial", 10, "bold"), width= 30,
                  command=self.show_info).pack(fill="x", pady=4)
        tk.Button(self.frame_tools, text="Sửa thông tin người dùng", bg="#328E6E", fg= "white", font=("Arial", 10, "bold"), width= 30,
                  command=self.edit_info).pack(fill="x", pady=4)

        self.checkboxes = CheckBoxes(self.center_panel, self.username)   

    def add_task(self):
        self.add = tk.Toplevel(self.parent)
        self.add.title("Thêm công việc")
        self.add.configure(bg="#F1F3E0")
        self.add.geometry("500x250")
        self.add.attributes("-topmost", True)

        if os.path.isfile("logo.jpg"):
            self.photo = Image.open("logo.jpg")
            self.logo = ImageTk.PhotoImage(self.photo)
            self.add.iconphoto(False, self.logo)
            
        self.add_form = tk.Frame(self.add, bg="#F1F3E0")
        self.add_form.pack(pady=20)

        tk.Label(self.add_form, text="Công việc", bg="#F1F3E0", font=("Arial", 12, "bold")).grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.entry_task = tk.Entry(self.add_form, width=30)
        self.entry_task.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.add_form, text="Mức độ ưu tiên", bg="#F1F3E0", font=("Arial", 12, "bold")).grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.priority = ttk.Combobox(self.add_form, values=["Cao", "Trung bình", "Thấp"], width=28)
        self.priority.grid(row=1, column=1, padx=5, pady=5)
        tk.Label(self.add_form, text="Ngày hết hạn", bg="#F1F3E0", font=("Arial", 12, "bold")).grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.deadline_task = DateEntry(self.add_form, width=27, date_pattern="dd/mm/yyyy", mindate=datetime.now())
        self.deadline_task.grid(row=2, column=1, padx=5, pady=5)

        self.add.bind("<Return>", lambda event: self.add_save())

        tk.Button(self.add, text= "Lưu", bg="#ff5757", fg= "white",
            command=self.add_save, font=("Arial", 10, "bold")).pack(pady=10)
    
    def add_save(self):
        task = self.entry_task.get().strip()
        priority = self.priority.get()
        deadline = self.deadline_task.get()

        today = datetime.now().strftime("%d/%m/%Y")
        d1 = datetime.strptime(deadline, "%d/%m/%Y")
        d2 = datetime.strptime(today, "%d/%m/%Y")

        if d1 < d2:
            messagebox.showerror("Lỗi", "Ngày hết hạn không được trước ngày hôm nay!")
            return

        if task == "" or priority == "":
            messagebox.showerror("Lỗi", "Vui lòng điền công việc và độ ưu tiên!")
            return

        users = load_data()
        found = False

        tasks_data = {"task": task, "priority": priority, "deadline": deadline, "done": 0}
    
        for user in users:
            if user["info"] == self.username:
                if "tasks" not in user:
                    user["tasks"] = []
                user["tasks"].append(tasks_data)
                found = True
                break

        if not found:
            users.append({
                "info": self.username,
                "email": self.email,
                "password": self.password,
                "tasks": [tasks_data]
            })

        save_data(users)
        self.checkboxes.load_task()

        messagebox.showinfo("Thông báo", "Thêm công việc thành công!")
        self.entry_task.delete(0, tk.END)
        self.priority.set(" ")
        self.deadline_task.delete(0, tk.END)
        self.deadline_task.insert(0, datetime.now().strftime("%d/%m/%Y"))

    def update_task(self):
        self.update = tk.Toplevel(self.parent)
        self.update.title("Sửa công việc")
        self.update.configure(bg="#F1F3E0")
        self.update.geometry("400x300")
        self.update.attributes("-topmost", True)

        if os.path.isfile("logo.jpg"):
            self.photo = Image.open("logo.jpg")
            self.logo = ImageTk.PhotoImage(self.photo)
            self.update.iconphoto(False, self.logo)

        self.update_form = tk.Frame(self.update, bg="#F1F3E0")
        self.update_form.pack(pady=20)

        tk.Label( self.update_form, text="Tên công việc cũ", bg="#F1F3E0", font=("Arial", 12, "bold")).grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.old_name = tk.Entry( self.update_form, width=30)
        self.old_name.grid(row=0, column=1, padx=5, pady=5)


        tk.Label( self.update_form, text="Tên công việc mới", bg="#F1F3E0", font=("Arial", 12, "bold")).grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.new_name = tk.Entry( self.update_form, width=30)
        self.new_name.grid(row=1, column=1, padx=5, pady=5)

        tk.Label( self.update_form, text="Ưu tiên mới", bg="#F1F3E0", font=("Arial", 12, "bold")).grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.new_priority = ttk.Combobox( self.update_form, values=["Cao", "Trung bình", "Thấp"], width=28)
        self.new_priority.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(self.update_form, text="Ngày hết hạn", bg="#F1F3E0", font=("Arial", 12, "bold")).grid(row=3, column=0, sticky="w", padx=5, pady=5)
        self.new_deadline = DateEntry(self.update_form, width=27, date_pattern="dd/mm/yyyy", mindate=datetime.now())
        self.new_deadline.grid(row=3, column=1, padx=5, pady=5)

        tk.Button(self.update, text="Cập nhật", bg="#ff5757", fg= "white",font=("Arial", 10, "bold"),
                command=self.update_save).pack(pady=10)
        
        self.update.bind("<Return>", lambda event: self.update_save())

    def update_save(self):
        old_task = self.old_name.get().strip()
        new_task = self.new_name.get().strip()
        new_pri = self.new_priority.get()
        new_deadline = self.new_deadline.get()

        if old_task == "" or new_task == "" or new_pri == "":
            messagebox.showerror("Lỗi", "Vui lòng điền đủ thông tin!")

    
        users = load_data()
        found = False
        for user in users:
            if user["info"] == self.username:
                for task in user.get("tasks", []):
                    if isinstance(task, dict) and task.get("task").lower() == old_task.lower():
                        task["task"] = new_task
                        task["priority"] = new_pri
                        task["deadline"] = new_deadline
                        found = True
                        break
                break
        if found:
            save_data(users)
            messagebox.showinfo("Thông báo", "Cập nhật thành công!")
            self.old_name.delete(0, tk.END)
            self.new_name.delete(0,tk.END)
            self.new_priority.set("")
            self.new_deadline.delete(0, tk.END)
            self.new_deadline.insert(0, datetime.now().strftime("%d/%m/%Y"))
            self.checkboxes.load_task()
        else:
            messagebox.showerror("Lỗi", "Không tìm thấy công việc cần sửa!")

    def delete_task(self):
        self.delete = tk.Toplevel(self.parent)
        self.delete.title("Xóa công việc")
        self.delete.configure(bg="#F1F3E0")
        self.delete.geometry("250x100")
        self.delete.attributes("-topmost", True)

        if os.path.isfile("logo.jpg"):
            self.photo = Image.open("logo.jpg")
            self.logo = ImageTk.PhotoImage(self.photo)
            self.delete.iconphoto(False, self.logo)
        
        tk.Label(self.delete, text="Tên công việc cần xóa", bg="#F1F3E0", font=("Arial", 12, "bold")).pack(pady= 5)
        self.name_task = tk.Entry(self.delete, width=30)
        self.name_task.pack()

        tk.Button(self.delete, text="Xóa", bg="#ff5757", font=("Arial", 10, "bold"), fg= "white",
                command=self.delete_save).pack(pady=10)
        
        self.delete.bind("<Return>", lambda event: self.delete_save())

    def delete_save(self):
        name_task = self.name_task.get().strip()

        if name_task == "":
            messagebox.showerror("Lỗi", "Vui lòng điền thông tin!")

        users = load_data()
        found = False
        new_tasks = []
        for user in users:
            if user["info"] == self.username:
                for task in user.get("tasks", []):
                    if isinstance(task, dict) and task.get("task").lower() == name_task.lower():
                        found= True
                        continue
                    new_tasks.append(task)        
                user["tasks"] = new_tasks
                break
        if found:
            save_data(users)
            messagebox.showinfo("Thông báo", "Đã xóa thành công!")
            self.name_task.delete(0, tk.END)
            self.checkboxes.load_task()
        else:
            messagebox.showerror("Lỗi", "Không tìm thấy công việc!")

    def search_task(self):
        self.search = tk.Toplevel(self.parent)
        self.search.title("Tìm kiếm công việc")
        self.search.configure(bg="#F1F3E0")
        self.search.geometry("250x100")
        self.search.attributes("-topmost", True)

        if os.path.isfile("logo.jpg"):
            self.photo = Image.open("logo.jpg")
            self.logo = ImageTk.PhotoImage(self.photo)
            self.search.iconphoto(False, self.logo)

        self.deadline = DateEntry(self.search, width=27, date_pattern="dd/mm/yyyy", mindate=datetime.now())
        self.deadline.pack(pady=10)

        tk.Button(self.search, text="Tìm kiếm", bg="#ff5757", font=("Arial", 10, "bold"), fg= "white",
                command=self.searched).pack(pady=10)
        
        self.search.bind("<Return>", lambda event: self.searched())

    def searched(self):
        task_deadline = self.deadline.get()

        if task_deadline == "":
            messagebox.showerror("Lỗi", "Vui lòng điền thông tin!")

        users = load_data()
        found = False
        found_tasks = []

        for user in users:
            if user["info"] == self.username:
                for task in user.get("tasks", []):
                    if isinstance(task, dict) and task.get("deadline") == task_deadline:
                        found_tasks.append(task.get("task"))
                        found = True
                break
        
        if found:
            tasks_str = "\n".join(found_tasks)
            messagebox.showinfo("Thông báo", f"Các công việc vào ngày {task_deadline}:\n{tasks_str}")
            self.search.destroy()
        else:
            messagebox.showerror("Lỗi", "Không tìm thấy công việc!")

    def sort_task_priority(self):  
        users = load_data()
        for user in users:
            if user["info"] == self.username:
                tasks = user.get("tasks", [])
                priority_list = {"Cao": 1, "Trung bình": 2, "Thấp": 3}
                user["tasks"] = sorted(tasks, key= lambda t: priority_list.get(t.get("priority", ""), 4))
                break
        save_data(users)
        self.checkboxes.load_task()
        messagebox.showinfo("Thông báo", "Sắp xếp công việc thành công")

    def sort_task_deadline(self):
        users = load_data()
        for user in users:
            if user["info"] == self.username:
                tasks = user.get("tasks", [])
                user["tasks"] = sorted(tasks, key=lambda t: datetime.strptime(t.get("deadline", "31/12/9999"), "%d/%m/%Y"))
                break
        save_data(users)
        self.checkboxes.load_task()
        messagebox.showinfo("Thông báo", "Sắp xếp công việc theo ngày hết hạn thành công")


    def reset_task(self):
        self.checkboxes.reset_all()

    def show_info(self):
        self.show = tk.Toplevel(self.parent)
        self.show.title("Thông tin người dùng")
        self.show.configure(bg="#F1F3E0")
        self.show.geometry("250x100")
        self.show.attributes("-topmost", True)

        if os.path.isfile("logo.jpg"):
            self.photo = Image.open("logo.jpg")
            self.logo = ImageTk.PhotoImage(self.photo)
            self.show.iconphoto(False, self.logo)

        users = load_data()

        for user in users:
            if user["info"] == self.username:
                text = text = f"{user['info']} - {user['email']}"
                self.info_label = tk.Label(self.show, text= text, font=("Arial", 12, "bold"), bg="#F1F3E0", wraplength=200)
                self.info_label.pack(fill="x", padx=10, pady=5)
            break

    def edit_info(self):
        self.edit = tk.Toplevel(self.parent)
        self.edit.title("Sửa thông tin người dùng")
        self.edit.configure(bg="#F1F3E0")
        self.edit.geometry("400x250")
        self.edit.attributes("-topmost", True)

        if os.path.isfile("logo.jpg"):
            self.photo = Image.open("logo.jpg")
            self.logo = ImageTk.PhotoImage(self.photo)
            self.edit.iconphoto(False, self.logo)

        self.edit_frame = tk.Frame(self.edit, bg="#F1F3E0")
        self.edit_frame.pack(pady= 20)

        tk.Label( self.edit_frame, text="Tên đăng nhập cũ", bg="#F1F3E0", font=("Arial", 12, "bold")).grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.old_name_info = tk.Entry( self.edit_frame, width=30)
        self.old_name_info.grid(row=0, column=1, padx=5, pady=5)

        tk.Label( self.edit_frame, text="Tên đăng nhập mới", bg="#F1F3E0", font=("Arial", 12, "bold")).grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.new_name_info = tk.Entry( self.edit_frame, width=30)
        self.new_name_info.grid(row=1, column=1, padx=5, pady=5)

        tk.Label( self.edit_frame, text="Email", bg="#F1F3E0", font=("Arial", 12, "bold")).grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.new_email = tk.Entry( self.edit_frame, width=30)
        self.new_email.grid(row=2, column=1, padx=5, pady=5)

        tk.Label( self.edit_frame, text="Password", bg="#F1F3E0", font=("Arial", 12, "bold")).grid(row=3, column=0, sticky="w", padx=5, pady=5)
        self.new_pass = tk.Entry( self.edit_frame, width=30)
        self.new_pass.grid(row=3, column=1, padx=5, pady=5)

        tk.Button(self.edit, text="Cập nhật", bg="#ff5757", font=("Arial", 10, "bold"), fg= "white",
                command=self.edit_save).pack(pady=10)

        self.edit.bind("<Return>", lambda event: self.edit_save())

    def edit_save(self):
        self.old_username = self.old_name_info.get().strip()
        self.new_username = self.new_name_info.get().strip()
        self.email = self.new_email.get().strip()
        self.pw = self.new_pass.get().strip()

        users = load_data()
        found = False
        for user in users:
            if user["info"] == self.old_username:
                user["info"] = self.new_username
                user["email"] = self.email
                user["password"] = self.pw
                found = True
                break
        if found:
            save_data(users)
            messagebox.showinfo("Thông báo", "Cập nhật thông tin người dùng thành công")
            self.old_name_info.delete(0, tk.END)
            self.new_name_info.delete(0, tk.END)
            self.new_email.delete(0, tk.END)
            self.new_pass.delete(0, tk.END)
            self.edit.destroy()
        else:
             messagebox.showerror("Lỗi", "Không tìm thấy người dùng")

class CheckBoxes:
    def __init__(self, parent, username):
        self.parent = parent
        self.username = username
        self.vars = []
        self.frame_checkboxes = tk.LabelFrame(self.parent, text= "Danh sách việc làm",
                                        bg="#F1F3E0", font=("Arial", 10, "bold"),padx=10, pady=10)
        self.frame_checkboxes.pack(anchor= "nw")

        self.checkbox_area = tk.Frame(self.frame_checkboxes, bg="#F1F3E0")
        self.checkbox_area.pack(pady=10)

        self.progress = Progress(self.parent, self.vars, self.username)
        self.load_task()

    def load_task(self):
        for x, check in self.vars:
            check.destroy()
        self.vars.clear()

        users = load_data()

        for user in users:
            if user["info"] == self.username:
                tasks = user.get("tasks", [])
                for task in tasks:
                    if isinstance(task, dict):
                        name = task.get("task", "")
                        priority = task.get("priority", "")
                        deadline = task.get("deadline", "")
                        done = task.get("done", 0)
                    else:
                        name = task
                        priority = "Không rõ" 
                        deadline = ""
                        done = 0
                    self.tasks_list(name, priority,deadline, done)
                break
        self.progress.update_progress()

    def tasks_list(self, task, priority, deadline="", done = 0):
        text = f"{task} ({priority})"
        if deadline:
            text += f" – Hết hạn: {deadline}"

        x = tk.IntVar(value= done)
        index = len(self.vars)
        row = index % 7
        col = index // 7

        check = tk.Checkbutton(
                self.checkbox_area,
                text=text,
                variable=x,
                font=("Arial", 12, "bold"),
                bg="#F1F3E0",
                command=lambda v=x, dl=deadline, nm=task: self.progress.update_progress(v, dl, nm)
            )

        check.grid(row=row, column=col, sticky="w")
        self.vars.append((x, check))

    def reset_all(self):
        if not messagebox.askyesno("Xác nhận", "Bạn có chắc muốn xóa toàn bộ công việc!"):
            return
        
        users = load_data()
        for user in users:
            if user["info"] == self.username:
                user["tasks"] = []
                break
        save_data(users)
        self.load_task()

        messagebox.showinfo("Thông báo", "Đã xóa toàn bộ công việc!")

class Progress:
    def __init__(self, parent, vars_list, username):
        self.parent = parent        
        self.vars = vars_list
        self.username = username
        self.frame_progress = tk.LabelFrame(parent, text="Tiến độ",
                                            bg="#F1F3E0", font=("Arial", 10, "bold"), padx=10, pady=10)
        self.frame_progress.pack(side="left", pady=30)

        self.progress = ttk.Progressbar(self.frame_progress, length=300, mode="determinate")
        self.progress.pack(side="left", padx=5)

        self.label_percent = tk.Label(self.frame_progress, text="0%", bg="#F1F3E0", font=("Arial", 12, "bold"))
        self.label_percent.pack(side="left", padx=5)

    def update_progress(self, var_clicked=None, deadline=None, task_name=None):
        if deadline and var_clicked and var_clicked.get() == 1:
            try:
                today = datetime.now().strftime("%d/%m/%Y")

                d1 = datetime.strptime(deadline, "%d/%m/%Y")
                d2 = datetime.strptime(today, "%d/%m/%Y")

                if d1 < d2:
                    messagebox.showwarning("Cảnh báo", f"Công việc '{task_name}' đã hết hạn!")
                    var_clicked.set(0)
            except ValueError as e:
                print("Lỗi định dạng ngày:", e)
                return
        users = load_data()
        for user in users:
            if user["info"] == self.username:
                for i, (var, _) in enumerate(self.vars):
                    if i < len(self.vars):
                        user["tasks"][i]["done"] = var.get()
                break
        save_data(users)

        if not self.vars:
            self.progress["value"] = 0
            self.label_percent.config(text="0%")
            return

        complete = sum(var.get() for var, _ in self.vars)
        total = len(self.vars)
        value = (complete / total) * 100
        self.progress["value"] = value

        # Cập nhật nhãn %
        self.label_percent.config(text=f"{int(value)}%")

        if value >= 100:

            self.frame_video = tk.Toplevel(self.parent)
            self.frame_video.title("Congratulation!")
            self.frame_video.geometry("460x250")

            if os.path.isfile("logo.jpg"):
                self.photo = Image.open("logo.jpg")
                self.logo = ImageTk.PhotoImage(self.photo)
                self.frame_video.iconphoto(False, self.logo)

            self.cong_label = tk.Label(self.frame_video, text= "Chúc mừng bạn đã hoàn thành tất cả công việc!", font=("Monospace", 14, "bold"),bg="#F1F3E0")
            self.cong_label.pack(side= "bottom")

            self.label_video = tk.Label(self.frame_video)
            self.label_video.pack()

            self.player = tkvideo("clap.mp4", self.label_video, loop=0, size=(480, 270))
            self.player.play()

            self.frame_video.after(1850, self.close_video)

    def close_video(self):
        self.frame_video.destroy()

class Calendar: 
    def __init__(self, parent):
        self.parent = parent
        self.calen = tk.LabelFrame(self.label_frame, text= "Lịch", bg="#F1F3E0", font=("Arial", 12, "bold"))
        self.calen.pack(anchor= "ne", padx= 20, pady= 30)

        DateEntry(self.calen, font=("Arial", 12, "bold"), width=12, borderwidth=2).pack(padx=10, pady=10)

class Quote:
    def __init__(self, parent):
        self.parent = parent
        self.quote = tk.LabelFrame(self.parent, text="Quote", bg="#F1F3E0",
                                   font=("Arial", 12, "bold"))
        self.quote.pack(side="left", fill="both", expand=True, padx=20, pady=10)

        self.url = "https://quotes.toscrape.com/"
        text = "Đang tải quote..."

        try:
            response = requests.get(self.url, timeout=5)
            soup = BeautifulSoup(response.text, "html.parser")

            quotes = soup.find_all("div", class_="quote")
            if quotes:
                chosen = random.choice(quotes)
                quote_text = chosen.find("span", class_="text")
                author_text = chosen.find("small", class_="author")

                if quote_text and author_text:
                    text = f"{quote_text.text.strip()} — {author_text.text.strip()}"
                else:
                    text = "Không tìm thấy nội dung quote!"
            else:
                text = "Không có quote nào trên trang!"
        except Exception as e:
            text = f"Lỗi khi tải quote: {e}"

        self.show_quote = tk.Label(
            self.quote,
            text=text,
            bg="#F1F3E0",
            fg="#123524",
            wraplength=400,
            justify="left",
            font=("Arial", 13, "bold")
        )
        self.show_quote.pack(padx=10, pady=10, fill= "x")

class Note:
    def __init__(self, parent, username):
        self.parent = parent
        self.username = username

        self.note_frame = tk.LabelFrame(self.parent, text="Ghi chú", bg="#F1F3E0",
                                        font=("Arial", 12, "bold"), padx=10, pady=10)
        self.note_frame.pack(side="left", fill="x", padx=20, pady=10)

        self.text_note = tk.Text(self.note_frame, height=5, font=("Arial", 11), wrap="word")
        self.text_note.pack(fill="both", expand=True)

        self.text_note.bind("<KeyRelease>", self.auto_save)

        self.load_note()

    def load_note(self):
        users = load_data()

        for user in users:
            if user["info"] == self.username:
                note = user.get("note", "")
                self.text_note.insert("1.0", note)
                break
    
    def auto_save(self, event):
        self.event = event
        content =   self.text_note.get("1.0", tk.END).strip()
        users = load_data()

        for user in users:
            if user["info"] == self.username:
                user["note"] = content
            break
        save_data(users)

# if __name__ == "__main__":
#     root = tk.Tk()
#     root.withdraw()  # Ẩn cửa sổ gốc nếu không dùng
#     ToDoApp(root, "Minh Quan", "quan02077@gmail.com", "minhQuan2006")  # Tên người dùng giả lập
#     root.mainloop()
