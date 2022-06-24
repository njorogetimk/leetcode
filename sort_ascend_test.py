

from sort_ascend import Solution


solve = Solution()

def test_use_1():
    """ [5,2,3,1] """

    assert solve.sortArray([5,2,3,1]) == [1,2,3,5]


def test_use_2():
    """ [5,1,1,2,0,0] """

    assert solve.sortArray([5,1,1,2,0,0]) == [0,0,1,1,2,5]