class Solution:
    def longestPalindrome(self, s: str) -> str:
        pals = ''
        start = 0
        width = 1

        if len(s) == 1:
            return s
        
        for i in range(len(s)):
            end = width
            while end <= len(s):
                chars = s[start:end]
                print(chars)
                pali = palindrome(chars)

                if pali:
                    pals = chars if len(chars)>len(pals) else pals

                start += 1
                end += 1
            
            width += 1
            start = 0

        
        return pals


def palindrome(chars):
    chars_r = list(chars)
    chars_r.reverse()

    chars_r = ''.join(chars_r)

    if chars == chars_r:
        return True
    else:
        return False
