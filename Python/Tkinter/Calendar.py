from tkinter import *
import calendar
from datetime import datetime

def show_calendar():
    text.delete("1.0", END)
    text.insert(END, calendar.month(year, month))

def tiep():
    global year, month
    month += 1
    if month == 13:
        month = 1
        year += 1
    show_calendar()

def lui():
    global year, month
    month -= 1
    if month == 0:
        month = 12
        year -=1
    show_calendar()

window = Tk()

now = datetime.now()
year = now.year
month = now.month

text = Text(window, width= 20, height= 8, font= ("Consolas", 12))
text.grid(row= 0, column= 0 ,columnspan= 3)

next_button = Button(window, text= "Next", command=tiep)
next_button.grid(row= 1, column= 1)

prev_button = Button(window, text= "Previous", command=lui)
prev_button.grid(row= 1, column= 0)

show_calendar()

window.mainloop()