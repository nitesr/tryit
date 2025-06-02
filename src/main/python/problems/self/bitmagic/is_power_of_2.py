"""
Given a number, check if its power of 2

Examples:
    Input: 2
    Output: True

    Input: 6
    Output: False
"""

import math
def is_power_of_2(n) -> bool:
    if n == 0:
        return False
    
    k = int(math.log2(n & ~(n-1)))
    return n & ~(1 << k) == 0

if __name__ == '__main__':
    x = 23; # 00010111

    # Output is False
    print(is_power_of_2(6));

    # Output is True
    print(is_power_of_2(2));

    # Output is True
    print(is_power_of_2(8));

    # Output is True
    print(is_power_of_2(0));
    