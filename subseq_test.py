

from subseq import Solution


solve = Solution()

def test_use_1():
    """ s = "abc", t = "ahbgdc" """

    assert solve.isSubsequence("abc", "ahbgdc") == True


def test_use_2():
    """ s = "axc", t = "ahbgdc" """

    assert solve.isSubsequence("axc", "ahbgdc") == False


def test_use_3():
    """ s = "aaa", t = "ababbab" """

    assert solve.isSubsequence("aaa", "ababbab") == True


def test_use_4():
    """ s = "aa", t = "abbbb" """

    assert solve.isSubsequence("aa", "abbbb") == False

def test_use_5():
    """ s ="acb" t = "ahbgdc" """

    assert solve.isSubsequence("acb", "ahbgdc") == False

def test_use_6():
    """ s = 'rfdc' t = 'wdrjkfndoc' """

    assert solve.isSubsequence('rfdc', 'wdrjkfndoc') == True

def test_edge_1():

    s = "sdfgt"*20
    t = "edwws"*20

    assert solve.isSubsequence(s, t) == False

def test_edge_2():
    """ '', 'were' """

    assert solve.isSubsequence('', 'were') == True


def test_edge_3():
    """ 'were', '' """

    assert solve.isSubsequence('were', '') == False


def test_edge_4():
    """ 'wsdrfgty', 'edfr' """

    assert solve.isSubsequence('wsdrfgty', 'edfr') == False