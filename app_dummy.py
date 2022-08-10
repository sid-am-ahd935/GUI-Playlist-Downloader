# import tkinter as tk
# root = tk.Tk()
# root.geometry("700x900")



# l = tk.Listbox(root)
# l.grid(row=0, column=0, sticky=tk.NSEW)



# for i in range(100):
#     f = tk.Frame(l, bd= 10, bg= "green")
#     f.grid(row= i, column= 0, columnspan= 2, sticky= tk.EW)
#     tk.Label(f, text= f"Hello There{i*100}", bg= "#ffe680").grid(row= 0, column= 0, sticky= tk.NSEW)
#     tk.Button(f, text= f"Click My {i}th Button", bg= "#ffe680", command= lambda : print(i)).grid(row= 0, column= 1, sticky= tk.NSEW)
#     l.columnconfigure(i, weight=1)













# root.columnconfigure(0, weight= 1)
# root.rowconfigure(0, weight= 1)
# root.mainloop()

# from tkinter import *
# from tkinter.scrolledtext import ScrolledText
# root = Tk()

# box = ScrolledText(root, width=15)
# box.pack(expand= 1, fill= BOTH)

# for i in range(20):
#     frame = Frame()
#     label = Label(frame, text=f"item {i}")
#     label.pack(side=LEFT)
#     button = Button(frame, text="click")
#     button.pack(side=LEFT)
#     box.window_create(END, window=frame)
#     box.insert(END, '\n')

# root.mainloop()

from threading import Thread
from pytube import YouTube, Playlist

url = "https://www.youtube.com/playlist?list=PL3IdQ7nHrG706h74SqSjKGbBn6lhpmMxs"
url = "https://www.youtube.com/playlist?list=PLhyHc3W8oSov-ucuA2YzzFMTJPZ6GNXJy"

class Cache:
    video_details = dict()
    threads = []

def get_details(i, v_url):
    vid_obj = YouTube(v_url)
    vid_info = vid_obj.vid_info
    streams = vid_obj.streams
    vid_details = vid_info['videoDetails']
    Cache.video_details[i] = vid_info, streams, vid_details
    # Cache.video_details[i] = vid_obj

for i, v_url in enumerate(Playlist(url)):

    thread = Thread(target= get_details, args= (i, v_url))
    thread.start()

    Cache.threads.append(thread)

for t in Cache.threads:
    t.join()

for k, v in Cache.video_details.items():
    i = k
    vid_info, streams, vid_details = v

    print(vid_details['title'])

print(len(Cache.video_details))
