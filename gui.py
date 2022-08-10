import tkinter as tk

from gui_connector import Cache
from gui_utils import add_cascade_menu, create_dropdown, create_label, create_scroll_entry, create_submit_scroll_entry



# Defined Constants for the GUI
from constants import (
    WIDTH,
    HEIGHT,
    PANE_MIN_WIDTH,
    PANE_MIN_SUB_HEIGHT,
    URL_PLACEHOLDER,
    QUALITY_PLACEHOLDER,
    AV_PLACEHOLDER,
    sp
)


# Parent Widgets
root = tk.Tk()

menu_bar = tk.Menu(root)
root.config(menu= menu_bar)

changable_frame = tk.Frame(root)

main_paned = tk.PanedWindow(changable_frame, orient= tk.HORIZONTAL, showhandle= True, sashrelief= tk.RAISED, sashwidth= 10, handlesize= 10)
left_paned = tk.PanedWindow(main_paned, orient= tk.VERTICAL, showhandle= True, sashrelief= tk.RAISED, sashwidth= 10, handlesize= 10)

left_top_frame = tk.Frame(main_paned, bg = "green", bd= 5, relief= tk.SUNKEN)
left_bottom_frame = tk.Frame(main_paned, bg = "red", bd= 5, relief= tk.SUNKEN)
right_frame = tk.Frame(main_paned, bd= 5, relief= tk.SUNKEN, padx= 10, pady= 10)


left_paned.add(left_top_frame, minsize= PANE_MIN_SUB_HEIGHT // 1)
left_paned.add(left_bottom_frame, minsize= PANE_MIN_SUB_HEIGHT // 3)        # Bottom Left is one-third size of top
main_paned.add(left_paned, minsize= PANE_MIN_WIDTH)
main_paned.add(right_frame, minsize= PANE_MIN_WIDTH)


changable_frame.pack(expand= 1, fill= tk.BOTH)
main_paned.pack(fill= tk.BOTH, expand= 1)


# GUI Variables
url_var = tk.StringVar()
path_var = tk.StringVar()
quality_var = tk.StringVar(value= QUALITY_PLACEHOLDER)
av_var = tk.StringVar(value= AV_PLACEHOLDER)
include_var = tk.StringVar()
exclude_var = tk.StringVar()

# Adding GUI variables to the connector
Cache.vars = {
    "url_var" : url_var,
    "path_var" : path_var,
    "quality_var" : quality_var,
    "av_var" : av_var,
    "include_var" : include_var,
    "exclude_var" : exclude_var
}


# Options For Cascade Menus
help_options = {
    "Docs" : None,
    "Usage" : None,
    "Demo" : None,
    "Tutorial" : None
}
settings_options = {
    "Lock Window Size" : None,
    "Dark Mode" : None,
    "Add Default Video Quality" : None
}
about_options = {
    "Credits" : None,
    "Repository Link" : None,
    "PyPi/Any Other Link" : None
}

# Options For Dropdown Widgets
quality_options = [
    "Low",
    "Medium",
    "High",
]
av_options = [
    "AV Both",
    "Audio Only",
    "Video Only",
]


####----Right Frame----####

help_menu = add_cascade_menu(menu_bar, "Help", options= help_options, separator_at= -1)
settings_menu = add_cascade_menu(menu_bar, "Settings", options= settings_options, separator_at= 2)
about_menu = add_cascade_menu(menu_bar, "About", options= about_options, separator_at= 2)


url_label = create_label(right_frame, "Playlist URL", 0, 0)
url_entry, url_entry_scrollbar = create_submit_scroll_entry(right_frame, url_var, 0, 1, func= Cache.add_videos, placeholder= URL_PLACEHOLDER)

path_label = create_label(right_frame, "Folder Path", 2, 0)
path_entry, path_entry_scrollbar = create_submit_scroll_entry(right_frame, path_var, 2, 1, func= Cache.save_path)

quality_label = create_label(right_frame, "Select Quality", 4, 0)
quality_dropdown = create_dropdown(right_frame, quality_var, 4, 1, Cache.save_quality, quality_options)

av_label = create_label(right_frame, "Select Video Type", 5, 0)
av_dropdown = create_dropdown(right_frame, av_var, 5, 1, Cache.save_av, av_options)

include_label = create_label(right_frame, "Videos Included", 6, 0)
include_entry, include_entry_scrollbar = create_submit_scroll_entry(right_frame, include_var, 6, 1, func= Cache.save_include)

exclude_label = create_label(right_frame, "Videos Excluded", 8, 0)
exclude_entry, exclude_entry_scrollbar = create_submit_scroll_entry(right_frame, exclude_var, 8, 1, func= Cache.save_exclude)

submit_button = tk.Button(right_frame, text= f"{sp('GO', 10)}", relief= tk.RAISED, bg= "#33ff33", bd= 2, command= Cache.final_submit)
submit_button.grid(row= 10, column= 0, columnspan= 2)

donwload_button = tk.Button(right_frame, text= f"{sp('DOWNLOAD', 4)}", relief= tk.RAISED, bg= "#33ff33", bd= 2, command= Cache.download_selection)
donwload_button.grid(row= 11, column= 0, columnspan= 2)


right_frame.columnconfigure(0, weight= 1)
right_frame.columnconfigure(1, weight= 3)
####----Done Nothing Left to Change Here----####



####----Left Top Frame----####


details_scrollbar = tk.Scrollbar(left_top_frame, orient= tk.VERTICAL)
details_box = tk.Listbox(left_top_frame, yscrollcommand= details_scrollbar.set)
details_scrollbar.config(command= details_box)

Cache.listbox = details_box

details_box.grid(row= 0, column= 0, sticky= tk.NSEW)
details_scrollbar.grid(row= 0, column= 1, sticky= tk.NSEW)
left_top_frame.columnconfigure(0, weight= 1)
left_top_frame.rowconfigure(0, weight= 1)

# root.columnconfigure(0,weight=2)
# root.columnconfigure(1,weight=1)
# root.rowconfigure(0,weight=1)


####----Done Nothing Left To Change Here----####


####----Left Bottom Status Bar----####

status_scrollbar = tk.Scrollbar(left_bottom_frame, orient= tk.VERTICAL)
status_box = tk.Listbox(left_bottom_frame, yscrollcommand= status_scrollbar.set)
status_scrollbar.config(command= status_box.yview)

Cache.statusbox = status_box

status_box.grid(row= 0, column= 0, sticky= tk.NSEW)
status_scrollbar.grid(row= 0, column= 1, sticky= tk.NSEW)
left_bottom_frame.columnconfigure(0, weight= 1)
left_bottom_frame.rowconfigure(0, weight= 1)













def update_widgets(event):
    root.title((f"[{root.winfo_width()}x{root.winfo_height()}]"))





root.after(1000 * 500, lambda : root.destroy())
root.bind("<Configure>", update_widgets)



url_entry.focus()






root.geometry(f"{WIDTH}x{HEIGHT}")
root.minsize(width= WIDTH, height= HEIGHT)
root.mainloop()
