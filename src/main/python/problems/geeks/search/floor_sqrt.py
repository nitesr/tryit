# coding:: utf-8
#
# Given an integer X, find its square root. If X is not a perfect square, 
#   then return floor(√x).
#  
# Example 1:
#   Input: x = 4
#   Output: 2
#   Explanation: 4 is perfect square
#
# Example 2:
#   Input: x = 7
#   Output: 2
#   Explanation: 7 is between 4 and 9, so floor is sqrt(4) = 2
#

# Constraints:
#   1 <= x <= 10^5
#



def floor_sqrt(x):
    lo = 1
    hi = x
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if mid * mid >= x:
            hi = mid - 1
        else:
            lo = mid + 1
    
    return lo if lo * lo == x else hi

import unittest

class Testcase(unittest.TestCase):
    def test_one(self):
        actual = floor_sqrt(1)
        expected = 1
        self.assertEqual(expected, actual, "1") 

    def test_two(self):
        actual = floor_sqrt(2)
        expected = 1
        self.assertEqual(expected, actual, "two") 

    def test_four(self):
        actual = floor_sqrt(4)
        expected = 2
        self.assertEqual(expected, actual, "four") 

    def test_seven(self):
        actual = floor_sqrt(7)
        expected = 2
        self.assertEqual(expected, actual, "seven") 

    def test_nine(self):
        actual = floor_sqrt(9)
        expected = 3
        self.assertEqual(expected, actual, "nine") 

    def test_hundred(self):
        actual = floor_sqrt(100)
        expected = 10
        self.assertEqual(expected, actual, "hundred") 

    def test_hundred_one(self):
        actual = floor_sqrt(101)
        expected = 10
        self.assertEqual(expected, actual, "hundred_one") 

if __name__ == '__main__':
    unittest.main()