"""
Given a string sequence say s, check to see if it is a subsequence of another
sequence t
Inputs: s, t
Output: boolean
"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Solution 1
        
        # Create a copy of s,
        # Loop through all characters in s
        # For each character check where it is found in t
        # If found, remove it and all characters before it in t
        # Also remove the found character from the copy of s
        # For the other characters in s, find them in t
        # If s is empty, return True, otherwise return False


        # s = [char for char in s]
        # t = [char for char in t]
        # s_copy = s[:]

        # for char1 in s:
        #     for i in range(len(t)):
        #         if char1 == t[i]:
        #             t = t[i+1:]
        #             s_copy.remove(char1)
        #             break
        
        # check = False if s_copy else True

        # return check

#################################################################################
        # Solution 2
        # 1. Create two pointers, i and j for s and t respectively
        # 2. Check if charcter s[i] is equal to character t[j]
        # 3. If True increase both pointers by one
        # 4. If not increase j by one
        # 5. Check to see if i == length of s and j <= len t
        # 6. If True, return True, i.e s is a substring of t
        # 7. put steps 2 to 6 in a while loop, with the condition
        # 8. i <= len s and j <= len t

        # i, j = 0, 0

        # if len(s) == 0:
        #     return True
        
        # if len(t) == 0:
        #     return False

        # while i < len(s) and j < len(t):
        #     if s[i] == t[j]:
        #         if i == len(s)-1:
        #             return True
                
        #         i += 1
        #         j += 1
        #     else:
        #         j += 1
            
        # return False

############################################################################        
        # Solution 3
        # Create a pointers i
        # loop through characters in t
        # if the character in t matches the on in s[i]
        # increase i by one
        # in the end check if i is equal to len(s)
        # Return True for a substring found otherwise False

        i = 0

        if len(s) == 0: return True
        if len(t) == 0: return False
        if len(s) > len(t): return False

        for char in t:
            if s[i] == char:
                i += 1
            if i >= len(s):
                break
        
        return i == len(s)