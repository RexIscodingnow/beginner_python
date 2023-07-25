"""
附註: 尚未解題完成

title: String to Integer (atoi)

Implement the myAtoi(string s) function,
which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:

Read in and ignore any leading whitespace.
Check if the next character (if not already at the end of the string) is '-' or '+'.
Read this character in if it is either.
This determines if the final result is negative or positive respectively.
Assume the result is positive if neither is present.

Read in next the characters until the next non-digit character or the end of the input is reached.
The rest of the string is ignored.
Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32).
If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).

If the integer is out of the 32-bit signed integer range [-2 ^ 31, 2 ^ 31 - 1],
then clamp the integer so that it remains in the range.

Specifically, integers less than -2 ^ 31 should be clamped to -2 ^ 31,
and integers greater than 2 ^ 31 - 1 should be clamped to 2 ^ 31 - 1.

Return the integer as the final result.

Note:
Only the space character ' ' is considered a whitespace character.

Do not ignore any characters other than the leading whitespace
or the rest of the string after the digits.


Example 1:
    Input: s = "42"
    Output: 42
    Explanation: The underlined characters are what is read in, the caret is the current reader position.
    Step 1: "42" (no characters read because there is no leading whitespace)
            ^
    Step 2: "42" (no characters read because there is neither a '-' nor '+')
            ^
    Step 3: "42" ("42" is read in)
            ^
    The parsed integer is 42.
    Since 42 is in the range [-2 ^ 31, 2 ^ 31 - 1], the final result is 42.

Example 2:
    Input: s = "   -42"
    Output: -42
    Explanation:
    Step 1: "   -42" (leading whitespace is read and ignored)
                ^
    Step 2: "   -42" ('-' is read, so the result should be negative)
                ^
    Step 3: "   -42" ("42" is read in)
                ^
    The parsed integer is -42.
    Since -42 is in the range [-2 ^ 31, 2 ^ 31 - 1], the final result is -42.

Example 3:
    Input: s = "4193 with words"
    Output: 4193
    Explanation:
    Step 1: "4193 with words" (no characters read because there is no leading whitespace)
            ^
    Step 2: "4193 with words" (no characters read because there is neither a '-' nor '+')
            ^
    Step 3: "4193 with words" ("4193" is read in; reading stops because the next character is a non-digit)
                ^
    The parsed integer is 4193.
    Since 4193 is in the range [-2 ^ 31, 2 ^ 31 - 1], the final result is 4193.
"""


class Solution(object):
    def myAtoi(self, s: str):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0


        number = ""
        positive = 0
        negative = 0

        i = 0

        while i < len(s) and s[i] == " ":   # 跳過前頭的空白字串 (就是忽略掉)
            i += 1

        if s[i].isdigit() == False and s[i] not in ['+', '-']:
            return 0

        while i < len(s):
            if s[i] == "-":
                negative += 1
            if s[i] == "+":
                positive += 1
            if s[i].isdigit():
                number += s[i]

            if s[i] == ".":
                break

            i += 1


        if (positive > 0 and negative > 0) or not number.isdigit():
            return 0

        if negative > 0:
            number = '-' + number


        number = int(number)

        if number >= 2 ** 31:
            return 2 ** 31
        elif number <= -2 ** 31:
            return -2 ** 31
        else:
            return number


solution = Solution()

s = "42"
result = solution.myAtoi(s)
print(result)

s = "     -42"
result = solution.myAtoi(s)
print(result)

s = "4193 with words"
result = solution.myAtoi(s)
print(result)

# 下方為 edge case，其結果要求為 0
s = "words and 987"
result = solution.myAtoi(s)
print(result)

s = "+-654.566"
result = solution.myAtoi(s)
print(result)