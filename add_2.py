
"""
from typing import List
from collections import deque

def summed(llist):
    sum = 0
    start = 1
    base = 10

    for value in llist:
        sum = sum + value * start
        start = start * base
    return sum

def add_2(l1: List[int], l2: List[int]) -> List[int]:
    llist1 = deque(l1)
    llist2 = deque(l2)

    total = summed(llist1) + summed(llist2)

    result = [int(i) for i in list(deque(str(total)))]
    result.reverse()
    return result
"""

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)
        result_tail = result
        carry = 0
                
        while l1 or l2 or carry:            
            val1  = (l1.val if l1 else 0)
            val2  = (l2.val if l2 else 0)
            carry, out = divmod(val1+val2 + carry, 10)    
                      
            result_tail.next = ListNode(out)
            result_tail = result_tail.next                      
            
            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)
               
        return result.next