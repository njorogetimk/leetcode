"""
Given an integer n, return n number of rows of the 
Pascal's triange.
Input: Integer n
Output: List with n rows of the triangle
"""
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        # def get_ptr(n, tri = [[1]]):

        #     if n == 1:
        #         return tri
            
        #     n -= 1 
        #     prev_row = tri[-1]
        #     curr_row = [1]
            
        #     for i in range(len(prev_row)-1):
        #         curr_row.append(prev_row[i]+prev_row[i+1])
            
        #     curr_row.append(1)
        #     tri.append(curr_row)

        #     p_tr_n = get_ptr(n, tri)

        #     return p_tr_n
        
        # return get_ptr(numRows)

        # def helper(n):
        #     if n:
        #         helper(n-1)                 # generate above row first
        #         ans.append([1]*n)           # insert current row into triangle
        #         for i in range(1, n-1):     # update current row values using above row
        #             ans[n-1][i] = ans[n-2][i] + ans[n-2][i-1]
        # ans = []
        # helper(numRows)
        # return ans

        # def get_rows(n):

        #     if n:
        #         print(n)
        #         get_rows(n-1)
        #         p_tri.append([1]*n)
        #         # print(p_tri, n)
        #         # print('----')
        #         for i in range(1, n-1):
        #             p_tri[n-1][i] = p_tri[n-2][i] + p_tri[n-2][i-1]

        # p_tri = []
        # get_rows(numRows)

        # return p_tri

        p_tri = [[1]*i for i in range(1,numRows+1)]

        for i in range(2,len(p_tri)):
            for j in range(1, len(p_tri[i])-1):
                p_tri[i][j] = p_tri[i-1][j-1]+p_tri[i-1][j]
        
        return p_tri
        
            
            
        