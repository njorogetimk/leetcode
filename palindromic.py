

class Solution:
    def countSubstrings(self, s: str) -> int:

        if s.strip() == '' or type(s) != str:
            return 0
        N = len(s)
        ans = 0
        for center in range(2*N - 1):
            left = center // 2
            right = left + center % 2
            while left >= 0 and right < N and s[left] == s[right]:
                ans += 1
                left -= 1
                right += 1
        return ans
