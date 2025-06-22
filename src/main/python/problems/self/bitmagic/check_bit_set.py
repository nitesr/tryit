"""
Given an unsigned integer n and k. The task is to check if kth bit is set

Example:
    Input: 23, 2
    Output: True
    Explanation: 23 (00010111) 0th, 1st, 2nd, 4th bit are set.
"""

def check_bit_set(num, k):
    return num & (1 << k) != 0

if __name__ == '__main__':

    # Output is True # 00010111
    print(check_bit_set(23, 2))

    # Output is False # 00010111
    print(check_bit_set(23, 3))


