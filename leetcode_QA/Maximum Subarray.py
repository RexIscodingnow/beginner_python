"""
title: Maximum Subarray

Given an integer array nums, find the subarray with the largest sum, and return its sum.

Explanation subarray:
    -- A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
    Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
    Output: 6
    Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:
    Input: nums = [1]
    Output: 1
    Explanation: The subarray [1] has the largest sum 1.

Example 3:
    Input: nums = [5,4,-1,7,8]
    Output: 23
    Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
"""


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)

        if length == 1:
            return nums[0]

        # 最大加總值 = 當前計算加總值
        # 初始值，皆從陣列開頭的數值
        sub_max = sub_sum = nums[0]
        
        for i in range(1, length):
            # 累加當下的加總值
            sub_sum += nums[i]

            """
            方式 1
            """
            # 假如現在 "遍歷的位置 i 的數值" > "前面累加的加總值"
            # 則是砍掉重計，從位置 i 的數值，重新累加
            if sub_sum < nums[i]:
                sub_sum = nums[i]

            # 假如 "前面累加的加總值" > "最大加總值"
            # 則更新 "最大加總值"
            if sub_sum > sub_max:
                sub_max = sub_sum
            

            """
            方式 2
            """
            # sub_max = max(sub_sum, sub_max)
            # sub_sum = max(sub_sum, nums[i])


        return sub_max


solution = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
result = solution.maxSubArray(nums)
print(result)

nums = [1]
result = solution.maxSubArray(nums)
print(result)

nums = [5,4,-1,7,8]
result = solution.maxSubArray(nums)
print(result)