"""
title: Asteroid Collision

We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size,
and the sign represents its direction (positive meaning right, negative meaning left).
Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions.
If two asteroids meet, the smaller one will explode.
If both are the same size, both will explode.
Two asteroids moving in the same direction will never meet.


Example 1:

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
Example 2:

Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.
Example 3:

Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
"""


class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """

        """
        解題方式: Stack 操作

        思路: 從題目中提到的小行星相撞，陣列 asteroids 中發生的情況

                有 3 種
                        -- 1. 兩兩相撞，比較 "小的" 元素，從 stack 彈出去
                        -- 2. 一樣又相撞，不過相撞的大小 "相等"，一起消滅掉
                                (一個從 stack 踢出去，另一個就跳過)
                        
                        -- 3. 沒有相撞，一起手牽手進入 stack

            會不會發生相撞，則是從陣列 asteroids 的每一個數值，
                是正數 or 負數，來決定移動方向

                -- 1. 正整數: 往右  --->
                -- 2. 負整數: 往左  <---
        """
        
        result = []   # 處理相撞情況的 stack
        n = len(asteroids)

        for i in range(n):
            while len(result) > 0 and result[-1] > 0 and asteroids[i] < 0:
                # 如果 負整數 還是比較大，
                # 就繼續彈出到 小於負整數 為止
                if result[-1] < abs(asteroids[i]):
                    result.pop()
                    continue
                
                # 相等大小則一起清掉，中斷 while loop 再抓下一個
                elif result[-1] == abs(asteroids[i]):
                    result.pop()

                break

            else:
                result.append(asteroids[i])

            # print(result)

        return result


solution = Solution()

asteroids = [5,10,-5]
result = solution.asteroidCollision(asteroids)
print(result)

asteroids = [8,-8]
result = solution.asteroidCollision(asteroids)
print(result)

asteroids = [10,2,-5]
result = solution.asteroidCollision(asteroids)
print(result)

asteroids = [-2,-1,1,2]
result = solution.asteroidCollision(asteroids)
print(result)