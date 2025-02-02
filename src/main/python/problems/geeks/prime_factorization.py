# coding:: utf-8
#
# Given a number, n find all its prime factors in non-decreasing order
#  
# Example 1:
#   Input: n = 10
#   Output: 2, 5
#   Explanation: 2 * 5 = 10
#
# Example 2:
#   Input: n = 100
#   Output: 2, 2, 5, 5
#   Explanation: 2 * 2 * 5 * 5 = 100
#
# Constraints:
#   1 <= node.value <= 10^5

from typing import List
def get_prime_table_till_sqrt_of(num: int) -> List[int]:
    x = 2
    nums = [None, None]
    while x * x <= num: nums.append(x); x += 1
    for x in range(2, len(nums)):
        if nums[x] is None:
            continue

        for y in range(x+1, len(nums)):
            if nums[y] is not None and y % x == 0:
                nums[y] = None
    
    prime_table = []
    for x in nums:
        if x is not None:
            prime_table.append(x)

    return prime_table


def find_prime_factors(n: int) -> List[int]:
    prime_table = get_prime_table_till_sqrt_of(n)
  
    factors = []
    def _factorize(num: int):
        if num < 2:
            return
        
        prime_factor = None
        for prime in prime_table:
            if num % prime == 0:
                prime_factor = prime
                factors.append(prime_factor)
                _factorize(num // prime)
                break
        
        if prime_factor is None:
            factors.append(num)

    _factorize(n)
    return factors

import unittest

class Testcase(unittest.TestCase):
    def test_10(self):
        actual = find_prime_factors(10)
        expected = self._find_prime_factors_bruteforce(10)
        self.assertListEqual(expected, actual, "10") 

    def test_100(self):
        actual = find_prime_factors(100)
        expected = self._find_prime_factors_bruteforce(100)
        self.assertListEqual(expected, actual, "100") 
    
    def test_1189(self):
        actual = find_prime_factors(1189)
        expected = [29, 41]
        self.assertListEqual(expected, actual, "1189") 
    
    def test_58(self):
        actual = find_prime_factors(58)
        expected = [2, 29]
        self.assertListEqual(expected, actual, "58") 
    
    def test_841(self):
        actual = find_prime_factors(841)
        expected = [29, 29]
        self.assertListEqual(expected, actual, "841")

    def test_min_square(self):
        actual = find_prime_factors(4)
        expected = [2, 2]
        self.assertListEqual(expected, actual, "min_square") 

    def test_min_odd_cube(self):
        actual = find_prime_factors(3**3)
        expected = [3, 3, 3]
        self.assertListEqual(expected, actual, "min_odd_cube") 

    def _find_prime_factors_bruteforce(self, n):
        def _is_prime(x: int):
            for num in range(2, x):
                if x % num == 0:
                    return False
            return True

        factors = []
        for prime in range(2, n+1):
            if not _is_prime(prime):
                continue

            y = n
            while y % prime == 0:
                factors.append(prime)
                y = y // prime

        return factors

    
    
if __name__ == '__main__':
    unittest.main()