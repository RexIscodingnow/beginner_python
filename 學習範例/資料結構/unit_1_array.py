'''
Python Data Structure: Array (陣列)

    representation module of python: Numpy

    notes:
        1. Usually to stored the sequence of relevant dataType in continuous memory space.
        2. It's must to declare the fixed space, so it's easy to cuase to waste memory space.
        3. Read and modify within array is fast in processing time.
        4. Delete or Addition new element(s) must to move large amount of data.

    由於是連續性的資料，所以搜尋資料，抓陣列的 "記憶體位址" 作找尋。

    example: language => c/c++

    declare 1D array, length: 3 => int array[3] = {1, 2, 3};
            -------------
            | 1 | 2 | 3 |
            -------------
            ^
            |
address: 0xff33s


    2D array, column: 2, row: 3 => int arr2D[2][3] = {{1, 2, 3}, {4, 5, 6}}
    
    ** row 橫向, column 縱向 **

    -------------------------------------------
    | arr2D[0][0] | arr2D[0][1] | arr2D[0][2] |
    -------------------------------------------
    | arr2D[1][0] | arr2D[1][1] | arr2D[1][2] |
    -------------------------------------------

    2D --> 1D
    
    1. row-major
    ---------------
    | arr2D[0][0] |
    ---------------
    | arr2D[0][1] |
    ---------------
    ~~~~~~~~~~~~~~~
    ~~~~~~~~~~~~~~~
    ---------------
    | arr2D[1][2] |
    ---------------

    2. column-major
    ---------------
    | arr2D[0][0] |
    ---------------
    | arr2D[1][0] |
    ---------------
    | arr2D[0][1] |
    ---------------
    | arr2D[1][1] |
    ---------------
    ~~~~~~~~~~~~~~~
    ~~~~~~~~~~~~~~~
    ---------------
    | arr2D[1][2] |
    ---------------


'''

import numpy as np
import random


class ArrayOperation():
    '''
    陣列的 常用五種操作，如下
                1. read
                2. write
                3. insert
                4. delete
                5. copy
    '''
    def read(self, array, dimension=1):
        ''' 讀取 '''
        if dimension == 1:
            for i in range(array.shape[0]):
                print(array[i], end=' ')
        
        elif dimension == 2:
            for i in range(array.shape[0]):
                for j in range(array.shape[1]):
                    print(array[i][j], end=' ')
                print()

    def write(self, value, array, index: int| list, dimension):
        ''' 寫入 '''
        if dimension == 1:
            array[index] = value
            ArrayOperation.read(array, 1)

        elif dimension == 2:
            if type(value) == list:
                k = 0
                for i in range(array.shape[0]):
                    for j in range(array.shape[1]):
                        array[i][j] = value[k]
                        k += 1
            else:
                array[index[0]][index[1]] = value

    def insert(self, array, value, index: int| list):
        ''' 插入 '''
        length = array.shape[0]
        if index < length:
            for i in range(length-1, index, -1):
                array[i] = array[i-1]
            
            array[index] = value
            return array

        else:
            return 0

    def delete(self, array, index: int):
        '''
        0  1  2  3
           t
            <- <-
        '''
        length = array.shape[0]
        if index < length:
            for i in range(index, length-1):
                array[i] = array[i+1]
            
            array[length-1] = 0
            return array
        else:
            return 0

    def copy(self, array, dimension):
        if dimension == 1:
            new_array = np.empty(array.shape[0])
            for i in range(array.shape[0]):
                new_array[i] = array[i]
            return new_array

        elif dimension == 2:
            new_array = np.empty(array.shape[0] * array.shape[1])
            new_array.reshape(array.shape[0], array.shape[1])
            for i in range(array.shape[0]):
                for j in range(array.shape[1]):
                    new_array[i][j] = array[i][j]


class Row_Column(ArrayOperation):
    '''
    自訂陣列

    陣列 行與列
    2D ~ 3D array 為主，但 2D 為重點部分
    '''
    def __init__(self, depth=0, column=0, row=0, dtype=float):
        self.dtype = dtype
        if row > 0:
            self.array = np.empty([row], self.dtype)
            if column > 0:
                self.array = np.empty([column, row], self.dtype)
                if depth > 0:
                    self.array = np.empty([depth, column, row], self.dtype)
        else:
            raise ValueError("row 至少大於 0")

        self.shape = self.array.shape
        self.dimensional = len(self.shape)
        
    def custom_array(self, data: list = None):
        '''
        自訂陣列 數值
        '''
        if data:
            if self.dimensional == 1:
                for i in range(self.shape[0]):
                    self.array[i] = data[i]

            elif self.dimensional == 2:
                for i in range(self.shape[0]):
                    for j in range(self.shape[1]):
                        self.array[i][j] = data[i][j]

            elif self.dimensional == 3:
                for i in range(self.shape[0]):
                    for j in range(self.shape[1]):
                        for k in range(self.shape[2]):
                            self.array[i][j][k] = data[i][j][k]
        return self.array
    
    def rand(self, digits=5, positive=False):
        '''
        隨機數值 (不想自訂，讓其自產)

        origin range: -n <= x <= n  (x: random number)

        : param digits: 範圍總位數  default -> 5 位
        : param positive: 限制在正數範圍  --> 0 <= x <= n
        '''
        if digits < 1:
            raise Exception("It must be over 1 digits")

        min_range = self.dtype(-9.2345 * (10 ** digits) / 10)
        max_range = abs(min_range)
        
        if positive:
            min_range = 0
        # print(min_range)
        # print(max_range)

        if self.dimensional == 1:
            for i in range(self.shape[0]):
                if self.dtype == int:
                    self.array[i] = random.randint(min_range, max_range)
                elif self.dtype == float:
                    self.array[i] = random.uniform(min_range, max_range)
    
        elif self.dimensional == 2:
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    if self.dtype == int:
                        self.array[i][j] = random.randint(min_range, max_range)
                    elif self.dtype == float:
                        self.array[i][j] = random.uniform(min_range, max_range)

        elif self.dimensional == 3:
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    for k in range(self.shape[2]):
                        if self.dtype == int:
                            self.array[i][j][k] = random.randint(min_range, max_range)
                        elif self.dtype == float:
                            self.array[i][j][k] = random.uniform(min_range, max_range)

        return self.array

    def row_major(self):
        '''
        以列為主
        '''
        print(self.array)
        # ArrayOperation.read(self.array, 2)

    def column_major(self):
        '''
        以行為主
        '''
        pass

    def arrange(self, start=0):
        '''
        1D ~ 3D array 遞增給值 (安排)

        PS: 希望不太常用到 3D ...
        '''
        if self.dimensional == 1:
            for i in range(self.array.shape[0]):
                self.array[i] = start
                start += 1

        elif self.dimensional == 2:
            for i in range(self.array.shape[0]):
                for j in range(self.array.shape[1]):
                    self.array[i][j] = start
                    start += 1

        elif self.dimensional == 3:
            for i in range(self.array.shape[0]):
                for j in range(self.array.shape[1]):
                    for k in range(self.array.shape[2]):
                        self.array[i][j][k] = start
                        start += 1

        # print(self.array)
        return self.array

    # ---------------------------------------------------------------------------------
    # ---------------------------------------------------------------------------------
    # ---------------------------------------------------------------------------------
    def matrixAdd(self, array):
        '''
        矩陣相加
        注意: 行列要相等
        :param array: 矩陣
        '''
        shape_1, shape_2 = len(self.array.shape), len(array.shape)
        
        if shape_1 > 0 and shape_2 > 0:    # 矩陣大小是否 1 維以上
            if self.array.shape[0] == array.shape[0] and self.array.shape[1] == array.shape[1]:
                result = np.empty([self.array.shape[0], self.array.shape[1]], self.dtype)
                for i in range(self.array.shape[0]):
                    for j in range(self.array.shape[1]):
                        result[i][j] = self.array[i][j] + array[i][j]
                return result
            else:
                return
        else:
            return

    # ---------------------------------------------------------------------------------
    # ---------------------------------------------------------------------------------
    # ---------------------------------------------------------------------------------
    def binary_search(self, array, target):
        '''
        其他: 1D array 二分搜尋法
        
        **註 1: 陣列內的數值已做好排序大小為前提
        **註 2: 這裡的指標 非比 需熟悉不然頭痛的指標 (by 寫過 c++ 的我)
        
        運行步驟如下
            number.close();
            1. 指標_1 向右比對，比目標數值小

        初始圖解
            1   3   5   7   9   12   15   18   20
            |-----------------------------------|
            ^           ^                       ^
            |           |                       |
          指標_1      中央點                  指標_2
        '''
        shape = len(array.shape)
        if shape == 1:
            # 設置 基準點 for 頭尾 
            left, right = 0, array.shape[0] - 1
            while left <= right:
                # 設立 中央點
                middle = int((left + right) / 2)
                if target < array[middle]:
                    right = middle - 1

                elif target > array[middle]:
                    left = middle + 1
                
                else:
                    return middle
            return -1

        return

    def bubble_sort(self):
        '''
        1D array 泡沫排序法

        Big-O(n ^ 2)
        '''
        shape = len(self.array.shape)
        if shape == 1:
            for i in range(self.array.shape[0]):
                for j in range(i, self.array.shape[0]):
                    if self.array[i] > self.array[j]:
                        temp = self.array[j]
                        self.array[j] = self.array[i]
                        self.array[i] = temp

            print("bubble sort")
            print(self.array)

    def selection_sort(self):
        '''
        1D array 選擇排序法

        Big-O(n ^ 2)
        '''
        shape = len(self.array.shape)

        if shape == 1:
            for i in range(self.array.shape[0]):
                min_index = i
                for j in range(i+1, self.array.shape[0]):
                    if self.array[j] < self.array[min_index]:
                        min_index = j

                if min_index != i:
                    # swap
                    temp = self.array[i]
                    self.array[i] = self.array[min_index]
                    self.array[min_index] = temp

        return self.array




