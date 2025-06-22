"""
Given an unsigned integer n. The task is to get the rightmost unset bit

Example:
    Input: 23
    Output: 3
    Explanation: 23 (00010111), rightmost set bit is at 3rd pos

Example:
    Input: 32
    Output: 0
    Explanation: 32 (100000), rightmost unset bit is at 5th pos
"""

import math
def rightmost_unset_bit(num):
    return int(math.log(~num & ~(~num-1), 2))

if __name__ == '__main__':

    # Output is 3
    print(rightmost_unset_bit(23))

    # Output is 0
    print(rightmost_unset_bit(32))


