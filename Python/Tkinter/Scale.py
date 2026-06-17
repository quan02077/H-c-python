from tkinter import *
from PIL import Image, ImageTk
def submit():
    label.config(text= "The temperature is: " +str(scale.get())+" degrees C")
window = Tk()

hotImage= Image.open("hot.png")
hotImage = hotImage.resize((50,50))
hotPhoto= ImageTk.PhotoImage(image=hotImage)#Thêm hình ảnh vào
hotLabel= Label(window, image=hotPhoto)
hotLabel.pack()

scale = Scale(window, 
              from_=100, 
              to= 0,
              length= 500,  #Chiều dài của cái scale
              orient= VERTICAL, #Scale đặt ngang hay dọc Vertical/Horizontal
              font= ("Consolas", 20),
              tickinterval= 10, #Hiện ra cá chỉ số trên scale nếu để là 10 là nó sẽ cách 10 số 
              #showvalue= 0, #Điều này sẽ làm ẩn chỉ số hiện tại khi kéo thanh trượt
              #resolution= 5, #Mỗi lần trượt thanh trượt chỉ nó sẽ khực lại cách 5 số
              troughcolor= "#69EAFF",
              bg = "black",
              fg = "red"
              )
scale.set(((scale["from"] - scale["to"]) /2) + scale["to"]) #Dùng để khi mở lên mặc định thanh trượt sẽ ở số mà bạn điền vào hoặc bạn nhập vào công thức như này để tính ra con số ở giữa
scale.pack()

iceImage= Image.open("ice.png")
iceImage = iceImage.resize((50,50))
icePhoto= ImageTk.PhotoImage(image=iceImage) #Thêm hình ảnh vào
iceLabel= Label(window, image=icePhoto)
iceLabel.pack()

button = Button(window, text= "Submit", command=submit)
button.pack()

label = Label(window, text="")
label.pack()
window.mainloop()