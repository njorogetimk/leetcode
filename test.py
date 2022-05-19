from add_2 import add_2

def test_usecase_1() -> None:
    """Add two lists of the same length"""
    assert add_2([2,4,3], [5,6,4]) == [7,0,8]


def test_usecase_2() -> None:
    """Add two lists containing zeroes"""
    assert add_2([0], [0]) == [0]


def test_usecase_3() -> None:
    """Add two lists of nonequal length"""
    assert add_2([9,9,9,9,9,9,9], [9,9,9,9]) == [8,9,9,9,0,0,0,1]

def test_edgecase_1() -> None:
    """Test for an empty list"""
    assert add_2([], []) == []

def test_edgecase_2() -> None:
    """Test single empty list"""
    assert add_2([], [3]) == [3]