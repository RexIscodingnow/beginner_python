# 迴圈進階控制
#  break
# n = 0
# while n < 5:
#     if n == 3:
#         break
#     print(n) # 迴圈中的 n
#     n += 1
# print("最後的 n:",n) # 迴圈結束的 n

#  continue
# n = 0
# for x in [0,1,2,3]:
#     if x % 2 == 0: # x 是偶數
#         continue
#     print(x)
#     n += 1
# print("最後的 n:",n)
#  else
# sum = 0
# for n in range(11):
#     sum += n
# else:
#     print(sum) # 印出 0+1+2+...+10

#  綜合範例: 找整數平方根
#  輸入 9 得到 3
#  輸入 11 得到 [沒有] 整數平方根
# n = input("請輸入正整數: ")
# n = int(n)  # 轉換成數字
# for i in range(n):
#     if i*i == n:
#         print("找到整數平方根:",i) # 用 break 強制結束迴圈，不會執行 else 區塊
#         break
# else:
#     print("沒有找到")