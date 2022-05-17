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
    
    def test_many_not_common(self):
        string = ["flower","flow","flight", "jump"]
        check = get_longest(string)
        longest = check.get_long()

        assert longest == ""

if __name__ == "__main__":
    unittest.main()