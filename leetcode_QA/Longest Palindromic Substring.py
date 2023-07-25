"""
title: Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s.

Explanation palindromic substring:
    -- A string is palindromic if it reads the same forward and backward.
    -- A substring is a contiguous non-empty sequence of characters within a string.

Example 1:
    Input: s = "babad"
    Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:
    Input: s = "cbbd"
    Output: "bb"
"""


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""

        for i in range(len(s)):
            odd_str = self.expand(s, i, i)      # 奇數長度的回文字串
            even_str = self.expand(s, i, i+1)   # 偶數長度...(同上)

            res = max(res, odd_str, even_str, key=len)   # 以字串長度為基準

        return res


    def expand(self, s, i, j):
        """
        以向外擴展，來檢索回文字串

        : rtype: string slicing
        """
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1

        return s[i+1: j]


solution = Solution()

s = "babad"
result = solution.longestPalindrome(s)
print(result)

s = "abbabbd"
result = solution.longestPalindrome(s)
print(result)

s = "afdtft"
result = solution.longestPalindrome(s)
print(result)