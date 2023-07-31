"""
title: Can Place Flowers

You have a long flowerbed in which some of the plots are planted, and some are not.
However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's,
where 0 means empty and 1 means not empty, and an integer n,
return true if n new flowers can be planted in the flowerbed without
violating the no-adjacent-flowers rule and false otherwise.

Example 1:
    Input: flowerbed = [1,0,0,0,1], n = 1
    Output: true

Example 2:
    Input: flowerbed = [1,0,0,0,1], n = 2
    Output: false
"""


class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """

        """
        解題方式: greedy algorithm

        思路: 在 flowerbed 陣列中其擺放模式，
                -- 在 1 與 1 的兩側，中間為 0 的位置，不能放入
                -- 在 0 與 0 的兩側，中間為 0 的位置，才能放入

            1. 遍歷的位置 i 索引，是介於 flowerbed 的中間部分 (不含頭尾)
                -- 皆為 0 的元素，必須為 3 個一組
            
            但是，
            
            2. 遍歷的位置 i 索引，只有在 flowerbed 的開頭 & 最尾部 (i = 0, i = len(flowerbed) - 1)
                -- 只需要 2 個一組，皆為 0 的元素

            當找到可以擺放的位置，
            就在該位置標記為 1，表示已使用
            並記錄標記數量            
        """
        length = len(flowerbed)
        
        if n == 0:
            return True
        
        if length == 1:            
            return flowerbed[0] == 0

        count = 0       # 可放入的數目
        result = True

        for i in range(length):
            # 最前面的兩項 & 最尾段的兩項
            if i == 0 or i == length - 2:
                if flowerbed[i] == 0 and flowerbed[i+1] == 0:
                    # 找到位置時，做標記
                    flowerbed[i] = 1
                    count += 1
            
            if flowerbed[i] == 1:
                continue

            else:
                # 檢視左右兩邊
                if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                    flowerbed[i] = 1
                    count += 1

        # print(count)
        # print("after:", flowerbed)

        if count < n:
            result = False
        
        return result


solution = Solution()

flowerbed = [1,0,0,0,1]
n = 1
result = solution.canPlaceFlowers(flowerbed, n)
print(result)

flowerbed = [1,0,0,0,1]
n = 2
result = solution.canPlaceFlowers(flowerbed, n)
print(result)

flowerbed = [0,0,0,0]
n = 2
result = solution.canPlaceFlowers(flowerbed, n)
print(result)