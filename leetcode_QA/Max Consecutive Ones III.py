"""
title: Max Consecutive Ones III

Given a binary array nums and an integer k,
return the maximum number of consecutive 1's in the array if you can flip at most k 0's.


Example 1:
    Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
    Output: 6
    Explanation: [1,1,1,0,0,1,1,1,1,1,1]
                            -----------
                            ^         ^
    Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Example 2:
    Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
    Output: 10
    Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
                      -------------------
                          ^ ^       ^
    Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.


** Bolded numbers: by "Up Arrow" position
"""


class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        """
        解題方式: sliding window
        """
        
        """
        Complexity
            -- time: O(n * k)
            -- space: O(k)

        n: length of array nums
        k: length of array zeros (to store index of element of zero)
        """

        # n = len(nums)
        
        # # 建立儲存 0 的索引值的表格
        # zeros = []
        # for i in range(n):
        #     if nums[i] == 0:
        #         zeros.append(i)

        # # print("zeros:", zeros)
        # # print()
        
        # # 初始化窗口的起始索引和結束索引
        # start = 0
        # end = 0
        
        # i = 0
        # max_length = 0
        
        # while end < n:
        #     # 0 的個數 (只限於 sliding window 範圍內)
        #     zeros_inside = []
        #     for idx in zeros:
        #         if start <= idx and idx <= end:
        #             zeros_inside.append(idx)
            

        #     if len(zeros_inside) <= k:
        #         max_length = max(max_length, end - start + 1)
        #         end += 1

        #     else:
        #         start = zeros[i] + 1
        #         i += 1
        
        # return max_length


        """
        上方的思路再 code review

        1. 拿掉
            -- 建立儲存 0 之索引值表格

        2. 改成
            -- 計算剩餘未填入的數量
        
        修改 sliding window 大小


        Complexity:
            -- time: O(n)
            -- space: O(1)
        """
        
        n = len(nums)
        
        start = 0
        end = 0

        while end < n:
            # 遞減，剩餘未填入的數量
            if nums[end] == 0:
                k -= 1

            if k < 0:
                # 為 0，則 剩餘數量 + 1
                if nums[start] == 0:
                    k += 1

                start += 1

            end += 1

        return end - start


solution = Solution()

nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2             
result = solution.longestOnes(nums, k)
print(result)

nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3
result = solution.longestOnes(nums, k)
print(result)