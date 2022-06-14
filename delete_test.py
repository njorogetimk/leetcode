from delete import Solution

solve = Solution()

def test_use_1() -> None:
    """Input: word1 = "sea", word2 = "eat" """

    assert solve.minDistance("sea", "eat") == 2

def test_use_2() -> None:
    """Input: word1 = "leetcode", word2 = "etco" """

    assert solve.minDistance("leetcode", "etco") == 4