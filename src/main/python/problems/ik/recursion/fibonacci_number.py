# coding:: utf-8
#
# Fibonacci Number
#   Given a number n, find the n-th Fibonacci Number.
#   In mathematics, the Fibonacci numbers, commonly denoted Fn, form a sequence, called the Fibonacci sequence, 
#       such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
#       F(0) = 0, F(1) = 1 and F(n) = F(n − 1) + F(n − 2) for n > 1.
# Example 1:
#   Input: n = 2
#   Output: 1
#   Explanation: 2nd Fibonacci Number is the sum of the 0th and 1st Fibonacci Number = 0 + 1 = 1.
#
#  Constraints:
#   0 <= n <= 46
#   
import unittest
import random
from typing import List

def find_fibonacci(n):
    """
    Args:
     n(int32)
    Returns:
     int32
    """
    # Solution:
    #   fib(n) = fib(n-1) + fib(n-2)
    #   solution 1: we can have recursive function
    #       Time Complexity: O(2^n)
    #       Space complexity: O(n) - call stack
    #   solution 2: we can start with base cases and iteratively add up previous two values
    #       Time Complexity: O(n)
    #       Space complexity: O(1)
    #   solution 3: solution 1 + memoization so the same number is not computed again
    #       Time Complexity: O(n)
    #       Space complexity: O(n) - call stack + o(n) for memoization
    #   solution 4: try finding out the fibonanchi number thinking we have previous numbers
    #       fib(n, b1, b2) -> fib(n-1, b2, b1+b2) -> as n gets 1 b2 becomes the base number for n+1 which is n
    #       Time Complexity: O(n)
    #       Space complexity: O(n) - call stack

    # Edge cases:
    def sol1_find_fib(n: int) -> int:
        if n == 0 or n == 1:
            return n
        return sol1_find_fib(n-2) + sol1_find_fib(n-1)
    
    def sol2_find_fib(n: int) -> int:
        if n == 0 or n == 1:
            return n
        
        b1 = 0
        b2 = 1
        for i in range(2, n+1):
            b1, b2 = b2, b1 + b2
        return b2

    memo = {}
    def sol3_find_fib(n: int) -> int:
        if n == 0 or n == 1:
            return n
        if n in memo:
            return memo[n]
        
        memo[n] = sol1_find_fib(n-2) + sol1_find_fib(n-1)
        return memo[n]

    def sol4_find_fib(n: int, b1: int = 0, b2: int = 1) -> int:
        if n == 0:
            return b1
        
        if n == 1:
            return b2
        
        return sol4_find_fib(n-1, b2, b1+b2)
    
    return sol4_find_fib(n)
    
class Testcase(unittest.TestCase):
    def test_example1(self):
        n = 2
        actual = find_fibonacci(n)
        expected = 1
        self.assertEqual(expected, actual, "Example1") 

    def test_zero(self):
        n = 0
        actual = find_fibonacci(n)
        expected = 0
        self.assertEqual(expected, actual, "zero") 
    
    def test_one(self):
        n = 1
        actual = find_fibonacci(n)
        expected = 1
        self.assertEqual(expected, actual, "one") 
    
    def test_three(self):
        n = 3
        actual = find_fibonacci(n)
        expected = 2
        self.assertEqual(expected, actual, "three") 
    
    def test_four(self):
        n = 4
        actual = find_fibonacci(n)
        expected = 3
        self.assertEqual(expected, actual, "four") 
    
    def test_five(self):
        n = 5
        actual = find_fibonacci(n)
        expected = 5
        self.assertEqual(expected, actual, "five") 
    
    def test_six(self):
        n = 6
        actual = find_fibonacci(n)
        expected = 8
        self.assertEqual(expected, actual, "six") 

if __name__ == '__main__':
    unittest.main()