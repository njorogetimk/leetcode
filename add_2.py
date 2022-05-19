from typing import List

def add_2(l1: List[int], l2: List[int]) -> List[int]:
    # Check for empty lists in both
    if len(l1) == 0 and len(l2) == 0:
        return []
    # add trailing zeroes to the shorter lists
    ext = len(l1) - len(l2)
    if ext > 0:
        # l1 length larger than l2
        # add trailing zeroes to l2
        for i in range(ext):
            l2.append(0)
    else:
        for i in range(ext*-1):
            l1.append(0)
    
    # reverse the list items
    l1.reverse()
    l2.reverse()
    
    # convert the lists to string and join them 
    l1_joined = int(''.join([str(i) for i in l1]))
    l2_joined = int(''.join([str(i) for i in l2]))
    # add the two lists
    addition = str(l1_joined + l2_joined)
    # print(addition)
    # reverse and return the list
    result = [int(i) for i in addition]
    result.reverse()
    return result