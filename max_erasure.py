from typing import List

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        found = set()

        curr, max_s, counter = 0, 0, 0

        for num in nums:
            print(num, found, curr)
            while num in found:
                curr -= nums[counter]
                found.remove(nums[counter])
                counter += 1
            
            curr += num
            found.add(num)
            max_s = max(max_s, curr)
        
        return max_s