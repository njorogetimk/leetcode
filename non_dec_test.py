

from non_dec import Solution


solve = Solution()


def test_use_1():
    """ Input: nums = [4,2,3] """

    assert solve.checkPossibility([4,2,3]) == True


def test_use_2():
    """ Input: nums = [4,2,1] """

    assert solve.checkPossibility([4,2,1]) == False

def test_use_3():
    """ Input: nums = [1,1,1] """

    assert solve.checkPossibility([1,1,0,0]) == True