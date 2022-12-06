'''
    if 判斷式
'''
# 輸入分數，獎勵機制
# 情境: 假設分數 100 分，得 1000 元 、 90 分，得 800 元 、 80 分，得 500 、 介於 80 ~ 61，得 300 元 ， 低於 60 分 ， 則回字串 "再加油 !"
try:
    # flag = True

    # while flag:
    print("輸入分數 => ")
    score = int(input())
    price = 0
    if score == 100:
        price = 1000

    elif score < 100 and score >= 90:
        price = 800

    elif score < 90 and score >= 80:
        price = 500

    elif score < 80 and score >= 60:
        price = 300

    else:
        price = 0
        print("再加油 !")

    print("獎勵 ", price, " 元\n")

except Exception:
    print("上限為 100，且為整數，請再輸入 !\n")