"""
title: Max Number of K-Sum Pairs

You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array
whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.


Example 1:
    Input: nums = [1,2,3,4], k = 5
    Output: 2
    Explanation: Starting with nums = [1,2,3,4]:
    - Remove numbers 1 and 4, then nums = [2,3]
    - Remove numbers 2 and 3, then nums = []
    There are no more pairs that sum up to 5, hence a total of 2 operations.

Example 2:
    Input: nums = [3,1,3,4,3], k = 6
    Output: 1
    Explanation: Starting with nums = [3,1,3,4,3]:
    - Remove the first two 3's, then nums = [1,4,3]
    There are no more pairs that sum up to 6, hence a total of 1 operation.
"""


class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        """
        解題方式: two pointer

        Complexity
            -- time: O(n log n)
            -- space: O(1)
        """
        nums = sorted(nums)
        count = 0
        
        i = 0
        j = len(nums) - 1

        while i < j:
            if nums[i] + nums[j] == k:
                count += 1
                i += 1
                j -= 1

            elif nums[i] + nums[j] < k:
                i += 1
            else:
                j -= 1


        return count


solution = Solution()

nums = [1,2,3,4]
k = 5
result = solution.maxOperations(nums, k)
print(result)

nums = [3,1,3,4,3]
k = 6
result = solution.maxOperations(nums, k)
print(result)

nums = [4,4,1,3,1,3,2,2,5,5,1,5,2,1,2,3,5,4]
k = 2
result = solution.maxOperations(nums, k)
print(result)