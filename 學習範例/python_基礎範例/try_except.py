# 例外事件處裡

# 輸入值若無法轉換成數字，則重新輸入
while True:
    data = input("輸入一個數字: ")
    try:
        number = int(data)
        break

    # Exception => 一切的例外狀況
    except Exception:
        number = 0
        print("輸入錯誤，請重新輸入")

number = number ** 2

print(number)
