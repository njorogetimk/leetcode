class get_longest:
    def get_long(self, strs):
        # initialize the tally

        tally = {}
        winner = ""
        for word in strs:
            for i in range(len(word)):
                char = word[:i+1]
                tally[char] = tally[char]+1 if tally.get(char, False) else 1

        new_tally = tally.copy()
        for prefix, number in tally.items():
            if number == 1:
                new_tally.pop(prefix)
        
        new_tally_prefixes = new_tally
        
        number = 0
        for prefix, count in new_tally_prefixes.items():
            if count > number:
                winner = prefix
                number = count
            elif len(prefix) > len(winner) and count == number:
                winner = prefix
                number = count

        return  winner

