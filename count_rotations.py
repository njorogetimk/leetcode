from typing import List

def binary_search(hi: int, lo: int, condition):
    mid = (hi + lo)//2
    result = condition(mid)

    if result == 'found':
        return mid
    elif result == 

class Solution:
    def count_rotations(self, nums: List[int]) -> int:
        pass