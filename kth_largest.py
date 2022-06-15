from typing import List

"""
Sort the elements in decreasing order
Return the kth element of the array
"""

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        # Solution 1
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
        
        """
        # Solution 2
        # Has a time limit exceeded
        def merger(arr, start=0, end=None):

            if end is None:
                end = len(arr) -1

            if start < end:

                pivot = partition(arr, start, end)
                merger(arr, start, pivot-1)
                merger(arr, pivot+1, end)

            return arr

        def partition(arr, start=0, end=None):
            if end is None:
                end = len(arr)-1
            
            l, r = start, end-1

            while r > l:

                if arr[l] > arr[end]:
                    l += 1
                
                elif arr[r] <= arr[end]:
                    r -= 1

                else:
                    arr[l], arr[r] = arr[r], arr[l]

            if arr[l] < arr[end]:
                arr[l], arr[end] = arr[end], arr[l]
                return l
            
            return end
        
        sorted_list = merger(nums)

        return sorted_list[k-1]
        """
