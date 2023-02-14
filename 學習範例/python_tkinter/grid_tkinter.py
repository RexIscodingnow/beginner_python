'''
Tkinter 網格布局

    元件.grid()
'''

from tkinter import Tk, Label, Entry, Button


win = Tk()

def window_size(win_size: str):
    size = ""
    win_size = win_size.split()
    for char in win_size:
        size += char
    return size

size = window_size("550 x 300 + 550 + 250")

win.geometry(size)
win.minsize(width=500, height=250)

win.title("Grid 網格布局")


user_label = Label(text="User", font=("微軟正黑體", 20))
password_label = Label(text="Password", font=("微軟正黑體", 20))
user_label.grid(column=0, row=0)
# password_label.grid(column=0, row=1)


user_entry = Entry(font=("微軟正黑體", 20))
password_entry = Entry(font=("微軟正黑體", 20))
# user_entry.grid(column=1, row=0)
# user_entry.grid(column=1, row=0, rowspan=2)
# password_entry.grid(column=1, row=1)


win.mainloop()