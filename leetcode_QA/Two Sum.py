"""
title: Two Sum

Given an array of integers nums and an integer target,
    return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution,
    and you may not use the same element twice.

You can return the answer in any order.


Example 1:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
    Input: nums = [3,2,4], target = 6
    Output: [1,2]

Example 3:
    Input: nums = [3,3], target = 6
    Output: [0,1]
"""

class Solution:
    def twoSum(self, nums: list[int], target: int):
        '''
        1. 全部遍歷
        
        time complexity: O(n ^ 2)
        '''
        # 1-1. 加法版
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

        # 1-2. 減法版
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                if target - nums[i] == nums[j]:
                    return [i, j]

        '''
        2. hash map

        time complexity: O(n)
        '''
        numMap = {}

        for i in range(len(nums)):
            if target - nums[i] in numMap.keys():
                return [numMap.get(target - nums[i]), i]
            
            numMap[nums[i]] = i


solution = Solution()
nums = [2, 7, 11, 15]
target = 9
result = solution.twoSum(nums, target)
print(result)

nums = [3, 2, 4]
target = 6
result = solution.twoSum(nums, target)
print(result)