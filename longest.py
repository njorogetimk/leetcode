"""
Purpose: Get longest string from a string of characters
"""


class get_longest:

    def __init__(self, strs):
        self.strs = strs

    def get_long(self):
        # Check if the input is a list
        # Check length of the string
        # Return the longest prefix if present

        if len(self.strs) == 1:
            if len(self.strs[0]) > 200:
                return f'{self.strs[0]} is too long'
            elif not self.strs[0].islower():
                return 'Must be lowercase only'
            return self.strs[0]
        elif len(self.strs) > 200:
            return "Too many characters to compare"

        for word in self.strs:
            # Check if the word meets the constrains
            if len(word) > 200:
                return f'{word} is too long'
            elif len(word) == 0:
                return ''
            elif not word.islower():
                return 'Must be lowercase only'
        # Pick the first word
        # Check if there is a repeat of a prefix

        first = self.strs[0]
        counter = 1
        winner = ''
        for char in first:
            prefix = first[0:counter]
            temp = 0
            for word in self.strs:
                if len(word) < len(prefix):
                    # prefix = 'ganner' word = 'gain'
                    break

                if word[0:counter] == prefix:
                    temp += 1
                else:
                    temp -= 1

            if temp == len(self.strs):
                winner = prefix
            else:
                break

            counter += 1

        return winner
