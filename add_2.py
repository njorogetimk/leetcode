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