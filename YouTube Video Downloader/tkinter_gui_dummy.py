import tkinter as tk
import os
from time import time

W = WIDTH = 733
H = HEIGHT = 434

root = tk.Tk()
v = tk.IntVar()

url_type_radio = tk.Radiobutton(root, text= "Video", padx= 10, variable= v, value= 1)
url_type_radio.pack()


frame = tk.Frame(root)
l = tk.Label(frame, text="Label in Frame")
l.pack()




def show():
    d_print(v.get())

tk.Button(root, text= 'Click Me', command= show).pack()


















root.title("Playlist Downloader")
root.geometry(f"{W}x{H}")
root.minsize(W, H)
root.maxsize(W, H)



root.mainloop()
exit()
