# coding:: utf-8
#
# Count All Subsets Of A Set Of Size N
#   Given a number denoting the size of a set, count the number of unique subsets of that set.
#
#   Empty subset should also be counted.
#
# Example 1:
#   Input: n = 3
#   Output: 8
#   Explanation: f we have a set {1, 2, 3}, then all the possible subsets are: 
#       {}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}.
#
#  Constraints:
#   0 <= input number <= 30
#   
import unittest
import random
from typing import List

def count_all_subsets(n):
    """
    Args:
     n(int32)
    Returns:
     int32
    """
    # Solution:
    #   a set of size 0 can have only 1 subset
    #   a set of size 1 can have #subsets for set of size 0 without this element + #subsets for set of size 0 with this element
    #   a set of size 2 can have #subsets for set of size 1 without this element + #subsets for set of size 1 with this element
    #   ...so on
    #   count_subsets(n) = 2 * count_subsets(n-1)
    #   Time complexity: O(n)
    #   Space complexity: O(n) call-stack
    #
    #  Alternatively if we know the number of subsets is 2^n, then we can do 
    #       count_subsets(n) = count_subsets(n//2) * count_subsets(n//2) * count_subsets(1) if n is odd else 1
    #  Time complexity: o(logn)
    #  Space complexity: o(logn)
    #
    # Edge cases:

    def count_subsets(size: int) -> int:
        if size == 0:
            return 1
        if size == 1:
            return 2
        
        remainder = 1 if size % 2 == 1 else 0
        m = (count_subsets(size // 2) ** 2) * count_subsets(remainder)
        return m
    
    return count_subsets(n)

class Testcase(unittest.TestCase):
    def test_example1(self):
        n = 3
        actual = count_all_subsets(n)
        expected = 8
        self.assertEqual(expected, actual, "Example1") 

    def test_2_power(self):
        n = 8
        actual = count_all_subsets(n)
        expected = 256
        self.assertEqual(expected, actual, "2_power") 

    def test_even(self):
        n = 6
        actual = count_all_subsets(n)
        expected = 64
        self.assertEqual(expected, actual, "even")

    def test_odd(self):
        n = 7
        actual = count_all_subsets(n)
        expected = 128
        self.assertEqual(expected, actual, "odd")

    def test_one(self):
        n = 1
        actual = count_all_subsets(n)
        expected = 2
        self.assertEqual(expected, actual, "one")

    def test_zero(self):
        n = 0
        actual = count_all_subsets(n)
        expected = 1
        self.assertEqual(expected, actual, "zero")

if __name__ == '__main__':
    unittest.main()