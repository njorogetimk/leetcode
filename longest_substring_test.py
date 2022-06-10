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

    assert solve.lengthOfLongestSubstring('pwwkew') == 3