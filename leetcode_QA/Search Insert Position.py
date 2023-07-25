"""
title: Search Insert Position

Given a sorted array of distinct integers and a target value,
return the index if the target is found.
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
    Input: nums = [1,3,5,6], target = 5
    Output: 2
Example 2:
    Input: nums = [1,3,5,6], target = 2
    Output: 1
Example 3:
    Input: nums = [1,3,5,6], target = 7
    Output: 4
"""


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        """
        algorithm: linear search
        time Complexity: O(n)
        """
        # 插入位置
        # position = 0

        # for i in range(len(nums)):
        #     if target == nums[i]:
        #         position = i
        #         break
            
        #     else:
        #         if target > nums[i]:
        #             position = len(nums)
        #         else:
        #             if (i == 0 and target < nums[0]) or (i > 0 and target > nums[i-1] and target < nums[i]):
        #                 position = i

        # return position

        """
        algorithm: binary search
        time complexity: O(log n)
        """
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = int((left + right) / 2)
            
            if target < nums[mid]:
                right = mid - 1

            elif target > nums[mid]:
                left = mid + 1

            else:
                return mid
        
        # target 不在 nums 裡面
        # 則是往插入位置逼近 (left == right)
        return left


solution = Solution()

nums = [2, 5]
target = 0
result = solution.searchInsert(nums, target)
print(result)

nums = [-1, 3, 5, 6]
target = 7
result = solution.searchInsert(nums, target)
print(result)

nums = [1, 3, 5, 6]
target = 2
result = solution.searchInsert(nums, target)
print(result)