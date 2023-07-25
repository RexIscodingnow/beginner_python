"""
title: Longest Substring Without Repeating Characters

Given a string s, find the length of the longest 
substring without repeating characters.

Explanation substring:
    -- A substring is a contiguous non-empty sequence of characters within a string.

Example 1:
    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.
Example 2:
    Input: s = "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.
Example 3:
    Input: s = "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3.
    Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        """
        滑動窗口 sliding window 解法
        
        使用資料結構: hashMap
        """

        # letter: index
        indexes = {}    # 使用 hash map 去儲存遍歷過的每一個字元
        start = 0       # 滑動窗口的起始範圍
        max_length = 0  # 最大值

        for (i, letter) in enumerate(s):
            # 有存入過
            if letter in indexes and start <= indexes[letter]:
                """
                往後面移動 (更新到不重複的字元)
                
                ex: pwwkew  => test case
                    012345  => index
                
                index: 0 ~ 1
                : before indexes: None   # 前一個狀態
                : start = 0
                : maxLength = 2 => ((1 - 0) + 1)  vs  0
                : final indexes: {p: 0, w: 1}    # 修改後

                index: 1 ~ 2
                : before indexes: {p: 0, w: 1}
                : start = 2 ==> (w: 1) + 1
                : maxLength = 1 = ((2 - 2) + 1)   vs  1
                : final indexes: {p: 0, w: 2}    # 字母 w 的位置，更新至 2

                以此類推......
                """
                start = indexes[letter] + 1

            # 當前遍歷的位置 - 起始位置 + 1  v.s.  當前計算的最大長度
            max_length = max((i - start) + 1, max_length)
            indexes[letter] = i

            print(indexes)
        
        return max_length


# class Solution(object):
#     def lengthOfLongestSubstring(self, s):
#         """
#         :type s: str
#         :rtype: int

#         Powered By ChatGPT
#         """
#         window = {}  # Hash map to store the characters in the current window
#         max_length = 0  # Variable to store the maximum length found so far
#         start = 0  # Start of the sliding window

#         print("window in for loop:")
#         for i, c in enumerate(s):
#             # If the current character is already in the window, update the start of the window
#             if c in window:
#                 start = max(start, window[c] + 1)

#             # Update the maximum length and add the current character to the window
#             max_length = max(max_length, i - start + 1)
#             window[c] = i
#             print(window)
#             print("max_length:", max_length)

#         print("final window:", window)

#         return max_length


# test case
solution = Solution()
s = "bbbbbbbbb"
result = solution.lengthOfLongestSubstring(s)
print(result)
s = "abcabcaa"
result = solution.lengthOfLongestSubstring(s)
print(result)
s = "pwwkew"
result = solution.lengthOfLongestSubstring(s)
print(result)