from typing import Union
from tkinter import Menu
from tkinter import Tk, Label, SUNKEN, EW
from tkinter import Scrollbar, Entry, NORMAL, HORIZONTAL
from tkinter import OptionMenu
from tkinter import INSERT
from constants import DEFAULT_ENTRY_PLACEHOLDER, OS
from typing import Callable
from event_handlers import (
    select_all,
    erase_placeholder,
    add_placeholder,
    custom_paste,
    fix_keypad,
    ctrl_backspace,
    shift_delete,
    ctrl_delete,
    focus_in_submit,
    focus_out_submit,
    cursor_go_left,
    cursor_go_right,
    cursor_follow_delta
)



def add_cascade_menu(parent_menu : Menu, name, options : Union[dict, list, tuple, set], separator_at : Union[int, tuple, list, set]= None):
    """
    Adds a Cascade Menu inside a given parent menu using options from an iterable
    """
    if isinstance(options, (list, tuple, set)):
        temp = dict()
        for each in options:
            temp[each] = None
        options = temp

    elif not isinstance(options, dict):
        raise ValueError(":options: of type %s must be either list, tuple, set or dict" % (type(options)))

    if not separator_at:
        separator_at = 0

    if isinstance(separator_at, int) and separator_at < 0:
        separator_at = len(options) + separator_at

    if not isinstance(separator_at, (tuple, list, set)):
        separator_at = [separator_at, ]


    menu = Menu(parent_menu)
    parent_menu.add_cascade(label= name, menu= menu)

    for i, option_pair in enumerate(options.items(), start= 1):
        option_name, option_command = option_pair
        menu.add_command(label= option_name, command= option_command)

        if i in separator_at:
            menu.add_separator()

    return menu



def create_label(parent : Tk, text, row= None, column= None, bd= 2, bg= "#ffe680", relief= SUNKEN, width= 20, **kwargs):
    """
    Creates a Label widget with a preferred set of default options for convenience
    """
    label = Label(parent, text= text, bd= bd, bg= bg, relief= relief, width= width, **kwargs)

    if not (row is None and column is None):
        label.grid(row= row or 0, column= column or 0, sticky= EW)

    return label



def create_scroll_entry(parent : Tk, textvariable, row= None, column= None, state= NORMAL, placeholder= DEFAULT_ENTRY_PLACEHOLDER, **kwargs):
    """
    Creates a set of One Entry and One Scrollbar, both attached, and also Entry widget is added Shortcut Functionalities
    """
    scrollbar = Scrollbar(parent, orient= HORIZONTAL)

    entry = Entry(parent, textvariable= textvariable, state= state, xscrollcommand= scrollbar.set)
    scrollbar.config(command= entry.xview)

    if not (row is None and column is None):
        entry.grid(row= row or 0, column= column or 0, sticky= EW)
        scrollbar.grid(row= row+1, column= column, sticky= EW)

    fix_keypad(for_widget= entry)

    entry.bind("<Control-a>", select_all)
    entry.bind("<<Paste>>", custom_paste)
    entry.bind('<Control-BackSpace>', ctrl_backspace)
    entry.bind('<Shift-Delete>', shift_delete)
    entry.bind('<Control-Delete>', ctrl_delete)


    entry.insert(0, placeholder)    # Adding The Background String Initially
    entry.bind("<FocusIn>", lambda event, placeholder= placeholder : erase_placeholder(event, placeholder))
    entry.bind("<FocusOut>", lambda event, placeholder= placeholder : add_placeholder(event, placeholder))

    if OS == "Linux":
        entry.bind('<4>', cursor_go_right)
        entry.bind('<5>', cursor_go_left)
    else:
        # Windows and MacOS
        entry.bind("<MouseWheel>", cursor_follow_delta)

    return entry, scrollbar


def create_submit_scroll_entry(parent : Tk, textvariable, row= None, column= None, func : Callable= print, state= NORMAL, placeholder= "Enter...", threaded= True, **kwargs):
    """
    Automatically calls the :func: and transfers the contents into the :func:.
    """
    entry, scrollbar = create_scroll_entry(parent, textvariable, row, column, state, placeholder, **kwargs)

    entry.bind("<Return>", lambda event : focus_in_submit(event, placeholder= placeholder, func= func, threaded= threaded))
    entry.bind("<FocusOut>", lambda event : focus_out_submit(event, placeholder= placeholder, func= func, threaded= threaded))




    return entry, scrollbar



def create_dropdown(parent : Tk, textvariable : str, row= None, column= None, func : Callable= print, options= [], *other_options, **kwargs):
    """
    Creates a dropdown with a set of preferred defaults using contents from a list or *args
    """
    dropdown = OptionMenu(parent, textvariable, *options, *other_options, command= func)


    if not (row is None and column is None):
        dropdown.grid(row= row or 0, column= column or 0, sticky= EW)

    return dropdown
