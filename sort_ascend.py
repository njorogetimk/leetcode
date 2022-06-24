from typing import List

"""
Sort a given list of integers in ascending order
"""

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        # Solution 1
        # Divide the array into single values
        # Merge the values in ascending order

    #     if len(nums) == 1:
    #         return nums
        
    #     mid = len(nums)//2

    #     left_div, right_div = self.sortArray(nums[:mid]), self.sortArray(nums[mid:])

    #     merged = self.merger(left_div, right_div)

    #     return merged
    
    # def merger(self, arr1, arr2):

    #     new_array = []

    #     i, j = 0, 0

    #     while i < len(arr1) and j < len(arr2):
    #         if arr1[i] < arr2[j]:
    #             new_array.append(arr1[i])
    #             i += 1
            
    #         else:
    #             new_array.append(arr2[j])
    #             j += 1
        
    #     return new_array + arr1[i:] + arr2[j:]

################################################################################################

        # Solution 2
        # Sort the array in place
        # Use pointers to move elements of the array in order
        # Partition the array into smaller units
        # For each partition, sort it in ascending order
        # Get the position of the smallest value in the partition
        # Use it to sort other partitions appropriately
        return self.quicksort(nums)
    
    def quicksort(self, arr, start=0, end=None):

        if end is None:
            end = len(arr)-1
        
        if start < end:
            pivot = self.partition(arr, start, end)
            self.quicksort(arr, start, pivot-1)
            self.quicksort(arr, pivot+1, end)
        
        return arr

    
    def partition(self, arr, start=0, end = None):

        if end == None:
            end = len(arr)-1
        
        l, r = start, end-1

        while l < r:

            if arr[l] <= arr[end]:
                l += 1
            
            elif arr[r] > arr[end]:
                r -= 1
            
            else:
                arr[l], arr[r] = arr[r], arr[l]
        
        if arr[l] > arr[end]:
            arr[l], arr[end] = arr[end], arr[l]

            return l
        
        return end
            

        