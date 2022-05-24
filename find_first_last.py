from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        hi, lo, mid = len(nums), 0, len(nums)//2
        
        def find_left(left_part, mid, target):
            left = mid - left_part.count(target)
            return left
        
        def find_right(right_part, mid, target):
            right = mid + right_part.count(target)
            return right

        count = 0
        while count < len(nums):
            # Check if the mid == target
            if nums[mid] == target:
                first = mid if nums[mid-1] != target else find_left(nums[lo:mid], mid, target)

                if mid == len(nums) - 1:
                    # target last value in list
                    last = mid
                    return [first, last]

                last = mid if nums[mid+1] != target else find_right(nums[mid+1:hi], mid, target)

                return [first, last]
            elif nums[mid] < target:
                # target on the right
                lo = mid
                mid = lo + len(nums[lo:hi])//2
            else:
                # target on the left
                hi = mid
                mid = len(nums[lo:hi])//2
            
            count += 1    
            
        return [-1, -1]