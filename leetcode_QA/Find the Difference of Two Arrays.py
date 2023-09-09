"""
title: Find the Difference of Two Arrays

Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

-- answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
-- answer[1] is a list of all distinct integers in nums2 which are not present in nums1.

Note that the integers in the lists may be returned in any order.


Example 1:
    Input: nums1 = [1,2,3], nums2 = [2,4,6]
    Output: [[1,3],[4,6]]
    Explanation:
    For nums1, nums1[1] = 2 is present at index 0 of nums2,
    whereas nums1[0] = 1 and nums1[2] = 3 are not present in nums2. Therefore, answer[0] = [1,3].
    
    For nums2, nums2[0] = 2 is present at index 1 of nums1,
    whereas nums2[1] = 4 and nums2[2] = 6 are not present in nums2. Therefore, answer[1] = [4,6].

Example 2:
    Input: nums1 = [1,2,3,3], nums2 = [1,1,2,2]
    Output: [[3],[]]
    Explanation:
    For nums1, nums1[2] and nums1[3] are not present in nums2. Since nums1[2] == nums1[3],
    their value is only included once and answer[0] = [3].
    
    Every integer in nums2 is present in nums1. Therefore, answer[1] = [].
"""


class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        if not nums1:
            return [[], nums2]
        if not nums2:
            return [nums1, []]
        

        """
        解題方式: build-in type --> set 集合運算
        """
        # answer = []

        # set_1 = set(nums1)
        # set_2 = set(nums2)

        # 差集運算
        # answer.append(list(set_1 - set_2))
        # answer.append(list(set_2 - set_1))


        """
        解題方式: 遍歷整個陣列
        """
        answer = [[], []]

        n = len(nums1)
        m = len(nums2)

        for i in range(n):
            if nums1[i] not in nums2 and nums1[i] not in answer[0]:
                answer[0].append(nums1[i])

        for j in range(m):
            if nums2[j] not in nums1 and nums2[j] not in answer[1]:
                answer[1].append(nums2[j])

        return answer


solution = Solution()

nums1 = [1,2,3]
nums2 = [2,4,6]
result = solution.findDifference(nums1, nums2)
print(result)

nums1 = [1,2,3,3]
nums2 = [1,1,2,2]
result = solution.findDifference(nums1, nums2)
print(result)