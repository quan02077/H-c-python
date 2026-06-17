from tkinter import *
count = 0
def Click():
    global count
    count += 1
    label.config(text= count) #Dòng này dùng để số lần click trên màn hoạt động và thay đổi
    label2.pack() #Dòng này dùng để khi mỗi lần ta click thì nó sẽ đóng gói và thêm 1 hình vào window
window = Tk()
button = Button(window, text= "Click!")
button.config(command=Click)
button.config(font=("Ink Free", 40, "bold"))
button.config(bg= "red")
button.config(fg= "yellow")
button.config(activebackground= "green")
button.config(activeforeground= "pink")
# Đổi định dạng ảnh từ JPG sang định dạng mà PhoToImage đọc được
photo = PhotoImage(file= "point_emoji.png")
button.config(image=photo)
button.config(compound= "bottom")
#button.config(state= DISABLED) #Vô hiệu hóa nút (ACTIVE hoặc DISABLE)
label = Label(window, text= count)
label.config(font=("Monospace", 50)) #Ba dòng này dùng để in số lần bạn click vào button trên màn hình window
label.pack()
label2 = Label(window, image=photo) #Dòng này dùng để tạo thêm 1 cái hình nữa
button.pack()
window.mainloop()