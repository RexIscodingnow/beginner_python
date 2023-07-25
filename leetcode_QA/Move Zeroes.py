"""
title: Move Zeroes


Given an integer array nums,
move all 0's to the end of it
while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:
    Input: nums = [0,1,0,3,12]
    Output: [1,3,12,0,0]

Example 2:
    Input: nums = [0]
    Output: [0]
"""


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        count = 0

        for i in range(n):
            if nums[i] != 0:
                temp = nums[i]
                nums[i] = nums[count]
                nums[count] = temp

                count += 1

            print(nums)


        print(nums)


solution = Solution()

nums = [0, 1, 0, 3, 12]
solution.moveZeroes(nums)

nums = [0, 0, 1]
solution.moveZeroes(nums)

nums = [5, 6, 8, 0, 9, 0, 10]
solution.moveZeroes(nums)