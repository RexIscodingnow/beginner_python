"""
title: Pascal's Triangle II

Given an integer rowIndex, return the rowIndex -th (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

n = 5
        1
      1   1
    1   2   1
  1   3   3   1
1   4   6   4   1


Example 1:
    Input: rowIndex = 3
    Output: [1,3,3,1]

Example 2:
    Input: rowIndex = 0
    Output: [1]

Example 3:
    Input: rowIndex = 1
    Output: [1,1]
"""


class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        result = []
        
        # 巴斯卡三角形，它的最外圍都是 1
        for i in range(rowIndex + 1):
            layer = [0] * (i+1)
            if len(layer) < 2:
                layer[0] = 1
            else:
                layer[0] = layer[len(layer) - 1] = 1

            result.append(layer)


        for i in range(2, rowIndex + 1):
            top_layer = result[i-1]    # 前一層

            for j in range(1, len(result[i]) - 1):
                result[i][j] = top_layer[j-1] + top_layer[j]

        return result[len(result) - 1]


solution = Solution()

rowIndex = 3
result = solution.getRow(rowIndex)
print(result)

rowIndex = 0
result = solution.getRow(rowIndex)
print(result)

rowIndex = 1
result = solution.getRow(rowIndex)
print(result)