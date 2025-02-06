# coding:: utf-8
#
# Given a sorted array arr[] with possibly duplicate elements, 
#   the task is to find indexes of the first and last occurrences of 
#   an element x in the given non-decreasing sorted array. 
#  
# Example 1:
#   Input: arr = [1, 3, 5, 5, 5, 5, 67, 123, 125], x = 5
#   Output: (2, 5)
#   Explanation: indices of 5 start at 2 and end at 5
#
# Example 2:
#   Input: arr = [1, 3, 5, 5, 5, 5, 7, 123, 125], x = 7
#   Output: (6, 6)
#   Explanation: index of 7 is at 6
#
#
# Example 2:
#   Input: arr = [1, 3, 5, 5, 5, 5, 7, 123, 125], x = 6
#   Output: (6, 5)
#   Explanation: 6 is not in the array but its insert position is at index 6
#              and last position is 5 (6-1) to show no elements in array.
#
# Constraints:
#   1 <= arr[i] <= 10^5
#   0 <= len(arr) <= 10^5
#

def _first_occurrence(arr, x):
    lo, hi = 0, len(arr)-1

    while lo <= hi:
        mid = lo + (hi-lo)//2
        if arr[mid] >= x:
            hi = mid-1
        else:
            lo = mid+1
    
    return lo

def _last_occurrence(arr, x):
    lo, hi = 0, len(arr)-1

    while lo <= hi:
        mid = lo + (hi-lo)//2
        if arr[mid] <= x:
            lo = mid+1
        else:
            hi = mid-1
    

    return hi

def first_last_occurrence(arr, x):
    f_idx = _first_occurrence(arr, x)
    if f_idx in range(0, len(arr)) and arr[f_idx] == x:
        l_idx = _last_occurrence(arr, x)
        return (f_idx, l_idx)
    
    return (f_idx, f_idx-1)

import unittest

class Testcase(unittest.TestCase):
    def test_one(self):
        actual = first_last_occurrence([1], 1)
        expected = (0, 0)
        self.assertEqual(expected, actual, "1") 

    def test_two_same(self):
        actual = first_last_occurrence([1, 1], 1)
        expected = (0, 1)
        self.assertEqual(expected, actual, "two_same") 

    def test_two(self):
        actual = first_last_occurrence([1, 2], 2)
        expected = (1, 1)
        self.assertEqual(expected, actual, "two") 
    
    def test_two_none_ending(self):
        actual = first_last_occurrence([1, 2], 3)
        expected = (2, 1)
        self.assertEqual(expected, actual, "two_none_ending") 

    def test_two_none_begining(self):
        actual = first_last_occurrence([1, 2], 0)
        expected = (0, -1)
        self.assertEqual(expected, actual, "two_none_begining") 

    def test_two_none_middle(self):
        actual = first_last_occurrence([1, 3], 2)
        expected = (1, 0)
        self.assertEqual(expected, actual, "two_none_middle") 

    def test_five_none_ending(self):
        actual = first_last_occurrence([1, 2, 6, 7, 9], 10)
        expected = (5, 4)
        self.assertEqual(expected, actual, "five_none_ending") 

    def test_five_none_begining(self):
        actual = first_last_occurrence([1, 2, 6, 7, 9], 0)
        expected = (0, -1)
        self.assertEqual(expected, actual, "five_none_begining") 

    def test_five_none_middle(self):
        actual = first_last_occurrence([1, 2, 6, 7, 9], 5)
        expected = (2, 1)
        self.assertEqual(expected, actual, "five_none_middle") 

    def test_more_duplicates(self):
        actual = first_last_occurrence([1, 2,3,4,4,4,5,6,8,8,9], 4)
        expected = (3, 5)
        self.assertEqual(expected, actual, "more_duplicates") 

    def test_more_none(self):
        actual = first_last_occurrence([1, 2,3,4,4,4,5,6,8,8,9], 7)
        expected = (8, 7)
        self.assertEqual(expected, actual, "more_none") 

if __name__ == '__main__':
    unittest.main()