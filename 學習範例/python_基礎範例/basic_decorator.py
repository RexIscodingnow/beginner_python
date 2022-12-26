# # 定義裝飾器
# def demo(callback):
#     def run():
#         print("裝飾器中的函式")
#         # 該回乎函式，為被裝飾之普通函式
#         callback(3)

#     return run

# # 使用裝飾器
# @demo
# def use(n):
#     print("普通函式", n)

# use()

# 使用裝飾器 =. 1+2+3+......+50
# def addToFivety(callback):
#     def run():
#         # 要執行之片段
#         result = 0

#         for i in range(51):
#             result += i
        
#         callback(result)
#     return run

# 執行
# @addToFivety
# def showResult(n):
#     print("1 + 2 + 3 + ... + 50 = ", n)

# showResult()

'''
    1 ~ 48 產生隨機 7 碼之亂數器
'''
# from numpy import empty
# from random import randint
# def randSevenNumber(printResult):
#     def running():
#         number = 1
#         nums = empty([48])
#         result = empty([7])
#         for i in range(48):
#             nums[i] = number + i
        
#         for j in range(len(result)):
#             result[j] = randint(min(nums), max(nums))
        
#         printResult(result)
#     return running

# @randSevenNumber
# def result(nums):
#     print("隨機 7 碼 => ", nums)

# result()