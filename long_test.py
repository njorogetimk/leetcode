

from long import Solution


solve = Solution()

def test_use_1() -> None:
    """Input: words = ["a","b","ba","bca","bda","bdca"]"""

    assert solve.longestStrChain(["a","b","ba","bca","bda","bdca"]) == 4

def test_use_2() -> None:
    """Input: words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]"""

    assert solve.longestStrChain(["xbc","pcxbcf","xb","cxbc","pcxbc"]) == 5

def test_use_3() -> None:
    """Input: words = ["abcd","dbqca"]"""

    assert solve.longestStrChain(["abcd","dbqca"]) == 1