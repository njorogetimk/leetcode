from longest_substring import Solution

solve = Solution()

def test_use_1() -> None:
    """Input: s = 'abcabcbb'"""

    assert solve.lengthOfLongestSubstring('abcabcbb') == 3

def test_use_2() -> None:
    """Input: s = 'bbbbb'"""

    assert solve.lengthOfLongestSubstring("bbbbb") == 1

def test_use_3() -> None:
    """Input: s = 'pwwkew'"""

    assert solve.lengthOfLongestSubstring('pwwewk') == 3

def test_use_4() -> None:
    """Input: s = 'dfrfdcvbghytes'"""

    assert solve.lengthOfLongestSubstring('dfrfdcvbghytes') == 12

def test_use_5() -> None:
    """Input: s = 'rftghujikhfeessxcvbnm'"""

    assert solve.lengthOfLongestSubstring("rftghujikhfeessxcvbnm") == 9