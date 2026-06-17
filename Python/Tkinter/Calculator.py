from tkinter import *

def button_press(num):
    global luu_kq

    luu_kq = luu_kq + str(num) #Đây là hàm khi bấm nút là biến luu_kq đang rỗng sẽ thêm các nút mình bấm vào

    equaltion_text.set(luu_kq) #Set luu_kq để in ra label

def result():
    global luu_kq
    try:
        kq =  str(eval(luu_kq)) #Hàm eval() dùng để tính toán cái chuỗi đó

        equaltion_text.set(kq)

        luu_kq = kq #Để giữ lại kết quả để tính tiếp
    except ZeroDivisionError:
        equaltion_text.set("Loi phep tinh")
    except SyntaxError:
        equaltion_text.set("Loi cu phap")
def clear():
    global luu_kq

    equaltion_text.set("") #Set rỗng để in ra label

    luu_kq = "" 

window = Tk()
window.geometry("500x500")

luu_kq = ""

equaltion_text = StringVar() #StringVar() liên kết với các widget

equaltion_label = Label(window, textvariable=equaltion_text, height= 4, width= 45, bg= "white", font= 20) #textvariable= là nơi chỉ định widget để lấy dữ liệu
equaltion_label.pack(pady= 10)

frame = Frame(window)
frame.pack(pady= 5)

button1 = Button(frame, text= 1, height=4, width=9, font= 35, command= lambda: button_press(1))
button1.grid(row= 2, column= 0)

button2 = Button(frame, text= 2, height=4, width=9, font= 35, command= lambda: button_press(2))
button2.grid(row= 2, column= 1)

button3 = Button(frame, text= 3, height=4, width=9, font= 35, command= lambda: button_press(3))
button3.grid(row= 2, column= 2)

button4= Button(frame, text= 4, height=4, width=9, font= 35, command= lambda: button_press(4))
button4.grid(row= 1, column= 0)

button5 = Button(frame, text= 5, height=4, width=9, font= 35, command= lambda: button_press(5))
button5.grid(row= 1, column= 1)

button6 = Button(frame, text= 6, height=4, width=9, font= 35, command= lambda: button_press(6))
button6.grid(row= 1, column= 2)

button7= Button(frame, text= 7, height=4, width=9, font= 35, command= lambda: button_press(7))
button7.grid(row= 0, column= 0)

button8 = Button(frame, text= 8, height=4, width=9, font= 35, command= lambda: button_press(8))
button8.grid(row= 0, column= 1)

button9 = Button(frame, text= 9, height=4, width=9, font= 35, command= lambda: button_press(9))
button9.grid(row= 0, column= 2)

button0 = Button(frame, text=0, height=4, width=9, font= 35, command= lambda: button_press(0))
button0.grid(row= 3, column= 0)

plus = Button(frame, text= '+', height=4, width=9, font= 35, command=lambda: button_press('+'))
plus.grid(row= 0, column= 3)

minus = Button(frame, text= '-', height=4, width=9, font= 35, command=lambda: button_press('-'))
minus.grid(row= 1, column= 3)

multiply = Button(frame, text= '*', height=4, width=9, font= 35, command=lambda: button_press('*'))
multiply.grid(row= 2, column= 3)

divide = Button(frame, text= '/', height=4, width=9, font= 35, command=lambda: button_press('/'))
divide.grid(row= 3, column= 3)

equal = Button(frame, text= '=', height=4, width=9, font= 35, command= result)
equal.grid(row= 3, column= 2)

decimal = Button(frame, text= '.', height=4, width=9, font= 35, command=lambda: button_press('.'))
decimal.grid(row= 3, column= 1)

clear = Button(window, text= "Clear", height=4, width=36, font= 35, command= clear)
clear.pack()

window.mainloop()