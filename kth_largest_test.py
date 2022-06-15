from kth_largest import Solution

solve = Solution()

def test_use_1():
    """nums = [3,2,1,5,6,4], k = 2"""

    assert solve.findKthLargest(nums = [3,2,1,5,6,4], k = 2) == 5


def test_use_2():
    """nums = [3,2,3,1,2,4,5,5,6], k = 4"""

    assert solve.findKthLargest(nums = [3,2,3,1,2,4,5,5,6], k = 4) == 4