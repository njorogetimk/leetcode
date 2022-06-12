from typing import List
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        sum_slider = sum(nums) - x

        curr, max_ops = 0, 0
        start = 0
        found = False

        for end in range(len(nums)):
            curr += nums[end]

            # Implement the slider for min 
            while start <= end and curr > sum_slider:
                curr -= nums[start]
                start += 1
            
            if curr == sum_slider:
                found = True
                max_ops = max(max_ops, end - start+1)
        
        min_ops = len(nums) - max_ops if found else -1

        return min_ops