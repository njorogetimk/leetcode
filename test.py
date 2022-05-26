from count_rotations import Solution

solve = Solution()

def test_use_case_1() -> None:
    """[22, 25, 30, 1, 7, 8, 13, 17]"""

    assert solve.count_rotations([22, 25, 30, 1, 7, 8, 13, 17]) == 3

def test_use_case_2() -> None:
    """[7, 8, 13, 17, 22, 25, 30, 1]"""
    assert solve.count_rotations([7, 8, 13, 17, 22, 25, 30, 1]) == 7

def test_use_case_3() -> None:
    """[8, 9, 1, 3, 5]"""

    assert solve.count_rotations([8, 9, 1, 3, 5]) == 2

def test_use_case_4() -> None:
    """[8, 9, 1, 1, 1, 3, 5]"""

    assert solve.count_rotations([8, 9, 1, 1, 1, 3, 5]) == 2

def test_use_case_5() -> None:
    """[1, 1, 1, 1, 1, 1]"""

    assert solve.count_rotations([1, 1, 1, 1, 1, 1]) == 0

def test_edge_case_1() -> None:
    """[1]"""

    assert solve.count_rotations([1]) == 0

def test_edge_case_2() -> None:
    """[]"""

    assert solve.count_rotations([]) == 0