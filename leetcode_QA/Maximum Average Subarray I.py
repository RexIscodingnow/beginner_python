"""
title: Maximum Average Subarray I

You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k
that has the maximum average value and return this value.

Any answer with a calculation error less than 10 ^ -5 will be accepted.

Example 1:
    Input: nums = [1,12,-5,-6,50,3], k = 4
    Output: 12.75000
    Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

Example 2:
    Input: nums = [5], k = 1
    Output: 5.00000
"""


class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """

        """
        解題方式: Sliding Window (滑動窗口)

        思路: 從起始點開始，將窗口從尾部擴大，擴大的同時加總數值， -- (1)
                直到窗口大小 與 k 相等，則停止窗口擴大， ----------- (2)
            
                計算的平均值 與 先前的平均值比，
                -- 當前的較大，則寫入  ---------------------------- (3)
                -- 反之，則移動窗口  ------------------------------ (4)
        """
        n = len(nums)
 
        start = 0   # left bound
        end = 0     # right bound
        total = 0

        max_avg = float("-inf")

        while end < n:
            if end - start < k:
                total += nums[end]

            if end - start + 1 == k:
                max_avg = max((total / k), max_avg)

                total -= nums[start]    # remove the element of left bound
                start += 1

            end += 1

        return max_avg


solution = Solution()

nums = [1, 12, -5, -6, 50, 3]
k = 4
result = solution.findMaxAverage(nums, k)
print(result)

nums = [5]
k = 1
result = solution.findMaxAverage(nums, k)
print(result)

nums = [8860,-853,6534,4477,-4589,8646,-6155,-5577,-1656,-5779,-2619,-8604,-1358,-8009,4983,7063,3104,-1560,4080,2763,5616,-2375,2848,1394,-7173,-5225,-8244,-809,8025,-4072,-4391,-9579,1407,6700,2421,-6685,5481,-1732,-8892,-6645,3077,3287,-4149,8701,-4393,-9070,-1777,2237,-3253,-506,-4931,-7366,-8132,5406,-6300,-275,-1908,67,3569,1433,-7262,-437,8303,4498,-379,3054,-6285,4203,6908,4433,3077,2288,9733,-8067,3007,9725,9669,1362,-2561,-4225,5442,-9006,-429,160,-9234,-4444,3586,-5711,-9506,-79,-4418,-4348,-5891]
k = 93
result = solution.findMaxAverage(nums, k)
print(result)