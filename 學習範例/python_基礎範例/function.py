# 定義函式
#  函式內部的程式碼，若沒有做函式呼叫，就不會執行
# def multiply(n1,n2):
#     #print(n1*n2)
#     return n1*n2
# 呼叫函式
# value = multiply(3,4) + multiply(10,5)
# print(value)
# multiply(3,4)
# multiply(10,8)

# 程式的包裝
#  1+....+10
#  1+.......+20
# sum = 0
# for n in range(1,11):
#     sum = sum + n
# print(sum)
# def calculate(max):
#     sum = 0
#     for n in range(1,max + 1):
#         sum = sum + n
#     print(sum)

# calculate(10)
# calculate(20)

# 函式進階玩法
#  參數預設資料用法
# def power(base,exp = 0):
#     print(base**exp)
# power(3,2)
# power(4)
#  使用參數名稱對應
# def divide(n1,n2):
#     print(n1/n2)
# divide(2,4)
# divide(n2 = 2,n1 = 4)
#  無限/不定 參數資料 => 資料型態: Tuple
# def avg(*ns):
#     print(ns)
#     sum = 0
#     for n in ns:
#         sum = sum + n
#     print(sum / len(ns))
# avg(3,4)
# avg(1,4,-1,-8)
# avg(3,5,10)