'''
    發票號碼核對 (末三碼)
'''

import numpy as np

array = np.array([
    '120', 
    '913', 
    '936', 
    '738', 
    '205'
])

while True:
    number = input("輸入發票末 3 碼: ")

    if number in array:
        print("核對號碼!!\n", number)

    elif number == "00":
        print("結束~~")
        break

    elif not number:
        print("未輸入 \n")

    elif number not in array:
        print("試試下一張!!\n")