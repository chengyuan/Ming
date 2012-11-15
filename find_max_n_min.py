# find max and min in a list of numbers
# time complexity: O(1.5N)

import sys

def find_max_min(array):
    max_num = -sys.maxint
    min_num = sys.maxint
    
    offset = len(array) % 2

    for idx in range(0, len(array) - offset, 2 ):
        first = array[idx]
        second = array[idx + 1]
        if first < second:
            first, second = second, first
        if first > max_num:
            max_num = first
        if second < min_num:
            min_num = second

    if offset:
        if array[-1] > max_num:
            max_num = array[-1]
        elif array[-1] < min_num:
            min_num = array[-1]

    return max_num, min_num

print find_max_min([2,1,3,4,5,6,7])
