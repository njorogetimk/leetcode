from typing import List

"""
Sort the elements in decreasing order
Return the kth element of the array
"""

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        def merge(a, b):
            i, j, a_b = 0, 0, []

            while i < len(a) and j < len(b):
                if a[i] >= b[j]:
                    a_b.append(a[i])
                    i += 1
                else:
                    a_b.append(b[j])
                    j += 1
            
            
            return a_b + a[i:] + b[j:]
        
        def merger(arr):
            if len(arr) <= 1:
                return arr
            
            mid = len(arr)//2

            left_div, right_div = merger(arr[:mid]), merger(arr[mid:])

            merged = merge(left_div, right_div)

            return merged
        
        sorted_nums = merger(nums)
        l = k-1
        return sorted_nums[l]
            
