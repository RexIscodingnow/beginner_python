"""
title: Find the Index of the First Occurrence in a String

Given two strings needle and haystack,
return the index of the first occurrence of needle in haystack,
or -1 if needle is not part of haystack.

Example 1:
    Input: haystack = "sadbutsad", needle = "sad"
    Output: 0
    Explanation: "sad" occurs at index 0 and 6.
    The first occurrence is at index 0, so we return 0.
Example 2:
    Input: haystack = "leetcode", needle = "leeto"
    Output: -1
    Explanation: "leeto" did not occur in "leetcode", so we return -1.
"""


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # 以 needle 的範圍移動搜尋，因此扣掉尾段長: len(needle)
        for i in range(len(haystack) - len(needle) + 1):

            # haystack 的切片，切片長度為 needle 的字串長度
            if haystack[i: i + len(needle)] in needle:
                return i

        return -1


solution = Solution()


haystack = ["sadbutsad", "leetcode", "thecode"]
needle = ["sad", "leeto", "code"]
results = []

for i in range(len(needle)):
    res = solution.strStr(haystack[i], needle[i])
    results.append(res)

for result in results:
    print(result)