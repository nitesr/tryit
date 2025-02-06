# coding:: utf-8
#
# Given an array of integers, our task is to write a program that efficiently 
#   finds the second largest element present in the array. 
#  
# Example 1:
#   Input: n = [12, 35, 1, 10, 34, 1]
#   Output: 34
#   Explanation: [1, 10, 12, 34, 35] is distinct sorted array and 34 is the second largest
#
# Example 2:
#   Input: n = [1, 1, 1, 1]
#   Output: -1
#   Explanation: [1] is distinct sorted array and its length is less than 2
#
# Constraints:
#   1 <= arr[i] <= 10^5
#   0 <= len(arr) <= 10^5
#

def second_largest(arr):
    if len(arr) < 2:
        return -1
    
    max_num = arr[0]
    premax_num = float('-inf')

    for ele in arr:
        if ele > max_num:
            premax_num = max_num
            max_num = ele
        elif ele != max_num and ele > premax_num:
            premax_num = ele

    return premax_num if premax_num > float('-inf') else -1

import unittest

class Testcase(unittest.TestCase):
    def test_one(self):
        actual = second_largest([1])
        expected = -1
        self.assertEqual(expected, actual, "1") 

    def test_two_diff(self):
        actual = second_largest([1, 2])
        expected = 1
        self.assertEqual(expected, actual, "two_diff") 

    def test_two_same(self):
        actual = second_largest([1, 1])
        expected = -1
        self.assertEqual(expected, actual, "two_same") 

    def test_ascending(self):
        actual = second_largest([1, 2, 3, 3, 4, 5, 6, 7])
        expected = 6
        self.assertEqual(expected, actual, "ascending") 

    def test_descending(self):
        actual = second_largest(list(reversed([1, 2, 3, 3, 4, 5, 6, 7])))
        expected = 6
        self.assertEqual(expected, actual, "descending") 

if __name__ == '__main__':
    unittest.main()