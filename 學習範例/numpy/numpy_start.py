'''
    python 的陣列模組
'''

import numpy

# print(test_array.shape)

'''
    一維陣列
'''
# 建立 並 賦值
ar1 = numpy.array([54, 852, 845, 15])
# print(ar1)
# 使用 索引 => 指定該位置的值
# ar1[0] = 54,  ar1[3] = 15
# print(ar1[0])

# 給定長度 但 不賦值 (未定義行為)
# 直接印出會得到 記憶體位置
ar2 = numpy.empty(5)
# print(ar2)

# 給定長度 且 都賦值為 0
ar3 = numpy.zeros(3)
# print(ar3)

# 給定長度 且 都賦值為 1
ar4 = numpy.ones(3)
# print(ar4)

# 給定連續資料
ar5 = numpy.arange(5)
# print(ar5)

'''
    二維陣列
'''
# 建立 並 賦值
nd2_ar1 = numpy.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
# print(nd2_ar1)

# 給定長度 但 不賦值 (未定義行為)
# 直接印出會得到 記憶體位置
nd2_ar2 = numpy.empty([3, 3])
# print(nd2_ar2)

# 給定長度 且 都賦值為 0
nd2_ar3 = numpy.zeros([2, 3])
# print(nd2_ar3)

# 給定長度 且 都賦值為 1
nd2_ar4 = numpy.ones([2, 3])
# print(nd2_ar4)

'''
    三維陣列
'''
nd3_ar1 = numpy.array([
    [
        [3, 1], [3, 2]
    ],
    [
        [3, 3], [3, 4]
    ]
])
# print(nd3_ar1)

nd3_ar2 = numpy.zeros([2, 1, 2])
# print(nd3_ar2)

nd3_ar3 = numpy.ones([2, 1, 2])
# print(nd3_ar3)

'''
    高維陣列 (三維以上)
    一樣的做法
'''
nd4_ar1 = numpy.ones([2, 1, 1, 2])
print(nd4_ar1)


'''
    查看大小 使用 shape
'''
test_array = numpy.array([
    [
        [
            [1, 2, 3],
            [4, 5, 6]
        ],
        [
            [7, 8, 9],
            [10, 11, 12]
        ]
    ],
    [
        [
            [13, 14, 15],
            [16, 17, 18]
        ],
        [
            [19, 20, 21],
            [22, 23, 24]
        ]
    ]
])