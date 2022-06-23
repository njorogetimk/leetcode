"""
Given an integer n, return n number of rows of the 
Pascal's triange.
Input: Integer n
Output: List with n rows of the triangle
"""
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        def get_ptr(n, tri = [[1]]):

            if n == 1:
                return tri
            
            n -= 1 
            prev_row = tri[-1]
            curr_row = [1]
            
            for i in range(len(prev_row)-1):
                curr_row.append(prev_row[i]+prev_row[i+1])
            
            curr_row.append(1)
            tri.append(curr_row)

            p_tr_n = get_ptr(n, tri)

            return p_tr_n
        
        return get_ptr(numRows)



            
            
        