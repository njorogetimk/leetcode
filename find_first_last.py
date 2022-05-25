from typing import List

def binary_search(lo, hi, condition):
    """Generic binary search"""

    while lo <= hi:
        mid = (hi + lo)//2
        result = condition(mid)

        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid -1
        else:
            lo = mid + 1

    return -1

def find_first(nums: List[int], target: int) -> int:
    """Find first occurrence of the target"""
    lo, hi = 0, len(nums) - 1
    def condition(mid) -> str:
        mid_num = nums[mid]
        if mid_num == target:

            if mid == 0:
                return 'found'
            if nums[mid - 1] == target:
                return 'left'
            
            return 'found'
        elif mid_num > target:
            # Search left
            return 'left'
        else:
            # Search right
            return 'right'

    return binary_search(lo, hi, condition)

def find_last(nums: List[int], target: int) -> int:
    """Find last occurrence of the target"""
    lo, hi = 0, len(nums) - 1
    def condition(mid) -> str:
        mid_num = nums[mid]

        if mid_num == target:

            if mid == hi:
                return 'found'
            elif nums[mid + 1] == target:
                return 'right'
            return 'found'
        elif mid_num > target:
            # Search left
            return 'left'
        else:
            # Search right
            return 'right'
    return binary_search(lo, hi, condition)


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        return [find_first(nums, target), find_last(nums, target)]