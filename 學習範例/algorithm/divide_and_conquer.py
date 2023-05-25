'''
algorithm: Divide and Conquer (各個擊破法 / 分而分治演算法)

簡單說明: 將大問題 "切成" 小問題，再各個解決掉，有需要的話，再把結果 "合併起來"

Divide and Conquer 是一種由上而下 (top-down) 的解題方式
如果是用 Recursion 的方式，必須在 problem-solving level 思考，
並讓系統去處理獲得答案的細節 (利用操作 Stack)

'''

import numpy as np


class Divide_and_Conquer:
    '''
    各個擊破法
    '''
    def binary_search(self, data, search, low: int, high: int):
        '''
        屬於 Tail Recursion

        Tail Recursion: 所有的運算，在遞迴呼叫前完成

        : param low: 搜尋範圍 (左)
        : param high: 搜尋範圍 (右)
        '''
        if low > high:
            return -1
        
        else:
            mid = int((low + high) / 2)

            if search < data[mid]:
                return self.binary_search(
                    data, search,
                    low, mid-1
                )
            elif search > data[mid]:
                return self.binary_search(
                    data, search,
                    mid+1, high
                )
            else:
                return mid

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
        return self._merge(left, right)

    
    def _merge(self, left: list | np.ndarray, right: list | np.ndarray):
        '''
        資料合併

        : param left: 左半邊 迭代資料
        : param right: 右半邊 迭代資料
        '''
        merged = None
        dtype = type(left)

        if dtype == list:
            merged = [None] * (len(left) + len(right))
        elif dtype == np.ndarray:
            merged = np.empty([len(left) + len(right)], type(left[0]))

        i = 0
        j = 0
        k = 0

        # merge
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged[k] = left[i]
                i += 1
            else:
                merged[k] = right[j]
                j += 1
            
            k += 1

        if i < len(left):   # 左半邊尚未放完
            while i < len(left):
                merged[k] = left[i]
                i += 1
                k += 1
        else:               # 右半邊尚未放完
            while j < len(right):
                merged[k] = right[j]
                j += 1
                k += 1
        
        return merged






