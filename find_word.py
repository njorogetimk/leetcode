"""
purpose : find words formed from a string
"""
from typing import List


def find_words(words: List[str], chars: str) -> int:
    """Gets a string of characters and returns the length of words formed"""
    length = 0  # total length of words that can be formed from chars
    for word in words:
        chars_temp = chars[:]  # copy the characters since they'll be modified
        char_count = 0  # Character count in word that's in chars
        for char in word:
            if chars_temp.find(char) >= 0:
                chars_temp = chars_temp.replace(char, '')
                char_count += 1
        if char_count == len(word):
            length += char_count
    return length
