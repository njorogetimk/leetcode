from typing import List

def binary_search(hi: int, lo: int, condition):
    while lo <= hi:
        mid = (hi + lo)//2
        result = condition(mid)

        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid -1
        else:
            lo = mid + 1
    
    return 0

class Solution:
    def count_rotations(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums)-1

        def condition(mid):
            mid_num = nums[mid]

            if mid > 0 and mid_num <= nums[hi]:
                if mid_num == nums[mid-1]:
                    return 'left'
                return 'found'
            elif mid_num < nums[hi]:
                return 'left'
            else:
                return 'right'
        
        return binary_search(hi, lo, condition)