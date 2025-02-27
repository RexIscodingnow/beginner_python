"""
title: Successful Pairs of Spells and Potions

You are given two positive integer arrays spells and potions, of length n and m respectively,
where spells[i] represents the strength of the i-th spell and potions[j] represents
the strength of the j-th potion.

You are also given an integer success
A spell and potion pair is considered successful
if the product of their strengths is at least success.

Return an integer array pairs of length n where pairs[i] is the number of potions
that will form a successful pair with the i-th spell.


Example 1:
    Input: spells = [5,1,3], potions = [1,2,3,4,5], success = 7
    Output: [4,0,3]
    Explanation:
    - 0-th spell: 5 * [1,2,3,4,5] = [5,10,15,20,25]. 4 pairs are successful.
                                        ^  ^  ^  ^

    - 1-st spell: 1 * [1,2,3,4,5] = [1,2,3,4,5]. 0 pairs are successful.

    - 2-nd spell: 3 * [1,2,3,4,5] = [3,6,9,12,15]. 3 pairs are successful.
                                         ^  ^  ^
    
    Thus, [4,0,3] is returned.

Example 2:
    Input: spells = [3,1,2], potions = [8,5,8], success = 16
    Output: [2,0,2]
    Explanation:
    - 0-th spell: 3 * [8,5,8] = [24,15,24]. 2 pairs are successful.
                                  ^     ^

    - 1-st spell: 1 * [8,5,8] = [8,5,8]. 0 pairs are successful.

    - 2-nd spell: 2 * [8,5,8] = [16,10,16]. 2 pairs are successful.
                                  ^     ^
    
    Thus, [2,0,2] is returned.
"""


class Solution(object):
    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """

        """
        解題方式: binary search

        Complexity
            -- time: O(n * (log m))
            -- space: O(m)

        n: the length of array "spells"
        m: the length of array "potions"
        """
        
        n = len(spells)
        m = len(potions)
        result = []

        potions = sorted(potions)
        
        for i in range(n):
            left = 0
            right = m - 1
            spell = spells[i]

            # 求得以 success 為基準的分界線
            while left <= right:
                mid = (left + right) // 2
                product = spell * potions[mid]

                if product >= success:
                    right = mid - 1
                else:
                    left = mid + 1

            result.append(m - 1 - right)

        return result


solution = Solution()

spells = [5,1,3]
potions = [1,2,3,4,5]
success = 7
result = solution.successfulPairs(spells, potions, success)
print(result)

spells = [3,1,2]
potions = [8,5,8]
success = 16
result = solution.successfulPairs(spells, potions, success)
print(result)