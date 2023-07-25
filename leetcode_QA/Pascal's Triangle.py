"""
title: Pascal's Triangle

Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

n = 5
        1
      1   1
    1   2   1
  1   3   3   1
1   4   6   4   1

Example 1:
    Input: numRows = 5
    Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:
    Input: numRows = 1
    Output: [[1]]
"""


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        
        # 巴斯卡三角形，它的最外圍都是 1
        for i in range(numRows):
            layer = [0] * (i+1)
            if len(layer) < 2:
                layer[0] = 1
            else:
                layer[0] = layer[len(layer) - 1] = 1

            result.append(layer)

        # print(result)

        for i in range(2, numRows):
            top_layer = result[i-1]    # 前一層

            for j in range(1, len(result[i]) - 1):
                result[i][j] = top_layer[j-1] + top_layer[j]

        return result


solution = Solution()
numRows = 5
result = solution.generate(numRows)
print(result)

numRows = 1
result = solution.generate(numRows)
print(result)

numRows = 3
result = solution.generate(numRows)
print(result)