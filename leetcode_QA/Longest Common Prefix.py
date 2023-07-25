"""
title: Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".


Example 1:
    Input: strs = ["flower","flow","flight"]
    Output: "fl"

Example 2:
    Input: strs = ["dog","racecar","car"]
    Output: ""
    Explanation: There is no common prefix among the input strings.
"""


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        result = ""
        temp = ""
        compare_temp = ""   # 比對結果 暫存區
        result = strs[0]    # 取第一個值

        for i in range(1, len(strs)):
            temp = strs[i]
            min_len = min(result, temp)

            # 相鄰的兩個字串，逐字元比對
            for j in range(len(min_len)):
                if temp[j] == result[j]:
                    compare_temp += temp[j]

                elif temp[0] != result[0]:
                    return ""

                else:
                    break

            result = compare_temp
            compare_temp = ""

        return result
    

solution = Solution()

strs = ["flower","flow","flight"]
result = solution.longestCommonPrefix(strs)
print(result)

strs = ["dog","racecar","car"]
result = solution.longestCommonPrefix(strs)
print(result)