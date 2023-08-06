"""
title: Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] is equal to
the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.


Example 1:
    Input: nums = [1,2,3,4]
    Output: [24,12,8,6]

Example 2:
    Input: nums = [-1,1,0,-3,3]
    Output: [0,0,9,0,0]
"""


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        

        """
        解法方式: Dynamic Programming

        Complexity
            -- time: O(n)
            -- space: O(n) => O(n) + O(n)  *註: 左、右方向乘積

        思路: 建立兩個方向的陣列乘積，也就是
                -- 1. 左 --> 右
                -- 2. 右 --> 左

            但是遍歷計算乘積，不包含頭部、尾部，以及當前元素
            而且要從 "往前一個位置" 開始計算
            
            好比左右夾擊的方式，將自身數值排開


            左 --> 右: 0 ~ i
            右 --> 左: i ~ (n-1)

            如下:

            遍歷位置:              i
                     nums = [1, 2, 3, 4, 5]
            
            紀錄起始點:         j
            left -> right = [1, 1, 1, 1, 1]
                             |  |
                             0  1  (0 ~ 1 乘積)

            紀錄起始點:               k
            right -> left = [1, 1, 1, 1, 1]
                                      |  |
                                      3  4  (4 ~ 3 乘積)
        """
        n = len(nums)
        answer = [1] * n
        left_product = [1] * n      # left --> right
        right_product = [1] * n     # right --> left

        # 不包含 nums[n-1] 的乘積
        for i in range(1, n):
            left_product[i] = left_product[i-1] * nums[i-1]

        # 不包含 nums[0] 的乘積
        for i in range(n-2, -1, -1):
            right_product[i] = right_product[i+1] * nums[i+1]


        for i in range(n):
            answer[i] = left_product[i] * right_product[i]

        # return answer


        """
        解法方式: Dynamic Programming (空間優化版)

        Complexity
            -- time: O(n)
            -- space: O(1)
        """
        n = len(nums)
        answer = [0] * n    # 建立資料表，儲存 nums[1] ~ nums[n-2] 的相乘

        answer[0] = 1

        # 寫入 nums[1] ~ nums[n-2] 的相乘
        # 也就是說，除了陣列 nums 只有最後一個，並沒有乘進去
        # 
        # 依照寫入的位置，對應 nums 的索引值
        # 相乘的數值，正是 0 ~ i 所有數相乘，但不包含 nums[i] 乘入
        # 
        for i in range(1, n):
            answer[i] = answer[i-1] * nums[i-1]

        right = 1

        for i in range(n-1, -1, -1):
            answer[i] *= right
            right *= nums[i]

        return answer


solution = Solution()

nums = [1,2,3,4]
result = solution.productExceptSelf(nums)
print(result)

nums = [-1,1,0,-3,3]
result = solution.productExceptSelf(nums)
print(result)