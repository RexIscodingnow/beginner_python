"""
title: Greatest Common Divisor of Strings

For two strings s and t, we say "t divides s" if and

only if s = t + ... + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2,
return the largest string x such that x divides both str1 and str2.

Example 1:
    Input: str1 = "ABCABC", str2 = "ABC"
    Output: "ABC"

Example 2:
    Input: str1 = "ABABAB", str2 = "ABAB"
    Output: "AB"

Example 3:
    Input: str1 = "LEET", str2 = "CODE"
    Output: ""
"""


import math


class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        n = len(str1)
        m = len(str2)

        if (str1 + str2) == (str2 + str1):
            # 找最大公因數 (by string)
            gcd_idx = math.gcd(n, m)

            return str1[:gcd_idx]

        else:
            return ""


solution = Solution()

str1 = "ABCABC"
str2 = "ABC"
result = solution.gcdOfStrings(str1, str2)
print(result)

str1 = "ABABAB"
str2 = "ABAB"
result = solution.gcdOfStrings(str1, str2)
print(result)

str1 = "LEET"
str2 = "CODE"
result = solution.gcdOfStrings(str1, str2)
print(result)