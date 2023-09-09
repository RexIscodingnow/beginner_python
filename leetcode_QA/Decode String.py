"""
title: Decode String

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string],
where the encoded_string inside the square brackets is being repeated exactly k times.
Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid;
there are no extra white spaces,square brackets are well-formed, etc.
Furthermore, you may assume that the original data does not contain any digits and
that digits are only for those repeat numbers, k.

For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 10 ^ 5.


Example 1:
    Input: s = "3[a]2[bc]"
    Output: "aaabcbc"

Example 2:
    Input: s = "3[a2[c]]"
    Output: "accaccacc"

Example 3:
    Input: s = "2[abc]3[cd]ef"
    Output: "abcabccdcdcdef"
"""


class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        result = ""

        cnt = 0     # e.g: k[..x[..]] => 假設 [] 號內層還有嵌套 1 個(以上)
        num = ""
        stack = []

        for i in range(n):
            if s[i].isdigit():
                num += s[i]
            
            elif s[i] != "]":
                if num:
                    stack.append(num)

                if s[i] == "[":
                    cnt += 1

                num = ""
                stack.append(s[i])

            else:
                temp = ""

                # 提取在 [] 內的 decode string
                while len(stack) > 0:
                    c = stack.pop()
                    
                    if c != "[":
                        temp = c + temp
                    else:
                        break

                multi = int(stack.pop())
                for _ in range(multi):
                    result += temp

                # 不只一層 [] 號，則是先壓回 stack
                if cnt >= 1:
                    stack.append(result)
                    result = ""

                cnt -= 1

        temp = ""
        while len(stack) > 0:
            temp = stack.pop() + temp
        
        result += temp

        return result


solution = Solution()

s = "3[a]2[bc]"
result = solution.decodeString(s)
print(result)

s = "3[a2[c]]"
result = solution.decodeString(s)
print(result)

s = "2[abc]3[cd]ef"
# s = "abc3[cd]xyz"
# s = "abcd3[ef2[xy2[z]]g]"
# s = "10[leetcode]"
result = solution.decodeString(s)
print(result)