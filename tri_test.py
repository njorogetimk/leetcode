from tri import Solution

solve = Solution()

def test_use_1() -> None:
    """Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]"""

    assert solve.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]) == 11


def test_use_2() -> None:
    """Input: triangle = [[-10]]"""

    assert solve.minimumTotal([[-10]]) == -10

def test_use_3() -> None:
    """Input: triangle = [[2],[3,4],[6,6,6],[1,3,7,5]]"""

    assert solve.minimumTotal([[2],[3,4],[6,6,6],[1,3,7,5]]) == 12

def test_use_4() -> None:
    """Input: triangel = [[-1],[2,3],[1,-1,-3]]"""

    assert solve.minimumTotal([[-1],[2,3],[1,-1,-3]]) == -1