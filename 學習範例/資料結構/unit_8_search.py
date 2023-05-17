'''
Python Data Structure && algorithm: Search (搜尋)

'''

import numpy as np


class Search:
    def sequential_search(self, data, search):
        '''
        循序搜尋法 (又稱: 線性搜尋法)
        從頭到尾比對，效率差
        
        : rtype: bool
        
        Sort: False
        time Complexity: O(n)
        '''
        isFind = False

        # 寫法 1
        for i in range(len(data)):
            if search == data[i]:
                isFind = True

        # 寫法 2，比較 pythonic
        # for compare in data:
        #     if search == compare:
        #         isFind = True
        
        return isFind


    def binary_search(self, data, search):
        '''
        二分搜尋法

        
        : param data: **已經排序好的資料**
        : rtype: bool

        Time Complexity: O(log n)
        algorithm 類型: divide and conquer (分治法/分而分之演算法)
        '''
        left = 0
        right = len(data)

        while left <= right:
            mid = int((left + right) / 2)   # 取中央索引值
            if search < data[mid]:
                right = mid - 1
            
            elif search > data[mid]:
                left = mid + 1

            else:
                print("所處位置: ", mid)
                return True
        
        return False

    def interpolation_search(self, data, search):
        '''
        內插搜尋法 (插植搜尋法)
            -- 這是我的變異體
                        by 二分搜尋法 (X
        
        使用斜率公式
        '''
        pass


class HashTable:
    '''
    雜湊表

    key-value pair
    '''
    def __init__(self, capacity = 20, dtype=str):
        self._capacity = capacity
        self._CONSTANT = 10
        self._slot = 2
        self._keys = [[] for _ in range(self._capacity)]
        self._buckets = [[] for _ in range(self._capacity)]

        self.stored_size = 0   # 存入資料數量

    def view(self):
        print("keys:\n", self._keys)
        print("buckets:\n", self._buckets)


    def _hash_function(self, key: str):
        '''
        雜湊函數: MOD buckets

        : param key: 鍵
        '''
        i = 0
        hash_value = 0

        while i < len(key):
            hash_value += ord(key[i]) + self._CONSTANT
            i += 1
        
        return hash_value % self._capacity


    def put(self, key: str, value):
        '''
        放入雜湊表

        : param key: 鍵
        : param value: 存入數值
        '''
        if self.stored_size == self._capacity:
            raise Exception("Hash Table is full")
        
        index = self._hash_function(key)
        record = index   # recorded hash value from first hash
        
        # 發生碰撞
        while self._keys[index] != None:
            # key 被使用過，或繞一圈 --> 與第一次的雜湊值相同
            if self._keys[index] == key and index == record:
                print("Collision or Key is used")
                return

            # slot 尚未裝滿
            if len(self._buckets[index]) < self._slot:
                break

            else:
                key += str(self._CONSTANT)
                index = self._hash_function(key)

        self._keys[index].append(key)
        self._buckets[index].append(value)
        self.stored_size += 1

    
    def get(self, key: str):
        '''
        取資料

        : param key: 鍵
        '''
        index = self._hash_function(key)
        record = index

        while self._keys[index] != key:
            key += str(self._CONSTANT)
            index = self._hash_function(key)

        return self._buckets[index]


    def delete(self, key: str, value=None):
        '''
        刪除資料
        
        : param key: 鍵
        : param value: 指定資料刪除。預設未指定，清除整個 bucket
        '''
        index = self._hash_function(key)
        temp = index

        while self._keys[index] is not None:
            if self._keys[index] == key:
                target_bucket = self._buckets[index]   # 目標 bucket

                if value:
                    # 對 bucket 內部的槽 (slot) 做查找
                    # for i in range(self._slot):
                    #     if value == target_bucket[i]:
                    #         target_bucket[i] = None
                    target_bucket.remove(value)
                else:
                    target_bucket = None

                self.stored_size -= 1
                return True
            
            elif index == temp:
                return False

            key += str(self._CONSTANT)
            index = self._hash_function(key)




