

from palindrome import Solution


solve = Solution()

def test_use_1():
    """Input: s = "babad" """

    assert solve.longestPalindrome("babad") == "bab"


def test_use_2():
    """Input: s = "cbbd" """

    assert solve.longestPalindrome("cbbd") == "bb"

def test_use_3():
    """Input: s = "aa" """

    assert solve.longestPalindrome("aa") == "aa"