from tkinter import *
from PIL import Image, ImageTk
#Mảng thực đơn để làm radio button
food = ["Cơm Tấm", "Hủ Tiếu", "Bánh Mì"]

def order():
    if(x.get() == 0):
        label.config(text= "Mày chọn Cơm Tấm!")
    elif(x.get() == 1):
        label.config(text= "Mày chọn Hủ Tiếu!")
    elif(x.get()== 2):
        label.config(text= "Mày chọn Bánh Mì!")
    else:
        label.config(text= "Thế mày ăn cái gì?")

window = Tk()
#Mở hình ảnh chỉnh lại kích thước cho phù hợp và chuyển định dạng
window.config(background= "white")
image1 = Image.open("com_tam.png")
image1 = image1.resize((60,60))
com_tam = ImageTk.PhotoImage(image=image1)

image2 = Image.open("hu_tieu.jpg")
image2 = image2.resize((60,60))
hu_tieu = ImageTk.PhotoImage(image=image2)

image3 = Image.open("banh_mi.jpg")
image3 = image3.resize((60,60))
banh_mi = ImageTk.PhotoImage(image=image3)
#Mảng hình ảnh
food_image = [com_tam, hu_tieu, banh_mi]
x = IntVar()    
for i in range(len(food)):
    check = Radiobutton(window, 
                        text=food[i], #text gán bằng các phần tử trong mảng thực đơn
                        variable=x, 
                        value= i,  #value gán bằng chỉ số index của mảng 0,1,...
                        padx= 25, 
                        font=("Impact", 50), 
                        image=food_image[i],  #image gán bằng các phần tử trong mảng hình ảnh
                        compound= "left", 
                        bg= "white",
                        #indicatoron= 0, #Xóa chọn bằng hình tròn
                        #width = 375 #Chỉnh kích thước của radio button
                        command= order
                        )
    check.pack(anchor= W)
    label = Label(window, text="", bg= "white")
    label.pack()
window.mainloop()