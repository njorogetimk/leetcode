from typing import List

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        
        one, two = nums[:], nums[:] # make two copies of the array
        
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                one[i] = nums[i + 1]
                two[i + 1] = nums[i]
                break
        return one == sorted(one) or two == sorted(two)