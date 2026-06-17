from tkinter import *
import re
from tkinter import messagebox
import datetime

tour = ["Tour thành phố", "Tour biển", " Tour núi"]
def check():
    name = user_entry.get()
    email = email_entry.get()
    sdt = sdt_entry.get()
    nkh = nkh_entry.get()
    sl = sl_entry.get()

    errors = []

    if not name:
       errors.append("Tên khách hàng không được để trống")
   
    if not email:
       errors.append("Email không được để trống")
    else:
       email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
       if not re.match(email_pattern, email):
           errors.append("Email không đúng định dạng")
    if not sdt:
        errors.append("Số điện thoại không được để trống")
    elif not sdt.isdigit():
        errors.append("Số điện thoại chỉ là số")
    
    if not nkh:
        errors.append("Ngày khởi hành không được để trống")
    else:
        try:
            datetime.datetime.strptime(nkh, '%d-%m-%Y')
        except ValueError:
            errors.append("Ngày khởi hành sai định dạng (dd-mm-yyyy) hoặc ngày không hợp lệ")

    if not sl:
        errors.append("Số lượng không được để trống")
    else:
        try:
            sl_val = int(sl)
            if sl_val <= 0:
                errors.append("Số lượng phải lớn hơn 0")
        except ValueError:
            errors.append("Số lượng phải là một con số")

    if errors:
        errors_message = "Vui lòng khắc phục các lỗi sau:\n\n" + "\n".join(errors)
        messagebox.showerror("Lỗi đăng ký", errors_message)
    else:
        tour_name = tour[x.get()]

        kq = "ĐĂNG KÝ TOUR THÀNH CÔNG!\n"

        kq += "-------------------------------------\n"
        kq += f"Họ tên: {name}\n"
        kq += f"Email: {email}\n"
        kq += f"Điện thoại: {sdt}\n"
        kq += f"Ngày đi: {nkh}\n"
        kq += f"Số lượng: {sl}\n"
        kq += f"Tour đã chọn: {tour_name}\n"
        
        messagebox.showinfo("Thành công", kq)
        
        user_entry.delete(0, END)
        email_entry.delete(0, END)
        sdt_entry.delete(0, END)
        nkh_entry.delete(0, END)
        sl_entry.delete(0, END)
        x.set(0)
       

window = Tk()
window.geometry("550x500")
window.config(background= "#bce3c7")
window.title("Đăng ký tour")

user_label = Label(window, text= "Tên khách hàng", bg= "#bce3c7")
user_label.grid(row= 0, column= 1, pady= 20, padx = 50)

user_entry = Entry(width= 30)
user_entry.grid(row= 0, column= 2, pady= 20)

email_label = Label(window, text= "Email", bg= "#bce3c7")
email_label.grid(row= 1, column= 1, pady= 20)

email_entry = Entry(width= 30)
email_entry.grid(row= 1, column= 2, pady= 20)

sdt_label = Label(window, text= "Số điện thoại", bg= "#bce3c7")
sdt_label.grid(row= 2, column= 1, pady= 20)

sdt_entry = Entry(width= 30)
sdt_entry.grid(row= 2, column= 2, pady= 20)

nkh_label = Label(window, text= "Ngày khởi hành", bg= "#bce3c7")
nkh_label.grid(row= 3, column= 1, pady= 20)

nkh_entry = Entry(width= 30)
nkh_entry.grid(row= 3, column= 2, pady= 20)

sl_label = Label(window, text= "Số lượng", bg= "#bce3c7")
sl_label.grid(row= 4, column= 1, pady= 20)

sl_entry = Entry(width= 30)
sl_entry.grid(row= 4, column= 2, pady= 20)

luachon_label = Label(window, text= "Lựa chọn tour", bg= "#bce3c7")
luachon_label.grid(row= 5, column= 1)

x = IntVar()
frame = Frame(window, bg= "#bce3c7")
frame.grid(row= 5, column= 2)
for i in range(len(tour)):
    luachon = Radiobutton(frame, text= tour[i], variable= x, value= i, bg= "#bce3c7")
    luachon.pack(anchor= W)

button = Button(window, text="Đăng ký", command= check)
button.grid(row= 9, column= 2)

window.mainloop()