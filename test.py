from find_first_last import Solution

def test_use_case_1() -> None:
    """nums = [5,7,7,8,8,10] target 8"""
    solve = Solution()

    assert solve.searchRange([5, 7, 7, 8, 8, 10], 8) == [3, 4]

def test_use_case_2() -> None:
    """nums = [5,7,7,8,8,10] target 10"""
    solve = Solution()

    assert solve.searchRange([5, 7, 7, 8, 8, 10], 10) == [5, 5]

def test_use_case_3() -> None:
    """nums = [5,7,8,8,8,9,10] target 8"""
    solve = Solution()

    assert solve.searchRange([5, 8, 8, 8, 8, 9, 10], 8) == [1, 4]

def test_use_case_4() -> None:
    """nums = [5,7,7,8,8,10] target 5"""
    solve = Solution()

    assert solve.searchRange([5, 7, 7, 8, 8, 10], 5) == [0, 0]

def test_use_case_5() -> None:
    """nums list of 1000 values"""
    solve = Solution()

    nums = list(i for i in range(0,10000))
    assert solve.searchRange(nums, 999) == [999, 999]

def test_edge_case_1() -> None:
    """nums = [5,7,7,8,8,10] target 6"""
    solve = Solution()
    
    assert solve.searchRange([5, 7, 7, 8, 8, 10], 6) == [-1, -1]

def test_edge_case_2() -> None:
    """nums = [] target 6"""
    solve = Solution()

    assert solve.searchRange([], 6) == [-1, -1]
