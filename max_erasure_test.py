from max_erasure import Solution

solve = Solution()

def test_use_1() -> None:
    """Input: nums = [4,2,4,5,6]"""

    assert solve.maximumUniqueSubarray([4,2,4,5,6]) == 1

def test_use_2() -> None:
    """Input: nums = [5,2,1,2,5,2,1,2,5]"""

    assert solve.maximumUniqueSubarray([5,2,1,2,5,2,1,2,5]) == 8