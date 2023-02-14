'''
Python 視窗程式設計

module: Tkinter
'''

from tkinter import Tk, Entry, Label, PhotoImage, Button, StringVar


# 建立主視窗
window = Tk()

window.title("主視窗")  # 視窗標題

# 視窗大小 ---> 直向 x 橫向 + X座標 + Y座標 *以字串型別輸入，算式不可有空格*   註解: + X座標 + Y座標  =>  從螢幕左上角算起，向右 + X軸、向下 + Y軸
win_size = "600 x 500 + 630 + 250"
win_size = win_size.split()     # split(): rtype -> list => 把有字元的部分一個一個分開 (去掉空字元)
size = ""
for char in win_size:
    size += char

# 視窗大小式設定
window.geometry(size)
# 背景顏色
window.config(background="skyblue")

# 視窗最大 與 最小
window.minsize(width=350, height=350)
# window.maxsize(width=750, height=750)

# 縮放可能性 resizable(width, height)    False => 不可縮放   True => 可縮放
# window.resizable(False, False)

# icon 圖示   .ico 副檔名
# window.iconbitmap("")   # 檔案路徑


'''
屬性設置

    1. -alpha => 透明度
    2. -topmost => 最上層顯示
'''
# 透明度
window.attributes("-alpha", 1)    # 透明  0 ~ 1  不透明

# 置頂 (最上層顯示)
window.attributes("-topmost", False)   # 布林值

'''
元件
'''

'''
    1. 按鈕
        Button()
            param text: 按鈕上的文字
         
         設置參數 (setting variable): config, pack
         
         config()
            : image: 圖片
            : text: 設定按鈕文字
            : font: 設定字型與大小
            : width: 設定寬度，單位是字元
            : height: 設定高度，單位是字元
            : padx: 設定左右空白的空間，單位是像素
            : pady: 設定上下空白的空間，單位是像素
            : background/bg: 設定背景顏色
            : foreground/fg: 設定文字顏色
            : command: 按鈕按下後所要執行的方法
                        放函式 (物件狀態，類似回呼函式的寫法)

         pack(): 布局元件 (這邊是 放置按鈕)

    2. 圖片
        PhotoImage()
            param file: 圖片檔案路徑, type String

    3. 功能連結
        3-1. Label() 標籤，以下為常用參數
                : text: 設定文字內容
                : font: 設定字型與大小
                        1. (字體樣式, 文字大小) , type Tuple
                        2. "字體樣式 字體大小", type string
                : width: 設定寬度，單位是字元
                : height: 設定高度，單位是字元
                : padx: 設定左右空白的空間，單位是像素
                : pady: 設定上下空白的空間，單位是像素
                : background/bg: 設定背景顏色
                : foreground/fg: 設定文字顏色
        
        3-2. Entry(): 輸入框
                : font: 設定字型與大小
                : width: 設定寬度，單位是字元
                : padx: 文字最左或最右與文字方塊邊框的間距，單位是像素
                : pady: 文字最上或最下與文字方塊邊框的間距，單位是像素
                : background/bg: 設定背景顏色
                : foreground/fg: 設定文字顏色
                : state: 設定是否可輸入文字，預設為NORMAL，表示可以輸入，若設定為DISABLED則無法輸入
                : show: 輸入文字時顯示的字元，例如用在輸入密碼時可設定show="*"以顯示星號

                Functions
                    1. get() => 取得輸入框的資料

                setting variable:
                    config()
                        param width: 寬度
                        param font: (字體樣式, 文字大小) , type Tuple

'''
# def hello():
#     print("hello")

# btn = Button(text="按我")
# btn.config(background="skyblue", width=20, height=5)

# # 引入圖片
# img = PhotoImage(file="") 
# # btn.config(image=img)

# # 功能引用 (使用函式)
# btn.config(command=hello)

# btn.pack()   # 放置


# 1. label  參數 => fg = "" 調整文字顏色
label = Label(master=window, text="這個是label", background="black", fg="white")
# txtVar = StringVar()
# label = Label(master=window, textvariable=txtVar, background="black", fg="white")
label.config(width=20, height=5, font=("Arial", 30))
label.pack()

# on_hit = False
# def submit():
#     # text = entry.get()
#     # button.config(text=text)
#     global on_hit
#     if on_hit == False:
#         on_hit = True
#         txtVar.set("")
#     else:
#         on_hit = False
#         txtVar.set("")

# 2. 輸入框 (Entry)
entry = Entry()
entry.config(width=20, font=('Arial', 25))
entry.insert(0, "輸入")
entry.pack()

# 執行函式  參數 => command = function()
# button = Button(text='Ok', command=submit)
# button.config(font=("Arial", 13))
# button.pack()



# 常駐主視窗 ** 要放在最後一行 **
window.mainloop()