

from pascal import Solution


solve = Solution()

def test_use_1():
    """ n = 1 """

    assert solve.generate(1) == [[1]]


def test_use_2():
    """ N = 2 """

    assert solve.generate(2) == [[1],[1,1]]


def test_use_3():
    """ n = 3 """

    assert solve.generate(3) == [[1],[1,1],[1,2,1]]


def test_use_4():
    """ n = 5 """

    assert solve.generate(5) == [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]