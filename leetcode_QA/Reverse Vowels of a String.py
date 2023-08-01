"""
title: Reverse Vowels of a String

Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u',
and they can appear in both lower and upper cases, more than once.

Example 1:
    Input: s = "hello"
    Output: "holle"

Example 2:
    Input: s = "leetcode"
    Output: "leotcede"
"""


class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = []
        compare = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

        for i in range(len(s)):
            if s[i] in compare:
                vowels.append(s[i])

        vowels.reverse()

        k = 0
        result = ""

        for i in range(len(s)):
            if s[i] in compare:
                result += vowels[k]
                k += 1
            else:
                result += s[i]

        return result


solution = Solution()

s = "hello"
result = solution.reverseVowels(s)
print(result)

s = "leetcode"
result = solution.reverseVowels(s)
print(result)