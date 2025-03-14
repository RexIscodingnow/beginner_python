"""
title: Increasing Triplet Subsequence

Given an integer array nums,
return true if there exists a triple of indices (i, j, k)
such that i < j < k and nums[i] < nums[j] < nums[k].

If no such indices exists, return false.


Example 1:
    Input: nums = [1,2,3,4,5]
    Output: true
    Explanation: Any triplet where i < j < k is valid.

Example 2:
    Input: nums = [5,4,3,2,1]
    Output: false
    Explanation: No triplet exists.

Example 3:
    Input: nums = [2,1,5,0,4,6]
    Output: true
    Explanation: The triplet (3, 4, 5) is valid
                 because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.
"""

class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3:
            return False
        
        # small -> medium -> large
        first = second = float("inf")

        for i in range(len(nums)):
            if nums[i] <= first:
                first = nums[i]

            elif nums[i] <= second:
                second = nums[i]

            else:
                print(first, second, nums[i])
                return True
        
        return False


solution = Solution()

nums = [x for x in range(1, 6)]             # 1 ~ 5
result = solution.increasingTriplet(nums)
result = solution.increasingTriplet(nums)
print(result)

nums = [x for x in range(5, 0, -1)]         # 5 ~ 1
result = solution.increasingTriplet(nums)
print(result)

nums = [2,1,5,0,4,6]
result = solution.increasingTriplet(nums)
print(result)

nums = [2,4,-2,-3]
result = solution.increasingTriplet(nums)
print(result)