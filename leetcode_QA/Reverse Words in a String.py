"""
title: Reverse Words in a String

Given an input string , reverse the order of the words.s

A word is defined as a sequence of non-space characters.
The words in will be separated by at least one space.s

Return a string of the words in reverse order concatenated by a single space.

Note that may contain leading or trailing spaces or multiple spaces between two words.
The returned string should only have a single space separating the words.
Do not include any extra spaces.s


Example 1:
    Input: s = "the sky is blue"
    Output: "blue is sky the"

Example 2:
    Input: s = "  hello world  "
    Output: "world hello"
    Explanation: Your reversed string should not contain leading or trailing spaces.

Example 3:
    Input: s = "a good   example"
    Output: "example good a"
    Explanation: You need to reduce multiple spaces between two words to
                    a single space in the reversed string.
"""


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        
        temp = ""
        result = ""
        reverse_str = []

        for i in range(len(s)):
            if s[i] != " ":
                temp += s[i]
            else:
                if temp:
                    reverse_str.append(temp)
                    temp = ""
        if temp:
            reverse_str.append(temp)

        reverse_str.reverse()

        for i in range(len(reverse_str)):
            if i < len(reverse_str) - 1:
                result += reverse_str[i] + " "

            else:
                result += reverse_str[i]

        return result


solution = Solution()

s = "the sky is blue"
result = solution.reverseWords(s)
print(result)

s = "  hello world  "
result = solution.reverseWords(s)
print(result)

s = "a good   example"
result = solution.reverseWords(s)
print(result)