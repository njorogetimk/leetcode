"""
When climbing stairs, it takes n steps to get to the top.
One can take one or a maximum of two steps at a time.
Get the number of distinct ways one can get to the top.
"""

from itertools import permutations

class Solution:
    def climbStairs(self, n: int) -> int:
        
        """
        mem = {}
        
        def get_arrangements(twos, ones):
            inputs = [2]*twos+[1]*ones

            perms = permutations(inputs)

            for perm in perms:
                if perm in mem:
                    continue
                else:
                    mem[perm] = perm
        
        twos, ones = 0, n

        while ones >= 0:
            get_arrangements(twos, ones)
            twos += 1
            ones -= 2
        
        # print(list(mem.values()))
        return len(list(mem.values()))
        """

        # Implement Fibonacci
        """
        if n <= 0: return 0
        if n == 1: return 1
        if n == 2: return 2

        one_before = 2
        two_before = 1
        total = 0

        for i in range(2, n):
            total = one_before + two_before
            two_before = one_before
            one_before = total
        
        return total
        """

        bbf, bf = 1, 1

        for _ in range(n-1):
            bbf, bf = bf, bbf+bf
        
        return bf