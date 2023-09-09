"""
title: Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:
    Input: s = "()"
    Output: true

Example 2:
    Input: s = "()[]{}"
    Output: true

Example 3:
    Input: s = "(]"
    Output: false
"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) < 2 or len(s) % 2 != 0:
            return False

        stack = []
        legal = True

        parentheses = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for char in s:
            if char in parentheses.values():
                stack.append(char)

            elif char in parentheses.keys():
                if stack == []:
                    legal = False
                else:
                    if parentheses[char] != stack.pop():
                        legal = False

        if stack != []:
            legal = False

        return legal


solution = Solution()

s = "()"
result = solution.isValid(s)
print(result)

s = "()[]{}"
result = solution.isValid(s)
print(result)

s = "(]"
result = solution.isValid(s)
print(result)