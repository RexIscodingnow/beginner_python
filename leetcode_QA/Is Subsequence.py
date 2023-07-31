"""
title: Is Subsequence

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from
the original string by deleting some (can be none) of the characters
without disturbing the relative positions of the remaining characters.

(i.e., "ace" is a subsequence of "abcde" while "aec" is not).


Example 1:
    Input: s = "abc", t = "ahbgdc"
    Output: true

Example 2:
    Input: s = "axc", t = "ahbgdc"
    Output: false
"""


class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        """
        解題方式: Two Pointer
        """
        if not s:
            return True

        res = True
        j = 0

        for i in range(len(t)):
            if j >= len(s):
                break

            if s[j] == t[i]:
                j += 1

        if j < len(s):
            res = False

        return res


solution = Solution()

s = "abc"
t = "ahbgdc"
result = solution.isSubsequence(s, t)
print(result)

s = "axc"
t = "ahbgdc"
result = solution.isSubsequence(s, t)
print(result)

s = "acb"
t = "ahbgdc"
result = solution.isSubsequence(s, t)
print(result)