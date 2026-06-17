from tkinter import *
from PIL import Image, ImageTk #Khai báo thư viện PILLOW để định dạnh ảnh JPG qua các định dạnh mà PhoToImage đọc được
window = Tk()
image = Image.open("background.jpg")
photo = ImageTk.PhotoImage(image) #2 dòng này dùng để mở file hình JPG và chuyển về PNG, GIF, PPM,...
label = Label(window, 
              text="Quan dep trai vai chuong!", 
              font= ('Arial', 40, 'bold'), 
              fg= "#46F527", 
              bg= "#3A3D39", 
              relief=RAISED, #Viền
              bd= 20, #Độ dày của viền
              padx = 20,
              pady = 20,
              image=photo,
              compound= "bottom") #Vị trí của hình
label.pack()
#label.place(x= 100, y =50)
window.mainloop()