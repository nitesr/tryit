# coding:: utf-8
#
# Count number of palindromes from 1 to n (inclusive).
#  
# Example 1:
#   Input: n = 10
#   Output: 9
#   Explanation: 1, 2, 3, 4, 5, 6, 7, 8, 9 are palindromes
#
# Example 2:
#   Input: n = 25
#   Output: 11
#   Explanation: 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22 are palindromes
#
# Constraints:
#   1 <= node.value <= 10^5
#
#
# Solution:
#   count palindromes for every length till len(n) for range(0, n+1)
#
#   given a length less than len(n), count palindromes 
#     _ -> 9
#     _ _ -> 9
#     _ _ _ -> 9 * 10
#     _ _ _ .. _ -> 9 * 10^max(0, (ln - 2 + 1) // 2)
#       if ln = 1 or 2 -> 9 * 10^0 = 9
#       if ln = 3 -> 9 * 10^1 = 90
#       if ln = 4 -> 9 * 10^1 = 90, etc..
#
#   for len(n), count palindromes
#       if digits in n are given as d1, d2, .., di, ... dn
#          and positions are given as 1, 2, ... i, .. n
#          and digits in palindrome are given as p1, p2, ..., pi, .... p2, p1
#
#          For all pi < di, we can fill in all combinations 
#          For pi == di, we need to make choices so num([p1, .. pn]) <= num([d1, .. dn])

from typing import List
from collections import deque

def to_digits(n: int) -> List[int]:
    digits = deque([])
    x = n
    while x > 0:
        digits.appendleft(x % 10)
        x = x // 10
    return list(digits)

def _count_palindromes_recursively(n: int) -> int:
    digits = to_digits(n)

    def _to_number(digits):
        num = 0
        for d in digits:
            num = num * 10 + d
        return num
    
    def _count_all_palindromes(num_len, include_lead_zero):
        if num_len <= 0:
            return 1
        
        ways_lead_digit = 10 if include_lead_zero else 9
        return ways_lead_digit * 10 ** ( max(0, num_len-2+1) // 2 )

    def _count_full_len_palindromes(d_idx, palindrome):
        num_len = len(digits)
        mid_idx = (num_len + 1) // 2 - 1

        if d_idx > mid_idx:
            return 1
        
        count = 0
        min_digit = 1 if d_idx == 0 else 0
        max_digit = digits[d_idx]

        # for all digits < digits[d_idx] at d_idx
        mid_num_len = num_len - 2 * (d_idx + 1)
        count += (max_digit - min_digit) * _count_all_palindromes(mid_num_len, True)

        # for digits[d_idx] at d_idx
        palindrome[d_idx], palindrome[num_len-1-d_idx] = max_digit, max_digit
        if d_idx < mid_idx or _to_number(palindrome) <= n:
            count += _count_full_len_palindromes(d_idx + 1, palindrome)
        palindrome[d_idx], palindrome[num_len-1-d_idx] = None, None

        return count

    count = 0
    for i in range(1, len(digits)):
        count += _count_all_palindromes(i, False)
    count += _count_full_len_palindromes(0, [None for _ in range(len(digits))])
    return count
    

def count_palindromes(n: int) -> int:
    return _count_palindromes_recursively(n)

import unittest

class Testcase(unittest.TestCase):
    def _is_palindrome(self, n):
        digits = str(n)
        lo = 0
        hi = len(digits) - 1
        while lo < hi:
            if digits[lo] != digits[hi]:
                return False
            lo += 1
            hi -= 1
        return True
    
    def _count_palindrome_bruteforce(self, n):
        count = 0
        for i in range(1, n+1):
            if self._is_palindrome(i):
                count += 1
        return count
    
    def _print_palindromes(self, i, j):
        for k in range(i, j+1):
            if self._is_palindrome(k):
                print(k, end=", ")
        print()
    
    def test_one(self):
        actual = count_palindromes(1)
        expected = self._count_palindrome_bruteforce(1)
        self.assertEqual(expected, actual, "1") 
    
    def test_15(self):
        actual = count_palindromes(15)
        expected = self._count_palindrome_bruteforce(15)
        self.assertEqual(expected, actual, "15")  
    
    def test_99(self):
        actual = count_palindromes(99)
        expected = self._count_palindrome_bruteforce(99)
        self.assertEqual(expected, actual, "99")
    
    def test_999(self):
        actual = count_palindromes(999)
        expected = self._count_palindrome_bruteforce(999)
        self.assertEqual(expected, actual, "999")
    
    def test_9999(self):
        actual = count_palindromes(9999)
        expected = self._count_palindrome_bruteforce(9999)
        self.assertEqual(expected, actual, "9999")
    
    def test_198(self):
        actual = count_palindromes(198)
        expected = self._count_palindrome_bruteforce(198)
        self.assertEqual(expected, actual, "198")
    

    def test_1988(self):
        actual = count_palindromes(1988)
        expected = self._count_palindrome_bruteforce(1988)
        self.assertEqual(expected, actual, "1988")
    
    def test_19881(self):
        actual = count_palindromes(19881)
        expected = self._count_palindrome_bruteforce(19881)
        self.assertEqual(expected, actual, "19881")

    def test_54321(self):
        actual = count_palindromes(54321)
        expected = self._count_palindrome_bruteforce(54321)
        self.assertEqual(expected, actual, "54321")

if __name__ == '__main__':
    unittest.main()