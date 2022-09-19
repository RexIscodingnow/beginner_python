import numpy as array

# 逐元運算 (elementwise)
# data1 = array.array([3, 2, 10])
# data2 = array.array([1, 3, 6])

# result = data1 + data2
# print("加 ", result)

# result = data1 - data2
# print("減 ", result)

# result = data1 * data2
# print("乘 ", result)

# result = data1 / data2
# print("除 ", result)

# result = data1 > data2
# print("大於 ", result)

# result = data1 == data2
# print("是否相等 ", result)

# 矩陣運算 (matrix)
'''
內積: (1x2)+(3x(-2))  (1x(-1)+3x4)  1x3+3x1

應該是:
        |        |     | 2  -1  3 |
        |  1  3  |  •  |          |
        |        |     | -2  4  1 |  (橫排(每行) x 直排(每行)) ...... 還回去了，還是...睡著了沒聽到...
'''
# 1 x 2
# data1 = array.array([
#     [1, 3]
# ])
# # 2 x 3
# data2 = array.array([
#     [2, -1, 3],
#     [-2, 4, 1]
# ])
# 矩陣內積
# result = data1.dot(data2)
# result = data1 @ data2  # python 3.5 以上
# print("內積: ", result)

# 矩陣外積
'''
    外積: [(1 x 2)  (1 x -1)  (1 x 3)  (1 x -2)  (1 x 4)  (1 x 1)]
          [(3 x 2)  (3 x -1)  (3 x 3)  (3 x -2)  (3 x 4)  (3 x 1)]
'''
# result = array.outer(data1, data2)
# print("外積: ", result)


# 統計運算 (statistics)
data = array.array([
    [2, 1, 7],
    [-5, 3, 8]
])

# 總和
# result = data.sum()
# print("總和: ", result)

# 針對欄做總和 column  (針對第一個維度做總和)
# result = data.sum(axis=0)  # [(2+(-5))  (1+3)  (7+8)]
# print("欄的總和: ", result)

# 針對列做總和 row  (針對第二個維度做總和)
# result = data.sum(axis=1)  # [(2+1+7)  (-5+3+8)]
# print("列的總和: ", result)


# 最大值
# result = data.max()
# print("最大值: ", result)

# 平均數
# result = data.mean()
# print("平均數: ", result)

result = data.mean(axis=1)
print("列的平均數: ", result)


# 標準差
# result = data.std()
# print("標準差: ", result)

