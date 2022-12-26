'''
    Numpy 陣列運算
'''


import numpy as array


'''
    切片操作

    陣列操作[起始: 終止: 間隔] = 要變更的值
'''

# 1. 一維操作

# 位置取值
arr5 = array.arange(10)
# print("原陣列:")
# print(arr5)

# print(arr5[2])

# 一維切片
arr5[: 5] = 10
# print(arr5)

arr5[2: 6] = 5
# print("2 ~ 5 之索引值，值改 5:")
# print(arr5)

arr5[3: 9: 2] = 1
# print("3 ~ 8 之索引值，每隔 2 個，值改 1:")    # 從起始值開始算起，每隔 2 個，指派數值
# print(arr5)


# 2. 多維操作

# data_nd = array.arange(1, 7).reshape(2, 3)   # 1 ~ 6, 2x3 array
# print("2x3 原陣列")
# print(data_nd)
# print("------------------------")
# 2-1. 位置
# print("取值 (位置)")
# print("第 (0, 1) 位置 => 2")
# print(data_nd[0, 1])   # data[0][1]
# print("第 (1, 2) 位置 => 6")
# print(data_nd[1, 2])   # data[1][2]

# 2-2. 切片

# nd_arr = array.array([
#     [123, 456, 789], [1234, 4567, 7890],
#     [12345, 56789, 90123], [345678, 89012, 234567]
# ])

# print(nd_arr.shape)
# print(nd_arr[1: 3, 0: 2])   # [[1234, 4567], [12345, 56789]]
# print(nd_arr[:2, 2])   # [789, 7890]

# 使用 ... 切片，取得全部，也就表示我全都要(X
nd_arr2 = array.array([
    [
        [0, 1, 2],
        [3, 4, 5]
    ],
    [
        [-1, -5, 6],
        [8, 7, 9]
    ]
])

# print(nd_arr2[0, ...])   # [[0, 1, 2], [3, 5, 6]]
# print("------------------------")
# print(nd_arr2[..., 1: 3])   # [[[1, 2], [4, 5]], [[-5, 6], [7, 9]]]


'''
    布林陣列篩選值
'''

origin_arr = array.arange(10)

bool_arr = origin_arr < 5

# print("------------------------")
# print("原陣列:")
# print(origin_arr)
# print("------------------------")
# print("布林陣列:")
# print(bool_arr)
# print("------------------------")
# print("用 布林陣列 篩選值")
# print(origin_arr[bool_arr])







'''
    逐元運算 (elementwise)

    先決條件: 陣列長度、形狀，要一樣
'''
data1 = array.array([3, 2, 10])
data2 = array.array([1, 3, 6])

# result = data1 + data2
# print("加 => ", result)

# result = data1 - data2
# print("減 => ", result)

# result = data1 * data2
# print("乘 => ", result)

# result = data1 / data2
# print("除 => ", result)

result = data1 ** 2
# print("data1 陣列做 2 次方", result)

# result = data1 > data2
# print("大於 => ", result)

# result = data1 == data2
# print("是否相等 => ", result)

# 矩陣運算 (matrix)
'''
內積: (1x2)+(3x(-2))  (1x(-1)+3x4)  1x3+3x1

應該是:
        |        |     | 2  -1  3 |
        |  1  3  |  •  |          |
        |        |     | -2  4  1 |  (橫排(每行) x 直排(每行)) ...... 還回去了，還是...睡著了沒聽到...
'''
# 1 x 2
data1 = array.array([
    [1, 3]
])
# # 2 x 3
data2 = array.array([
    [2, -1, 3],
    [-2, 4, 1]
])
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
# print("外積: ")
# print(result)

# 統計運算 (statistics)
data = array.array([
    [2, 1, 7],
    [-5, 3, 8]
])

# 總和
# result = data.sum()
# print("總和: ", result)

'''
axis = 0: 針對欄做總和 column  (針對第一個維度做總和)
    例子: 像是 2 個一維陣列 做相加
            data = array.array([
                [1, 2, 3],
                [4, 5, 6]
            ])
            data1 = array.array([1, 2, 3])
            data2 = array.array([4, 5, 6])
            
            data.sum(axis=0)  ==  data1 + data2


axis = 1: 針對列做總和 row  (針對第二個維度做總和)
    例子: 2 維陣列內，所有 1 維陣列 "做相加"
            data = array.array([
                [1, 2, 3],  # 這一列相加  1 + 2 + 3
                [4, 5, 6]   # 同理       4 + 5 + 6
            ])
            data.sum(axis=1)    # 結果 => [6, 15]
'''
# result = data.sum(axis=0)  # [(2+(-5))  (1+3)  (7+8)]
# print("欄的總和: ", result)

result = data.sum(axis=1)  # [(2+1+7)  (-5+3+8)]
# print("列的總和: ", result)

# 最大值
# result = data.max()
# print("最大值: ", result)

# 平均數
# result = data.mean()
# print("平均數: ", result)

# result = data.mean(axis=1)
# print("列的平均數: ", result)

# 標準差
# result = data.std()
# print("標準差: ", result)

