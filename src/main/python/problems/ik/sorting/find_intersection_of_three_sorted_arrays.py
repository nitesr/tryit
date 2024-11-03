# coding:: utf-8
#
# Intersection Of Three Sorted Arrays
#   Given three arrays sorted in the ascending order, return their intersection sorted array in the ascending order.
#
# If the intersection is empty, return an array with one element -1.
#
# Example 1:
#   Input: 
#       arr1 = [2, 5, 10], arr2 = [2, 3, 4, 10], arr3 = [2, 4, 10]
#   Output: [2, 10]
#
# Example 2:
#   Input: 
#       arr1 = [1, 2, 3], arr2 = [], arr3 = [1, 2]
#   Output: [-1]
#
# Example 3:
#   Input: 
#       arr1 = [1, 2, 2, 2, 9], arr2 = [1, 1, 2, 2], arr3 = [1, 1, 1, 2, 2, 2]
#   Output: [1, 2, 2]
#
#   Constraints:
#   0 <= length of each given array <=  10^5
#   0 <= any value in a given array <= 2 * 10^6
#   
import unittest
import random
from typing import List

def find_intersection(arr1, arr2, arr3):
    """
    Args:
     arr1(list_int32)
     arr2(list_int32)
     arr3(list_int32)
    Returns:
     list_int32
    """
    # Solution:
    #  We can use three pointers to traverse each of the array
    #   as the arrays are sorted we can compare the current positions and 
    #       1. if not common across three positions, navigate the smallest to next greater number
    #       2. if common, navigate all three pointers to next position
    # Time complexity: O(m + n + k)
    # Space Complexity: O(m + n + k)

    # Edge cases:
    def is_empty(arr):
       return arr is None or len(arr) == 0
    
    if is_empty(arr1) or is_empty(arr2) or is_empty(arr3):
        return [-1]
    
    ptr1 = 0; ptr2 = 0; ptr3 = 0

    sol = []
    while ptr1 < len(arr1) and ptr2 < len(arr2) and ptr3 < len(arr3):
        # print(arr1[ptr1], arr2[ptr2], arr3[ptr3])
        if arr1[ptr1] == arr2[ptr2] and arr2[ptr2] == arr3[ptr3]:
            sol.append(arr1[ptr1])
            ptr1 += 1
            ptr2 += 1
            ptr3 += 1
        else:
            if arr1[ptr1] <= arr2[ptr2] and arr1[ptr1] <= arr3[ptr3]:
                ptr1 += 1
            elif arr2[ptr2] <= arr1[ptr1] and arr2[ptr2] <= arr3[ptr3]:
                ptr2 += 1
            else:
                ptr3 += 1

    return sol or [-1]

class Testcase(unittest.TestCase):
    def test_example1(self):
        arr1 = [2, 5, 10]
        arr2 = [2, 3, 4, 10]
        arr3 = [2, 4, 10]
        actual = find_intersection(arr1, arr2, arr3)
        expected = [2, 10]
        self.assertListEqual(expected, actual, "Example1") 

    def test_example2(self):
        arr1 = [1, 2, 3]
        arr2 = []
        arr3 = [2, 2]
        actual = find_intersection(arr1, arr2, arr3)
        expected = [-1]
        self.assertListEqual(expected, actual, "Example2") 

    def test_example3(self):
        arr1 = [1, 2, 2, 2, 9]
        arr2 = [1, 1, 2, 2]
        arr3 = [1, 1, 1, 2, 2, 2]
        actual = find_intersection(arr1, arr2, arr3)
        expected = [1, 2, 2]
        self.assertListEqual(expected, actual, "Example3") 

    def test_non_empty_no_intersection(self):
        arr1 = [1, 2, 3, 81]
        arr2 = [4, 5, 6, 108]
        arr3 = [7, 8, 9, 10]
        actual = find_intersection(arr1, arr2, arr3)
        expected = [-1]
        self.assertListEqual(expected, actual, "non_empty_no_intersection") 

    def test_more_than_one_empty(self):
        arr1 = []
        arr2 = [1]
        arr3 = []
        actual = find_intersection(arr1, arr2, arr3)
        expected = [-1]
        self.assertListEqual(expected, actual, "more_than_one_empty") 


    def test_mid_element_common(self):
        arr1 = [3, 30, 300]
        arr2 = [3, 30]
        arr3 = [30, 300]
        actual = find_intersection(arr1, arr2, arr3)
        expected = [30]
        self.assertListEqual(expected, actual, "mid_element_common")

if __name__ == '__main__':
    unittest.main()