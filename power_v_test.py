

from power_v import Solution


solve = Solution()

def test_use_1():
    """lo = 12, hi = 15, k = 2 Output: 13"""

    assert solve.get_power(12,15,2) == 13


def test_use_2():
    """ Input: lo = 7, hi = 11, k = 4 """

    assert solve.get_power(7, 11, 4) == 7


def test_edge_1():
    """ Input: lo = 1, hi = 1000, k = 1000 """

    assert solve.get_power(1, 1000, 1000) == 871