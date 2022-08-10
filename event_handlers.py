from typing import Callable
from threading import Thread
from tkinter import INSERT, END, TclError
from gui_connector import Cache
from helper_functions import d_print



def select_all(event):
    # select text
    event.widget.select_range(0, END)
    # move cursor to the end
    event.widget.icursor(END)
    #stop propagation
    return 'break'



def erase_placeholder(event= None, placeholder= ""):
    if not event:
        d_print("No event given in erase_placeholder!!")
        return

    d_print("Used erase placeholder for", event.widget._name)
    if event.widget.get().strip() == placeholder:
        d_print("Erased placeholder")
        event.widget.delete(0,END)



def add_placeholder(event= None, placeholder= ""):
    if not event:
        d_print("No event given in add_placeholder!!")
        return

    d_print("Used add placeholder for", event.widget._name)
    if event.widget.get().strip() == '':
        d_print("Added placeholder")
        event.widget.insert(0, placeholder)



def custom_paste(event):
    try:
        event.widget.delete("sel.first", "sel.last")
    except:
        pass

    # event.widget.insert("insert", event.widget.clipboard_get())
    # File "/usr/lib/python3.10/tkinter/__init__.py", line 904, in clipboard_get
    #     return self.tk.call(('clipboard', 'get') + self._options(kw))
    # _tkinter.TclError: CLIPBOARD selection doesn't exist or form "STRING" not defined
    try:
        event.widget.insert("insert", event.widget.clipboard_get())
    except TclError:
        print("No string copied inside the clipboard... Skipping Paste")
    return "break"



def focus_out_submit(event, placeholder= '', func : Callable= print, threaded : bool= False):
    text = event.widget.get()
    text = (text or '').strip()

    if not text or text == placeholder:
        erase_placeholder(event, placeholder)
        add_placeholder(event, placeholder)
        return

    if not threaded:
        func(text)
        return

    thread = Thread(target= func, args= (text, ))
    thread.start()
    Cache.threads.append(thread)
    return 0



def focus_in_submit(event, placeholder= '', func : Callable= print, threaded : bool= False):
    text = event.widget.get()
    text = (text or '').strip()

    if not text or text == placeholder:
        erase_placeholder(event, placeholder)
        return

    if not threaded:
        func(text)
        return

    thread = Thread(target= func, args= (text, ))
    thread.start()
    Cache.threads.append(thread)
    return 0



def fix_keypad(for_widget):
    widget = for_widget
    kmap = {
        '<KP_Left>': '<Left>',
        '<KP_Right>': '<Right>',
        '<KP_Up>': '<Up>',
        '<KP_Down>': '<Down>',
        '<KP_Home>': '<Home>',
        '<KP_End>': '<End>',
        '<KP_Next>': '<Next>',
        '<KP_Prior>': '<Prior>',
        '<KP_Enter>': '<Return>',
        '<KP_Delete>': '<Delete>',
    }
    for i in kmap:
        def mfunc(event, key=i):
            widget.event_generate(kmap[key], **{'state': event.state})
        widget.bind(i, mfunc)



def ctrl_backspace(event):
    widget = event.widget
    end_idx = widget.index(INSERT)
    start_idx = widget.get().rfind(" ", None, end_idx)
    widget.selection_range(start_idx, end_idx)



def shift_delete(event):
    widget = event.widget
    event.widget.delete(0, END)



def ctrl_delete(event):
    widget = event.widget
    start_idx = widget.index(INSERT)
    end_idx = widget.index(END)
    del_idx = widget.get().find(" ", start_idx, end_idx)
    del_idx = del_idx if del_idx != -1 else end_idx
    d_print("Ctrl Delete From", start_idx, "to", del_idx)
    event.widget.delete(INSERT, del_idx)



def cursor_go_left(event):
    position = event.widget.index(INSERT)
    event.widget.icursor(position - 1)

def cursor_go_right(event):
    position = event.widget.index(INSERT)
    event.widget.icursor(position + 1)


def cursor_follow_delta(event):
    if event.delta < 0:
        cursor_go_left(event)
    elif event.delta > 0:
        cursor_go_right(event)
