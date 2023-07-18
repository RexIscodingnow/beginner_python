'''
Python Data Structure && algorithm: Sort (排序)

'''

import numpy as np
import math


class Sorting:
    '''
    傳入參數，使用 NumPy NDArray

    Here is for one dimensional array to sorting.
    '''
    def __init__(self):
        self.data = None

    def swap(self, a: int, b: int):
        '''
        : param a: the index of first element
        : param b: the index of second element
        '''
        temp = self.data[a]
        self.data[a] = self.data[b]
        self.data[b] = temp


    def bubble_sort(self, data):
        '''
        1D array 泡沫排序法
                -- 挨家挨戶的叫鄰居們比大小，前面比我小的排在我後面

        Time Complexity: O(n ^ 2)
        Space Complexity: O(1)
        '''
        self.data = data

        for i in range(len(data)):
            for j in range(i+1, len(data)):
                if data[i] > data[j]:
                    self.swap(i, j)


    def selection_sort(self, data):
        '''
        選擇排序法 (不穩定)
        類似於 bubble sort 的結構 (by for loop)
                -- 前面最小的，跟我交換位置 (不用挨家挨戶的叫隔壁)

        Time Complexity: O(n ^ 2)
        Space Complexity: O(1)
        '''
        self.data = data

        for i in range(len(data)):
            min_index = i   # 設置最小值 (索引值)

            for j in range(i, len(data)):
                if data[j] < data[min_index]:   # 從 (i + 1) ~ 最底部的範圍，找出最小值
                    min_index = j

            if min_index != i:
                self.swap(i, min_index)


    def insert_sort(self, data):
        '''
        插入排序法 (穩定)

        Time Complexity: O(n ^ 2)
        Space Complexity: O(1)
        '''
        for i in range(1, len(data)):
            insert_val = data[i]   # 待插入的數值
            insert_index = i - 1   # 已排序部分的最後一個索引

            # 比 insert_val 大的數值往後移動
            while insert_index >= 0 and insert_val < data[insert_index]:
                data[insert_index+1] = data[insert_index]
                # print(f"i: {i}", "data[j+1]:", data[j+1], " data[j]:", data[j])

                insert_index -= 1

            # 把小的數值放到最前面
            data[insert_index+1] = insert_val
            
            # print(data)

    def radix_sort(self, data):
        """
        基數排序法

        : param data: mutable iterable data
        """
        if len(data) < 2:
            return
        

        """
        [170, 45, 75, 90, 802, 24, 2, 66]

        buckets 代表每一位數的數值: 0 ~ 9

        放入之位數: 個位數 ~ n 位數

            0   1   2   3   4   5   6   7   8   9
            [], [], [], [], [], [], [], [], [], []
        """
        buckets = [[] for _ in range(10)]
        max_digit = len(str(max(data)))   # 取最大數的總位數

        temp_digit = 1

        for _ in range(1, max_digit):   # digit 作為基數，從個位數開始排序
            divide = 10 ** temp_digit

            for i in range(len(data)):
                index = data[i] % divide
                print(index)


            temp_digit += 1


    def quick_sort(self, data, left, right):
        '''
        1D array 快速排序法 (不穩定)
                -- 第一波: 處理完全體，開切完全體
                   第二波: 處理兩邊分靈體，又再切一次
                   第三波: 分靈體變小(還是兩個分靈體)
                   
                   以此類推，把分靈體切到不能再切
        
        : param data: 排序資料
        : param left: 左邊指標 (切分狀態的所處位置)
        : param right: 右邊指飆 (切分狀態的所處位置)

        Time Complexity: O(n log n)
        Space Complexity: O(log n) ~ O(n)
        algorithm 類型: divide and conquer (分治法/分而分治之/各個擊破 演算法)
        '''
        if left >= right:   # 左邊的指標超過右邊，意味著排好，中斷執行
            return

        self.data = data

        i = left    # 左邊區域
        j = right   # 右邊區域
        pivot = data[left]  # 基準點

        while i != j:
            # 找到及停住
            while data[j] >= pivot and i < j:   # 比基準點大，往左邊靠攏
                j -= 1
            while data[i] <= pivot and i < j:   # 比基準點小，往右邊靠攏
                i += 1
            
            # 在兩個指標尚未相遇之時，兩指標值交換
            if i < j:
                self.swap(i, j)

        # 基準點更換，值為當前位於左邊的指標值
        data[left] = data[i]
        data[i] = pivot

        # 切成兩塊區域
        # 1. 左半邊數值偏小
        # 2. 右半邊數值偏大
        self.quick_sort(data, left, i-1)    # 左邊半邊，往左內縮
        self.quick_sort(data, i+1, right)   # 右邊半邊，往右內縮


    def merge_sort(self, data: list | np.ndarray):
        '''
        合併排序法 (穩定)

        : param data: 排序資料

        Time Complexity: O(n log n)
        Space Complexity: O(n)
        '''
        # 1. 切分
        #   遞迴法
        if len(data) <= 1:
            return data

        mid = len(data) // 2

        left = self.merge_sort(data[: mid])
        right = self.merge_sort(data[mid: ])

        # 2. merge
        return self.merge(left, right)

    
    def merge(self, left: list | np.ndarray, right: list | np.ndarray, merged=None):
        '''
        合併
        '''
        out_param = False
        dtype = type(left)

        if merged == None:
            if dtype == list:
                merged = [None] * (len(left) + len(right))
            elif dtype == np.ndarray:
                merged = np.empty([len(left) + len(right)], type(left[0]))

            out_param = True

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged[k] = left[i]
                i += 1
            else:
                merged[k] = right[j]
                j += 1
            
            k += 1

        if i < len(left):
            while i < len(left):
                merged[k] = left[i]
                i += 1
                k += 1
        else:
            while j < len(right):
                merged[k] = right[j]
                j += 1
                k += 1
        
        if out_param:
            return merged


    def slicing(self, data: list | np.ndarray, divide_size: int = 2, sort: bool = True):
        '''
        切資料 (experiment)

        : param data: 處理資料 1D array
        : type data: list | numpy.ndarray
    
        : param divide_size: 切分總份數
        : type divide_size: int

        : param sort: 啟用排序，預設開啟
        : param sort: bool

        : rtype: list | np.ndarray
        '''
        if len(data) < 2:
            return data

        arrays = None   # 切分資料總存放區

        bucket = None   # 剩下未放入的資料副存放區
        length = len(data)
        divide_len = length // divide_size   # 切分後，單一份的長度
        remain_len = length - divide_size * divide_len

        # 依照型別，準備空間
        if type(data) == list:
            arrays = [[0] * divide_len for _ in range(divide_size)]
            if remain_len > 0:
                bucket = [] * remain_len
        
        elif type(data) == np.ndarray:
            arrays = np.empty([divide_size, divide_len], data[0])
            if remain_len > 0:
                bucket = np.empty([remain_len], data[0])

        count = 0
        for i in range(divide_size):
            for j in range(divide_len):
                arrays[i][j] = data[count]
                count += 1
        
        if bucket:
            k = 0
            while count < length:
                bucket[k] = data[count]
                count += 1
                k += 1

            if sort:
                # print("before (bucket):\n", bucket)
                self.quick_sort(bucket, 0, len(bucket) - 1)
                # print("after (bucket):\n", bucket)

        # print("before:\n", arrays)
        if sort:
            for i in range(divide_size): 
                self.quick_sort(arrays[i], 0, divide_len-1)

        # print("after:\n", arrays)

        return arrays, bucket
