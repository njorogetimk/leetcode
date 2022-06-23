

from climb import Solution


solve = Solution()

def test_use_1():
    """ n = 2 """

    assert solve.climbStairs(2) == 2


def test_use_2():
    """ n = 3 """

    assert solve.climbStairs(3) == 3


def test_use_3():
    """ n = 4 """

    assert solve.climbStairs(4) == 5


def test_use_4():
    """ n = 1 """

    assert solve.climbStairs(1) == 1

def test_use_5():
    """ n = 5"""

    assert solve.climbStairs(5) == 8

def test_use_6():
    """ n = 6"""

    assert solve.climbStairs(45) == 1836311903