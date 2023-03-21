'''
    多軸陣列 (axis)，或稱為 多維陣列

                            最外層
    axis = 0  =>  最外層       ↑
    axis = 1  =>  第二層       |
    axis = 2  =>  第三層       |
    axis = n  =>  第 n 層      ↓
                            最內層
'''

import numpy as np

'''
    陣列型狀 操作 與 屬性

    1. 陣列.shape     => 取得當下 "陣列形狀"
    2. 陣列.T         => 資料轉置，行列反轉
    3. 陣列.ravel()   => 扁平化，高維陣列 轉到 一維，資料不變
    4. 陣列.reshape() => 參數: 目標形狀，改動陣列形狀。
                        注意: 改動的目標陣列，個數一定要一樣!!
                                ex: 2 x 3  =>  reshape(6) : 正確  or  reshape(2, 4) : 錯誤
'''

# original_arr = np.array([
#     [12, 13, 465],
#     [45, 54, 789]
# ])

# print("原陣列")
# print("形狀 => ", original_arr.shape)
# print(original_arr)
# print("------------------------")
# print("反轉後 (屬性 T)")
# print("形狀 => ", original_arr.T.shape)
# print(original_arr.T)
# print("------------------------")
# new_arr = original_arr.ravel()
# print("形狀 => ", new_arr.shape)
# print(new_arr)
# print("------------------------")
# reshape_arr = original_arr.reshape(3, 2)
# print("改變後的形狀", reshape_arr.shape)
# print(reshape_arr)
# reshape_arr = original_arr.reshape(2, 4)   # 錯誤

# data = np.zeros(18).reshape(3, 6)
# num = 1
# for i in range(data.shape[0]):
#     for j in range(data.shape[1]):
#         data[i][j] = num
#         num += 1
# data = np.arange(1, 19).reshape(3, 6)
# print(data)



'''
    軸 (axis)
'''
# origin_nd_arr = np.zeros([2, 3], dtype=int)

# k = 0
# for i in range(origin_nd_arr.shape[0]):
#     for j in range(origin_nd_arr.shape[1]):
#         k += 1
#         origin_nd_arr[i][j] = k


# sum_axis_0 = origin_nd_arr.sum(axis=0)
# sum_axis_1 = origin_nd_arr.sum(axis=1)


# print("原陣列")
# print(origin_nd_arr)
# print("----------------------")
# print("axis = 0 相加")
# print(sum_axis_0)
# print("----------------------")
# print("axis = 1 相加")
# print(sum_axis_1)





