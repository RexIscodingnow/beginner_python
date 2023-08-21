"""
title: Longest Subarray of 1's After Deleting One Element

Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array.

Return 0 if there is no such subarray.


Example 1:
    Input: nums = [1,1,0,1]
    Output: 3
    Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.

Example 2:
    Input: nums = [0,1,1,1,0,1,1,0,1]
    Output: 5
    Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].

Example 3:

    Input: nums = [1,1,1]
    Output: 2
    Explanation: You must delete one element.
"""


class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        """
        解題方式: sliding window

        思路: 先遍歷過一次，去紀錄 0 的位置
            
            1. 在陣列 nums 裡面

                -- 1-1. 都沒有 0   =>  刪掉一個
                -- 1-2. 只有 1 個  =>  一樣刪掉一個
                -- 1-3. 2 個以上   =>  使用 sliding window

            第二次遍歷 nums

            2. sliding window 的窗口內部，只允許 1 個 0 在裡面
                    
                如果有 2 個的話，就把其中一個 0 忽略掉
                    再計算 (subarray 的總長度 - 1) 

            在窗口內
                
                -- 2-1. 數值是 1    =>  繼續擴大

                    (0 的個數)
                -- 2-2. 只有 1 個   =>  繼續擴大
                -- 2-3. 有 2 個在內 =>  減去忽略掉的，取 subarray 總長 - 1
        """

        n = len(nums)
        max_length = 0

        zeros = []

        for i in range(n):
            if nums[i] == 0:
                zeros.append(i)

        if len(zeros) <= 1:
            return n - 1

        start = 0
        end = 0

        i = 0
        count = 0

        while end < n:
            if nums[end] == 0 and count <= 1:
                count += 1

            if count > 1:
                max_length = max(end - start - 1, max_length)

                start = zeros[i] + 1
                count -= 1
                i += 1
            
            end += 1

        max_length = max(end - start - count, max_length)

        return max_length


solution = Solution()

nums = [1,1,0,1]
result = solution.longestSubarray(nums)
print(result)

nums = [0,1,1,1,0,1,1,0,1]
result = solution.longestSubarray(nums)
print(result)

nums = [1,1,1]
result = solution.longestSubarray(nums)
print(result)

nums = [1,1,0,0,1,1,1,0,1]
result = solution.longestSubarray(nums)
print(result)