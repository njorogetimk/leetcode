from count_n_say import Solution

def test_usecase_1() -> None:
    solve = Solution()

    assert solve.countAndSay(1) == '1'

def test_usecase_2() -> None:
    solve = Solution()

    assert solve.countAndSay(4) == '1211'