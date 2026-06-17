import tkinter as tk
from tkvideo import tkvideo

root = tk.Tk()

l = tk.Label(root)
l.pack()

player = tkvideo("clap.mp4", l, loop= 1, size= (700, 500))
player.play()

root.mainloop()
