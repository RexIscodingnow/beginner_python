'''
隨機數字 生成器

使用 Tkinter
'''

from tkinter import Tk, Label, Entry, Button, StringVar
import random
import pyperclip    # 這邊用來 Ctrl + C 操作 (複製目標文字)


win = Tk()
win.title("隨機數字")


def window_size(win_size: str):
    size = ""
    win_size = win_size.split()
    for char in win_size:
        size += char
    return size

size = window_size("600 x 500")
win.geometry(size)
win.config(bg="black")

txtVar = StringVar()

def rand():
    try:
        min_num = int(min_entry.get())
        max_num = int(max_entry.get())
    except:
        min_num = float(min_entry.get())
        max_num = float(max_entry.get())

    result = random.randrange(min_num, max_num)
    txtVar.set("亂數: " + str(result))

def copy():
    # cget( 參數名稱 )
    copy_txt = result_num.cget("text")
    pyperclip.copy(copy_txt)


title_txt = Label(text="隨機數生成", fg="skyblue")
title_txt.config(font=("微軟正黑體", 25), bg="black")

min_range = Label(text="最小範圍數", fg="white", background="black")
min_range.config(font=("微軟正黑體", 20))

max_range = Label(text="最大範圍數", fg="white", background="black")
max_range.config(font=("微軟正黑體", 20))

min_entry = Entry()
min_entry.config(width=15, font=("微軟正黑體", 13))
max_entry = Entry()
max_entry.config(width=15, font=("微軟正黑體", 13))


result_num = Label(textvariable=txtVar, fg="white", background="black")
result_num.config(font=("微軟正黑體", 22))


generate_btn = Button(text="生成", command=rand)
generate_btn.config(font=("微軟正黑體", 15))
copy_btn = Button(text="複製", command=copy)
copy_btn.config(font=("微軟正黑體", 15))



'''
元件放置
'''
title_txt.pack()

min_range.pack()
min_entry.pack()

max_range.pack()
max_entry.pack()

result_num.pack()

generate_btn.pack()
copy_btn.pack()



win.mainloop()