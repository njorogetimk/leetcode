from find_word import find_words


def test_usecase_found() -> None:
    """Characters can form words"""
    assert find_words(["cat", "bt", "hat", "tree"], "atach") == 6


def test_usecase_found2() -> None:
    """Characters can form words"""
    assert find_words(["hello","world","leetcode"], chars = "welldonehoneyr") == 10


def test_usecase_notfound() -> None:
    """Characters cannot form words"""
    assert find_words(['tom', 'ken', 'paul'], 'adfujk') == 0


def test_edgecase_noword_nochar() -> None:
    """No words and no characters"""
    assert find_words([], '') == 0


def test_edgecase_no_word() -> None:
    """No words but characters"""
    assert find_words([], 'abcs') == 0


def test_edgecase_nochar() -> None:
    """No characters to form words"""
    assert find_words(['tom', 'tim'], '') == 0
