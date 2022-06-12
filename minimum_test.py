from minimum import Solution

solve = Solution()


def test_use_1() -> None:
    """Input: nums = [1,1,4,2,3], x = 5"""
    nums = [1,1,4,2,3]
    x = 5

    assert solve.minOperations(nums, x) == 2


def test_use_2() -> None:
    """Input: nums = [5,6,7,8,9], x = 4"""
    nums = [5,6,7,8,9]
    x = 4

    assert solve.minOperations(nums, x) == -1

def test_use_3() -> None:
    """Input: nums = [3,2,20,1,1,3], x = 10"""
    nums = [3,2,20,1,1,3]
    x = 10

    assert solve.minOperations(nums, x) == 5


def test_use_4() -> None:
    """Input: nums = [4,5,2,20,1,1,3,3], x = 10"""
    nums = [4,5,2,20,1,1,3,3]
    x = 10

    assert solve.minOperations(nums, x) == 3

def test_use_5() -> None:
    """Input: nums = [4,3,2,20,1,1,3,3], x = 10"""
    nums = [4,3,2,20,1,1,3,3]
    x = 10

    assert solve.minOperations(nums, x) == 3


def test_use_6()-> None:
    """[10,1,1,1,1,1], 5"""

    assert solve.minOperations([10,1,1,1,1,1], 5) == 5


def test_use_7()-> None:
    """[10,1,1,1,1,1], 5"""

    assert solve.minOperations([1,1,1,1,1,10], 5) == 5

def test_use_8() -> None:
    """[1,1], 3"""

    assert solve.minOperations([1,1], 3) == -1

def test_use_9() -> None:
    """[8828,9581,49,9818,9974,9869,9991,10000,10000,10000,9999,9993,9904,8819,1231,6309], 134365"""

    assert solve.minOperations([8828,9581,49,9818,9974,9869,9991,10000,10000,10000,9999,9993,9904,8819,1231,6309], 134365) == 16