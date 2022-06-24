

from subseq import Solution


solve = Solution()

def test_use_1():
    """ s = "abc", t = "ahbgdc" """

    assert solve.isSubsequence("abc", "ahbgdc") == True


def test_use_2():
    """ s = "axc", t = "ahbgdc" """

    assert solve.isSubsequence("axc", "ahbgdc") == False