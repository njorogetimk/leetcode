from full_tree import Solution

solve = Solution()

def test_use_1():
    """ n = 7 """

    ans = [[0,0,0,None,None,0,0,None,None,0,0],[0,0,0,None,None,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,None,None,None,None,0,0],[0,0,0,0,0,None,None,0,0]]

    assert solve.allPossibleFBT(7) == ans


def test_use_2():
    """ n = 3 """

    assert solve.allPossibleFBT(3) == [[0,0,0]]


def test_use_3():
    """ n = 1 """

    assert solve.allPossibleFBT(1) == [[0]]


def test_use_4():
    """ n = 2 """

    assert solve.allPossibleFBT(2) == []

def test_use_5():
    """ n = 5 """
    assert solve.allPossibleFBT(5) == [[0,0,0,0,0,None,None], [0,0,0,None,None,0,0]]
