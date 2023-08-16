"""
title:  Maximum Number of Vowels in a Substring of Given Length

Given a string s and an integer k,
return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.


Example 1:
    Input: s = "abciiidef", k = 3
    Output: 3
    Explanation: The substring "iii" contains 3 vowel letters.

Example 2:
    Input: s = "aeiou", k = 2
    Output: 2
    Explanation: Any substring of length 2 contains 2 vowels.

Example 3:
    Input: s = "leetcode", k = 3
    Output: 2
    Explanation: "lee", "eet" and "ode" contain 2 vowels.
"""



class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if not s or k == 0:
            return 0
        
        """
        解題方式: sliding window
        """
        n = len(s)

        start = 0
        count = 0
        max_len = 0

        vowels = ['a', 'e', 'i', 'o', 'u']

        for i in range(n):
            if i - start + 1 > k:
                max_len = max(count, max_len)

                if s[start].lower() in vowels:   # 嚴謹一點的話，轉小寫
                    count -= 1

                start += 1

            if s[i].lower() in vowels:
                count += 1

        max_len = max(count, max_len)

        return max_len


        """
        解題方式: substring 檢索

        Complexity
            -- time: O(n * k)
        """
        # start = 0
        # end = k
        # n = len(s)
        # vowels = ['a', 'e', 'i', 'o', 'u']

        # count = 0
        # max_len = 0

        # while end <= n:
        #     sub_str = s[start: end]

        #     for i in range(len(sub_str)):
        #         if sub_str[i] in vowels:
        #             count += 1

        #     max_len = max(count, max_len)

        #     start += 1
        #     end += 1
        #     count = 0

        # return max_len


solution = Solution()

s = "abciiidef"
k = 3
result = solution.maxVowels(s, k)
print(result)

s = "aeiou"
k = 2
result = solution.maxVowels(s, k)
print(result)

s = "leetcode"
k = 3
result = solution.maxVowels(s, k)
print(result)

s = "weallloveyou"
k = 7
result = solution.maxVowels(s, k)
print(result)