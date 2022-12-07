'''
Python NumPy 陣列操作，函式篇
'''

import numpy as np

'''
    亂數產生

    1. numpy.random.randn(陣列長度)  ==>  產生一組隨機數值的陣列
    2. numpy.random.randint(最小值, 最大值, 陣列長度, 型別)  ==>  指定範圍值，亂數陣列
    3. numpy.random.seed( 整數型別 )  ==>  亂數種子，產生固定的亂數
    4. numpy.random.rand(陣列長度)  ==>  產生一組 0 ~ 1 之間的亂數陣列
    5. numpy.random.choice(類似陣列之型別, 長度(挑選數量))  ==>  返回隨機挑選長度的 陣列
'''

x = np.random.randn(5)
y = np.random.randn(5)
z = np.random.randn()

# print("x: ", x)
# print("y: ", y)
# print("z: ", z)

times = 6
np.random.seed(times)
x = np.random.randn(5)

np.random.seed(0)
y = np.random.randn(5)

# print(f"x (seed = {times}): ", x)
# print("y (seed = 0): ", y)


arr1 = np.random.randint(0, 11, (3, 5))
# print("arr1:")
# print(arr1)

arr2 = np.random.rand(3)
# print("arr2:")
# print(arr2)

a = [123, 456, 789, 564987, 8794]
arr3 = np.random.choice(a, len(a) - 2)
# print(arr3)


'''
    陣列複製
        說明: 直接 把陣列指派給 新的陣列，其實是把 "陣列的每個索引值" 的 "記憶體位址"，給新的陣列使用
              這也說明了 "你家就是我家，我家就是你家。 我動了一個，你也跟著動了一個"
'''

data = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

# print("------------------------")
# print("原先陣列數值")
# print(data)
# print("------------------------")

# 錯誤操作: 直接指派過去
copy_new_array_1 = data

copy_new_array_2 = data.copy()


for i in range(2):
    for j in range(3):
        copy_new_array_1[i][j] += 1

# print("直接指派 (指派過去的):")
# print(copy_new_array_1)
# print("------------------------")
# print("直接指派 (原陣列)")
# print(data)
# print("------------------------")
# print("使用 copy() 函式:")
# print(copy_new_array_2)



'''
    切片操作

    陣列操作[起始: 終止: 間隔] = 要變更的值
'''

arr5 = np.arange(1, 11)
# print("原陣列:")
# print(arr5)

arr5[2: 6] = 5
# print("2 ~ 5 之索引值，值改 5:")
# print(arr5)

arr5[3: 9: 2] = 1
# print("3 ~ 8 之索引值，每隔 2 個，值改 1:")    # 從起始值開始算起，每隔 2 個，指派數值
# print(arr5)


'''
    布林陣列篩選值
'''


origin_arr = np.arange(10)

bool_arr = origin_arr < 5

# print("------------------------")
# print("原陣列:")
# print(origin_arr)
# print("------------------------")
# print("布林陣列:")
# print(bool_arr)




