import tkinter as tk
from tkinter import ttk, messagebox
import json, os
from PIL import Image, ImageTk
from todo_app  import ToDoApp   #import để mở cửa sổ todoapp
from user_data import load_data, save_data #import để sử dụng hàm đọc và lưu file
import re

class LoginForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Đăng nhập")
        self.root.geometry("400x350")
        self.root.resizable(False, False) #Dùng để cho cửa sổ không thể phóng to ra được
        self.root.configure(bg="#F1F3E0")

        if os.path.isfile("logo.jpg"):
            self.photo = Image.open("logo.jpg")
            self.logo = ImageTk.PhotoImage(self.photo)
            self.root.iconphoto(False, self.logo)

        tk.Label(self.root, text="Focus", font=("TechnicBold", 45, 'bold'),
                 bg="#F1F3E0").pack(pady=10)

        tk.Label(self.root, text="Tên tài khoản/Email", font=("Arial", 12, "bold"),
                 bg="#F1F3E0").pack(pady=5)
        self.entry_info = tk.Entry(self.root, width=30)
        self.entry_info.pack()

        img_show = Image.open("show.png")
        img_hide = Image.open("hide.png")

        img_show = img_show.resize((20, 20))
        img_hide = img_hide.resize((20, 20))

        self.show_image = ImageTk.PhotoImage(img_show)
        self.hide_image = ImageTk.PhotoImage(img_hide)

        self.eye_btn = tk.Button(self.root, image=self.show_image, command=self.toggle_password, bg="#F1F3E0")
        self.eye_btn.place(x=310, y=180)  #Đặt vị trí cố định

        tk.Label(self.root, text="Mật khẩu", font=("Arial", 12, "bold"),
                 bg="#F1F3E0").pack(pady=5)
        self.entry_password = tk.Entry(self.root, width=30, show="*")
        self.entry_password.pack()

        # 3 nút phụ
        btn_frame = tk.Frame(self.root, bg="#F1F3E0") #Tạo frame để dùng grid căn cho đẹp
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Đăng ký tài khoản",
                  bg="#328E6E", font=("Arial", 10, "bold"), fg= "white",
                  command=self.open_register).grid(row=0, column=0, padx=10)

        tk.Button(btn_frame, text="Quên mật khẩu",
                  bg="#328E6E", font=("Arial", 10, "bold"), fg= "white",
                  command=self.open_forget).grid(row=0, column=1, padx=10)

        tk.Button(self.root, text="Đăng nhập",
                  bg="#ff5757", font=("Arial", 10, "bold"), fg= "white",
                  command=self.login).pack(pady=10)
        
        self.root.bind("<Return>", lambda event: self.login()) #Dùng để có thể nhấn Enter mà không cần ấn nút đăng nhập trên giao diện
    
    def toggle_password(self): #Hàm chuyển pass 
        if self.entry_password.cget("show") == "": #Lấy giá trị show của widget entry_password nếu nó = "" nghĩa là không phải *
            self.entry_password.config(show="*") #Chuyển nó thành * để ẩn pass
            self.eye_btn.config(image=self.show_image) #Và set lại cái hình thành mắt mở
        else:
            self.entry_password.config(show="")
            self.eye_btn.config(image=self.hide_image)

    
    def login(self):
        info = self.entry_info.get().strip()
        password_n = self.entry_password.get().strip()

        if info == "":
            messagebox.showerror("Lỗi", "Vui lòng nhập tên tài khoản/email của bạn")
        
        if password_n == "":
            messagebox.showerror("Lỗi", "Vui lòng nhập mật khẩu của bạn")

        users = load_data()
        found = False
        for user in users:
            if (user["info"] == info or user["email"] == info) and user["password"] == password_n: #Có thể đăng nhập bằng user hoặc email
                found = True
                break
        if found:
            messagebox.showinfo("Đăng nhập", f"Chào mừng {user['info']}!")
            username = user["info"] #Lấy tên trong mảng user để gán vào username
            email = user["email"]
            password = user["password"]
            self.root.withdraw() #Ẩn dùng để ẩn đi cửa sổ đăng nhập
            ToDoApp(self.root, username, email, password) #Mở cửa sổ todoapp
            self.entry_info.delete(0, tk.END)
            self.entry_password.delete(0, tk.END)
        else:
            messagebox.showerror("Lỗi", "Sai tài khoản hoặc mật khẩu!")
            self.entry_info.delete(0, tk.END)
            self.entry_password.delete(0, tk.END)

    def open_register(self):
        self.root.withdraw()
        RegisterForm(self.root)#Mở form đăng ký

    def open_forget(self):
        self.root.withdraw()
        ForgetPasswordForm(self.root)#Mở form quên mật khẩu

class ForgetPasswordForm:
    def __init__(self, root):
        self.root = root
        self.win = tk.Toplevel(root)
        self.win.title("Quên mật khẩu")
        self.win.geometry("400x250")
        self.win.configure(bg="#F1F3E0")
        self.win.attributes("-topmost", True) #Dùng để khi xuất hiện cửa sổ này sẽ ở đằng trước form đăng nhập

        if os.path.isfile("logo.jpg"):
            self.photo = Image.open("logo.jpg")
            self.logo = ImageTk.PhotoImage(self.photo)
            self.win.iconphoto(False, self.logo)


        tk.Label(self.win, text="Đổi mật khẩu", font=("TechnicBold", 24, "bold"), 
                 bg="#F1F3E0").pack(pady=10)

        tk.Label(self.win, text="Tài khoản / Email", font=("Arial", 12, "bold"),bg="#F1F3E0").pack()
        self.entry_user = tk.Entry(self.win, width=30)
        self.entry_user.pack()

        tk.Label(self.win, text="Mật khẩu mới", font=("Arial", 12, "bold"),bg="#F1F3E0").pack()
        self.entry_new = tk.Entry(self.win, width=30, show="")
        self.entry_new.pack()


        tk.Button(self.win, text="Lưu", bg="#ff5757", fg= "white",
                  command=self.save, font=("Arial", 10, "bold")).pack(pady=10)
        
        self.win.bind("<Return>", lambda event: self.save())

    def save(self):
        username = self.entry_user.get().strip()
        newpass = self.entry_new.get().strip()

        users = load_data()
        found = False
        for user in users:
            if isinstance(user, dict):
                if user["info"] == username or user["email"] == username: #Tên với email phải giống với tên và email trong file thì mới cập nhật được 
                    user["password"] = newpass
                    found = True
                    break
        if found:
            save_data(users)
            messagebox.showinfo("Thành công", "Đổi mật khẩu thành công!")
            self.entry_user.delete(0, tk.END)
            self.entry_new.delete(0, tk.END)
            self.win.destroy()
            self.root.deiconify()
        else:
            messagebox.showerror("Lỗi", "Không tìm thấy tài khoản!")

class RegisterForm:
    def __init__(self, root):
        self.root = root
        self.win = tk.Toplevel(root)
        self.win.title("Đăng ký")
        self.win.geometry("400x400")
        self.win.configure(bg="#F1F3E0")
        self.win.attributes("-topmost", True)

        if os.path.isfile("logo.jpg"):
            self.photo = Image.open("logo.jpg")
            self.logo = ImageTk.PhotoImage(self.photo)
            self.win.iconphoto(False, self.logo)


        tk.Label(self.win, text="Đăng ký tài khoản", font=("TechnicBold", 24, "bold"),
                 bg="#F1F3E0").pack(pady=10)

        tk.Label(self.win, text="Tên tài khoản", font=("Arial", 12, "bold"),bg="#F1F3E0").pack()
        self.entry_user = tk.Entry(self.win, width=30)
        self.entry_user.pack()

        tk.Label(self.win, text="Email", font=("Arial", 12, "bold"),bg="#F1F3E0").pack()
        self.entry_email = tk.Entry(self.win, width=30)
        self.entry_email.pack()

        tk.Label(self.win, text="Mật khẩu", font=("Arial", 12, "bold"),bg="#F1F3E0").pack()
        self.entry_pass = tk.Entry(self.win, width=30, show="")
        self.entry_pass.pack()

        tk.Label(self.win, text="Xác nhận mật khẩu", font=("Arial", 12, "bold"),bg="#F1F3E0").pack()
        self.entry_confirm = tk.Entry(self.win, width=30, show="")
        self.entry_confirm.pack()

        tk.Button(self.win, text="Đăng ký", bg="#ff5757", fg= "white",
                  command=self.save, font=("Arial", 10, "bold")).pack(pady=10)
        
        self.win.bind("<Return>", lambda event: self.save())

    def save(self):
        username = self.entry_user.get().strip()
        email = self.entry_email.get().strip()
        pw = self.entry_pass.get().strip()
        cf = self.entry_confirm.get().strip()

        pattern_email = r'^[A-Za-z0-9]+[+_.]*@[a-z0-9]+\.[a-z]{2,4}$' #Kiểm tra email có đúng định dạng ko
        match = re.search(pattern_email, email) #So sánh email nhập vào có khớp với định dạng ko

        if not match:
            messagebox.showerror("Lỗi", "Vui lòng nhập lại email!")
            return

        if pw != cf: #Mật khẩu mới phải khác mật khẩu cũ
            messagebox.showerror("Lỗi", "Mật khẩu xác nhận không khớp!")
            return
        
        if len(pw) <= 6 or len(pw) >= 15:
            messagebox.showerror("Lỗi", "Mật khẩu phải dài hơn 6 và nhỏ hơn 15 kí tự!")
            return

        users = load_data()
        for u in users:
            if u["info"] == username or u["email"] == email: #Tên và email trùng với cái đã có rồi thì sẽ thông báo
                messagebox.showerror("Lỗi", "Tên hoặc Email đã tồn tại!")
                return
        users.append({
        "info": username,
        "email": email,
        "password": pw,
        "tasks": []
        })

        save_data(users) #Tạo 1 cái dict bằng những cái mình nhập vào và thêm vào 1 cái list và ghi vào file
        messagebox.showinfo("Thành công", "Đăng ký thành công!")
        self.entry_user.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.entry_pass.delete(0, tk.END)
        self.entry_confirm.delete(0, tk.END)
        self.win.destroy()
        self.root.deiconify()

root = tk.Tk()
LoginForm(root)
root.mainloop()
