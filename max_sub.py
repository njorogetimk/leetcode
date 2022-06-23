from typing import List
import math

"""
Purpose: Given an array of numbers, return the highest sum from a contigous subarray
Input: Array on nums e.g [4,-2,3,-5,7]
Output: highest sum of a contigous subarray i.e 7

Get the sum of each substring and return the highest sum
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        max_sum = nums[0]
        for i in range (len(nums)):
            end = i+1
            
            while end <= len(nums):
                max_sum = max(max_sum, sum(nums[i:end]))
                end += 1
        
        return max_sum
        """

        """
        def rec_s(nums, start=0, end=1, max_sum = None):

            if max_sum == None:
                max_sum = -math.inf
            
            if start > len(nums)-1:
                return max_sum
            
            if end <= len(nums):
                # print(nums[start:end], '**', sum(nums[start:end]) ,'**', max_sum)
                max_sum = max(max_sum, sum(nums[start:end]))
                end +=1
                q =rec_s(nums, start, end, max_sum)
            
            else:
                start += 1
                end = start + 1
                q = rec_s(nums, start, end, max_sum)
            
            return q

        return rec_s(nums)
        """

        """
        # @cache
        def solve(i, must_pick):
            if i >= len(nums): return 0 if must_pick else -inf
            return max(nums[i] + solve(i+1, True), 0 if must_pick else solve(i+1, False))
        return solve(0, False)
        """

        dp = [[0]*len(nums) for i in range(2)]
        dp[0][0], dp[1][0] = nums[0], nums[0]
        for i in range(1, len(nums)):
            dp[1][i] = max(nums[i], nums[i] + dp[1][i-1])
            dp[0][i] = max(dp[0][i-1], dp[1][i])
            print(dp)
        return dp[0][-1]