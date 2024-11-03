# coding:: utf-8
#
# Generate Binary Strings Of Length N
#   Given a number n, generate all possible binary strings of length n.
#
#   A string consisting of only 0s and 1s is called a binary string.
#   Return the output list in any order.
#
# Example 1:
#   Input: n = 3
#   Output: ["000", "001", "010", "011", "100", "101", "110", "111"]
#
#  Constraints:
#   1 <= n <= 16

import unittest
import random
from typing import List

def get_binary_strings(n):
    """
    Args:
     n(int32)
    Returns:
     list_str
    """
    # Solution:
    #   recursively branch out to build binary string with 0 and 1
    #       binary_string(n, slate) = binary_string(n-1, "0"+slate) and binary_string(n-1, "1"+slate)
    #       base condition is where n == 0 add the slate to the list.
    #
    #   Time Complexity: O(2^n)
    #   Space Compelxity: O(n) callstack + O(n) string + O(2^n) output
    #
    # Edge cases:
    if n == 0:
        return []
    
    binary_strings = []
    def binary_string(ln: int, slate: List) -> None:
        if ln == 0:
            binary_strings.append(''.join(slate))
            return
        
        slate.append('0')
        binary_string(ln-1, slate)
        slate.pop()

        slate.append('1')
        binary_string(ln-1, slate)
        slate.pop()

    binary_string(n, [])
    return binary_strings
    
class Testcase(unittest.TestCase):
    def test_example1(self):
        n = 3
        actual = get_binary_strings(n)
        expected = ["000", "001", "010", "011", "100", "101", "110", "111"]
        self.assertListEqual(expected, actual, "Example1") 

    def test_zero(self):
        n = 0
        actual = get_binary_strings(n)
        expected = []
        self.assertListEqual(expected, actual, "zero") 
    
    def test_one(self):
        n = 1
        actual = get_binary_strings(n)
        expected = ["0", "1"]
        self.assertListEqual(expected, actual, "one") 
        
    def test_two(self):
        n = 2
        actual = get_binary_strings(n)
        expected = ["00", "01", "10", "11"]
        self.assertListEqual(expected, actual, "two") 
        

if __name__ == '__main__':
    unittest.main()