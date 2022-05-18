import string
import unittest
from longest import get_longest

class TestProperInput(unittest.TestCase):
    def test_one_input(self):
        string = ["rachel"]
        check = get_longest(string)
        longest = check.get_long()

        assert longest == "rachel"
    
    def test_many_common(self):
        string = ["flower","flow","flight"]
        check = get_longest(string)
        longest = check.get_long()
        
        assert longest == "fl"
    
    def test_many_common2(self):
        string = ["abc", "a"]
        check = get_longest(string)
        longest = check.get_long()
        
        assert longest == "a"
    
    def test_many_not_common(self):
        string = ["flower","flow","flight", "jump"]
        check = get_longest(string)
        longest = check.get_long()

        assert longest == ""

class TestConstrains(unittest.TestCase):
    def test_array_more_200(self):
        string = []
        for i in range (201):
            string.append('njoroge')
        check = get_longest(string)
        longest = check.get_long()

        assert longest == 'Too many characters to compare'
    
    def test_word_more_200_chars(self):
        string = []
        for i in range(200):
            string.append('njoroge')
        string = [''.join(string)]

        check = get_longest(string)
        longest = check.get_long()
        assert longest == f'{string[0]} is too long'
    
    def test_word_more_200_chars_2(self):
        string = []
        for i in range(200):
            string.append('njoroge')
        string = [''.join(string)]

        string.append('matthew')

        check = get_longest(string)
        longest = check.get_long()
        assert longest == f'{string[0]} is too long'
    
    def test_lower_case_only(self):
        string = ['Tom']
        check = get_longest(string)
        longest = check.get_long()

        assert longest == 'Must be lowercase only'
    
    def test_lower_case_only_2(self):
        string = ['Tom', 'john']
        check = get_longest(string)
        longest = check.get_long()

        assert longest == 'Must be lowercase only'
    
        

if __name__ == "__main__":
    unittest.main()