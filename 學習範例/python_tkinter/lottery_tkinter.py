'''
測試: 樂透 7 碼

'''

from tkinter import *
from random import randint


win = Tk()

def window_size(win_size: str):
    size = ""
    win_size = win_size.split()
    for char in win_size:
        size += char
    return size

WIDTH = "600"
HEIGHT = "500"

win.geometry(window_size(WIDTH + "x" + HEIGHT + " + 600 + 300"))
win.resizable(False, False)
win.configure(background="wheat")
win.title("威力彩 python  --試試你的手氣")


message_1 = Label(text="第一區選號區 01 ~ 38", font=("微軟正黑體", 20))
message_1.config(background="skyblue", width=17)
message_1.place(x=12, y=0)

message_2 = Label(text="第二區選號區 01 ~ 08", font=("微軟正黑體", 20))
message_2.config(background="skyblue", width=17)
message_2.place(x=310, y=0)

msgVar = StringVar()
start_msg = "選 6 個號碼 + 1 個特別號"
msgVar.set(start_msg)
msg = Label(textvariable=msgVar, font=("微軟正黑體", 20))
msg.config(background="deepskyblue", width=26)
msg.place(x=105, y=60)

num = []
entrys = 6
for i in range(entrys):
    num.append(Entry(font=("微軟正黑體", 20), bg="white", fg="black", width=3))

x = 55
for i in range(entrys):
    num[i].place(x=x, y=130)
    x += 55

# 特別號 (選號)
special_entry = Entry(font=("微軟正黑體", 20), bg="white", fg="black", width=3)
special_entry.place(x=470, y=130)


'''
顯示
'''
show_first_area = StringVar()
show_special_area = StringVar()

begin_str = "開獎區 (第一區)"
show_first_area.set(begin_str)

second_str = "特別號"
show_special_area.set(second_str)

lotteryNumbers_Label = Label(textvariable=show_first_area)
lotteryNumbers_Label.config(font=("微軟正黑體", 20), bg="skyblue", fg="black", width=19)
lotteryNumbers_Label.place(x=(int(WIDTH) / 2 - 235), y=200)

specialNumber_Label = Label(textvariable=show_special_area)
specialNumber_Label.config(font=("微軟正黑體", 20), bg="skyblue", fg="black", width=5)
specialNumber_Label.place(x=460, y=200)


'''
選號 & 兌獎
'''

def check_lotteryNumbers(choose_numbers: list, choose_special: int, randNums: list, randSpecial: int):
    length = len(randNums)
    win_nums = 0    # 第一區中獎號碼 數量
    
    temp = 0
    for i in range(length):
        for j in range(length):
            if choose_numbers[i] == randNums[j]:
                if temp in choose_numbers and temp in randNums:
                    index_own = choose_numbers.index(temp)
                    index_rand = randNums.index(temp)
                    choose_numbers[index_own] = 0
                    randNums[index_rand] = 0
                else:
                    temp = choose_numbers[i]
                    choose_numbers[i] = 0
                    randNums[j] = 0
                    win_nums += 1

    win_special = False
    if choose_special == randSpecial:
        win_special = True

    if win_nums == 6:
        if win_special: return "頭獎"
        else: return "貳獎"

    elif win_nums == 5:
        if win_special: return "參獎"
        else: return "肆獎"

    elif win_nums == 4:
        if win_special: return "伍獎"
        else: return "陸獎"
    
    elif win_nums == 3:
        if win_special: return "柒獎"
        else: return "玖獎"
    
    elif win_nums == 2 and win_special: return "捌獎"
    elif win_nums == 1 and win_special: return "普獎"

    else: return "沒中獎"

    # win_items = {
    #     "6": True, "6": False, "5": True,
    #     "5": False, "4": True, "4": False,
    #     "3": True, "2": True, "3": False,
    #     "1": True
    # }


def show_OwnNumber(first_area, special_area):
    '''
    電腦選號
    顯示: 第一區 + 特別號 之輸入框
    '''
    for i in range(entrys):
        num[i].insert(0, first_area[i])
    special_entry.insert(0, special_area)

def show_lotteryNumbers(rand_numbers: list, rand_special: int):
    '''
    開獎號
    顯示: Label 元件上
    '''
    length = len(rand_numbers)
    show_string = ""
    for i in range(length):
        if i < length - 1:
            show_string += (rand_numbers[i] + ", ")
        else:
            show_string += rand_numbers[i]

    show_first_area.set(show_string)
    show_special_area.set(rand_special)


def getInput_Number():
    first_area = []   # 第一區 自選號
    rand_numbers = []   # 第一區 結果
    
    is_typeIn = True

    i = 0
    while i < entrys:
        get_number = num[i].get()
        
        if get_number:
            if int(get_number) < 10 and get_number == "0" + str(int(get_number)):
                first_area.append(get_number)

            elif int(get_number) > 9:
                first_area.append(get_number)

            # 個位數 開頭忘記加 0 ，自動加
            else:
                first_area.append("0" + get_number)
        else:
            is_typeIn = False
            
            temp = []
            auto_choose = randint(1, 38)    # 電腦選號

            temp.append(auto_choose)

            # 含重複號碼 之可能性
            if auto_choose > 9:
                first_area.append(str(auto_choose))

            # 個位數 開頭忘記加 0 ，自動加
            else:
                first_area.append("0" + str(auto_choose))

            # 不重複號碼
            # if auto_choose not in temp:
            #     if auto_choose > 9:
            #         first_area.append(str(auto_choose))

            #     # 個位數 開頭忘記加 0 ，自動加
            #     else:
            #         first_area.append("0" + str(auto_choose))
            # else:
            #     pass
        i += 1
        
        # ---------------------------------------------------------------------------------------------
        # ---------------------------------------------------------------------------------------------
        # ---------------------------------------------------------------------------------------------

        # 第一區 (開獎)
        rand = randint(1, 38)
        if rand > 9:
            rand_numbers.append(str(rand))
        else:
            rand_numbers.append("0" + str(rand))

    # 特別號 (開獎)
    rand_special = "0" + str(randint(1, 8))
    special_number = special_entry.get()

    is_typeIn_last = True   # 最後的欄位，是否有輸入
    if special_number:
        if special_number != "0" + str(int(special_number)):
            special_number = "0" + special_number
    else:
        is_typeIn_last = False
        auto_special = "0" + str(randint(1, 8))
        special_number = auto_special

    if is_typeIn == False and is_typeIn_last == False:
        show_OwnNumber(first_area, special_number)
    elif is_typeIn == False and is_typeIn_last:
        show_OwnNumber(first_area, "")

    show_lotteryNumbers(rand_numbers, rand_special)

    msgVar.set(check_lotteryNumbers(
        first_area, special_number,
        rand_numbers, rand_special
    ))

    # print("選號")
    # print(first_area, end='    ')
    # print(special_number)
    # print("--------------------------------")
    # print("target")
    # print(rand_numbers, end='    ')
    # print(rand_special)


btn = Button(text="開獎", font=("微軟正黑體", 18))
btn.config(command=getInput_Number)
btn.place(x=(int(WIDTH) / 2 - 40), y=300)


def clear():
    show_first_area.set(begin_str)
    show_special_area.set(second_str)

clear_btn = Button(text="清除開獎區", font=("微軟正黑體", 18))
clear_btn.config(command=clear)
clear_btn.place(x=(int(WIDTH) / 2 - 77), y=380)



win.mainloop()

# from tkinter import ttk

# frame = ttk.Frame(win, padding=10)
# frame.grid()

# frame_label = ttk.Label(frame, text="hello world")
# frame_label.grid(column=0, row=0)

# frame_btn = ttk.Button(frame, text="Quit", command=win.destroy)
# frame_btn.grid(column=0, row=1)