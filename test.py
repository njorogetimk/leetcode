from palindromic import Solution

solve = Solution()

def test_use_case_1() -> None:
    """ Input: s = "abc" """

    assert solve.countSubstrings('abc') == 3

def test_use_case_2() -> None:
    """ Input: s = "aaa" """

    assert solve.countSubstrings('aaa') == 6

def test_use_case_3() -> None:
    """ Input: s = "abcba" """

    assert solve.countSubstrings('adcda') == 7

def test_use_case_4() -> None:
    """ Input: s = "aaaaa" """

    assert solve.countSubstrings('aaaaa') == 15

def test_use_case_5() -> None:
    """ Input: s = "aaaaaaa" """

    assert solve.countSubstrings('aaaaaa') == 21

def test_edge_case_1() -> None:
    """ Input: s = "" """

    assert solve.countSubstrings('') == 0

def test_edge_case_2() -> None:
    """ Input: s = "  " """
    assert solve.countSubstrings('  ') == 0