'''
    python 基本資料型態，整理
'''
# 1. 數字
# (1) 整數 
123, 8, 561, 55

# (2) 浮點數 --> 就是小數
52.5454, 2.5, 88.888

# 2. 布林值
# --> True : 條件成立, 判斷給過 之類的
#     False : 條件不成立, 判斷不給過 之類的
True, False

# 3. 列表 : 一群資料，" 有順序 "
# (1) 稱為 " list " 的列表，可以 *更改*, *變動* [ ] 中資料
[5, 54, 6551, 222, 61]
#0,  1,  2,   3,   4 
["hello 你好嗎? 衷心感謝，自己接下去(誤)"]


# (2) 稱為 " Tuple " 的列表，不能 *更改*, *變動* ( ) 中資料
x = (21, 23, 623, 626, 25)
("hello 你好嗎? 衷心感謝，自己接下去(誤)")
# print(x[2])

# 4. 集合 & 字典
# (1) 集合 : 一群資料， " 沒有順序性 "
{1, 2, 3, 4, 5}

# * 在集合使用字串要先用 set() 再放入喔~~ 範例 : set(" 字串 ") *
set("hello")

# 集合運算
# 集合的運算
# s1 = {3,4,5}
# print(3 in s1)
# print(10 not in s1)
s1 = {3, 4, 5}
s2 = {4, 5, 6, 7}
# s3 = s1 & s2  # 交集 => 取兩集合中，相同的資料
# s3 = s1 | s2  # 聯集 => 取兩集合中的所有資料，但不重複
# s3 = s1 - s2  # 差集 => 從 s1 中，減去和 s2 重疊的部分
s3 = s1 ^ s2  # 反交集 => 取兩集合中，不重疊的部分
# print(s3)
# s = set("Hello")  # set(字串) => 重複的只 print 1個

# (2) 字典 : 一群資料 A 跟 B 對應 (兩兩成對)
{"apple": "蘋果", "debug": "解決錯誤(bug)"}
{1: 4, 2: 5, 3: 6}

# 5. 字串
"hello"
"hello 你好嗎? 衷心感謝，自己接下去(誤)"

# 6. 輸入資料
# x1 = int(input("輸入整數: "))
# print(x1)