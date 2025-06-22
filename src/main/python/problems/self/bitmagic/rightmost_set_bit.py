"""
Given an unsigned integer n. The task is to get the rightmost set bit

Example:
    Input: 23
    Output: 0
    Explanation: 23 (00010111), rightmost set bit is at 0th pos

Example:
    Input: 32
    Output: 5
    Explanation: 32 (100000), rightmost set bit is at 5th pos
"""

import math
def rightmost_set_bit(num):
    return int(math.log(num & ~(num-1), 2))

if __name__ == '__main__':

    # Output is 0
    print(rightmost_set_bit(23))

    # Output is 5
    print(rightmost_set_bit(32))


