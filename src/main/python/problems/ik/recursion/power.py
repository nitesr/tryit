# coding:: utf-8
#
# Power
#   Given a base a and an exponent b. Your task is to find a^b. 
#       The value could be large enough. So, calculate a^b % 1000000007.
# Example 1:
#   Input: a = 2, b = 10
#   Output: 1024
#
#  Constraints:
#   0 <= a <= 10^4
#   0 <= b <= 10^9
#   a and b together won't be 0

import unittest
import random
from typing import List


def calculate_power(a, b):
    """
    Args:
     a(int64)
     b(int64)
    Returns:
     int32
    """
    # Solution:
    #   recursively compute the value by dividing b into two almost equal parts
    #       a^b = a^(b/2) * a^(b/2) * a if b is odd else 1
    #       base condition: b == 1 return a, b == 0 return 1
    #   Time Complexity: O(2^logb)
    #   Space Compelxity: O(logb) - call stack
    #
    # Edge cases:
    if a == 0:
        return 0
    
    mod_const = 1000000007
    def calc_helper(x, y) -> int:
        if y == 0:
            return 1
        if y == 1:
            return x
        
        r = 1 if y % 2 == 0 else x
        v = calc_helper(x, y // 2) % mod_const
        return  (v * v * r) % mod_const
    
    return calc_helper(a, b)
    
class Testcase(unittest.TestCase):
    def test_example1(self):
        a = 2
        b = 10
        actual = calculate_power(a, b)
        expected = 1024
        self.assertEqual(expected, actual, "Example1") 

    def test_zero(self):
        a = 2
        b = 0
        actual = calculate_power(a, b)
        expected = 1
        self.assertEqual(expected, actual, "zero") 
    
    def test_one(self):
        a = 2
        b = 1
        actual = calculate_power(a, b)
        expected = 2
        self.assertEqual(expected, actual, "one") 
        
    def test_large(self):
        a = 1000
        b = 1000
        actual = calculate_power(a, b)
        expected = pow(1000, 1000) % 1000000007
        self.assertEqual(expected, actual, "large")     

if __name__ == '__main__':
    unittest.main()