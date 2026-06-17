import tkinter as tk
import tkinter.font as tkFont

root = tk.Tk()
fonts = tkFont.families()
for f in fonts:
    print(f)
root.destroy()
