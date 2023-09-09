"""
title: Plus One

You are given a large integer represented as an integer array digits,
where each digits[i] is the ith digit of the integer.
The digits are ordered from most significant to least significant in left-to-right order.
The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

"""


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        plus = 1
        nums = ""
        result = []

        for n in digits:
            nums += str(n)

        nums = int(nums)
        
        nums += plus

        for _ in range(len(str(nums))):
            temp = nums % 10
            nums //= 10

            result.insert(0, temp)
        
        return result


solution = Solution()

digits = [[1, 2, 3], [1, 2, 3, 4]]
results = []

for i in range(len(digits)):
    res = solution.plusOne(digits[i])
    results.append(res)

for result in results:
    print(result)