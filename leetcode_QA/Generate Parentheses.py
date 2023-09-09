"""
title: Generate Parentheses

Given n pairs of parentheses,
write a function to generate all combinations of well-formed parentheses.


Example 1:
    Input: n = 3
    Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
    Input: n = 1
    Output: ["()"]


其他大神的 solution 以及遞迴樹輔助說明
-- https://leetcode.com/problems/generate-parentheses/solutions/2542620/python-java-w-explanation-faster-than-96-w-proof-easy-to-understand/


*註: 下方遞迴樹的來源詳見上方網址

node: ( left, right, 當下排列狀態 )   p.s: 累加使用次數

n = 2
                    (0, 0, '')
                        |	
                    (1, 0, '(')  
                    /           \
            (2, 0, '((')      (1, 1, '()')
                /                 \
        (2, 1, '(()')           (2, 1, '()(')
            /                       \
    (2, 2, '(())')                (2, 2, '()()')
                |	                             |
    res.append('(())')             res.append('()()')
"""


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        """
        解題方式: Dynamic Programming 動態規劃法
        """

        if n < 1:
            return []
        
        parenthesis = []
        self.generator(n, n, "", parenthesis)
        return parenthesis


    def generator(self, left, right, item: str, result: list):
        """
        輔助函式
                -- 遞減的方式，以 "剩餘數量" 作為遞迴中止條件

        : param left: 左括號數量: ( 
        : param right: 右括號數量: )
        : param item: 當前的排列組合 (每一步的 Recursion 所排列的狀態)
        : param result: 排列結果
        """
        # 左、右兩邊的括號用完後，
        # 則儲存結果，並返回 (Non-rtype)
        if left == 0 and right == 0:
            # print("append:", item)

            result.append(item)
            return

        # 左括號的數輛尚未用完，則累加 ( 號
        if left > 0:
            # print("left:", item)
            self.generator(left - 1, right, item + "(", result)

        # 右括號剩餘數量 > 左括號剩餘數量，則放 ) 號
        if left < right:
            # print("right:", item)
            self.generator(left, right - 1, item + ")", result)


solution = Solution()

n = 1
print("n = 1")
print("----------------------")
result = solution.generateParenthesis(n)
print(result)

n = 2
print()
print("n = 2")
print("----------------------")
result = solution.generateParenthesis(n)
print(result)

n = 3
print()
print("n = 3")
print("----------------------")
result = solution.generateParenthesis(n)
print(result)