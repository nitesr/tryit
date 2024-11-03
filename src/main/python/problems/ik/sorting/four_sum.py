# coding: utf-8
#
# 4 Sum
#   Given a list of numbers, find all the unique quadruples that sum up to a given target value.
#   Note that quadruples may or may not be made of consecutive numbers in arr.
#   Notice that the solution set must not contain duplicate quadruples.
#   Two quadruples are considered different 
#       if there exists a number whose frequencies differ in those two quadruples.
#   The quadruples can be returned in any order.
#   The order of numbers inside any quadruple does not matter.
#
# Example 1:
#   Input: 
#       arr = [0, 0, 1, 3, 2, -1], target = 3
#   Output: [ [-1, 0, 1, 3], [0, 0, 1, 2] ]
#
#
# Constraints:
#   1 <= size of the input list <= 300
#   -10^5 <= any element of the input list <= 10^5
#   -4 * 10^5 <= target value <= 4 * 10^5
#   arr is not necessarily sorted

import unittest
import random
from typing import List



def four_sum(arr, target):
    """
    Args:
     arr(list_int32)
     target(int32)
    Returns:
     list_list_int32
    """
    # Solution:
    #    We can leverage three sum solution, for each element in array find the three sum
    #
    # Edge cases:
    if arr is None or len(arr) < 4:
        return []
    
    sorted_arr = sorted(arr)
    n = len(sorted_arr)
    solution = []

    def two_sum_2ptr(two_sum_start_index, four_sum_num, three_sum_num):
        two_sum_target = target - three_sum_num - four_sum_num
        lo = two_sum_start_index
        hi = n-1

        while lo < hi:
            low_num = sorted_arr[lo]
            hi_num =  sorted_arr[hi]
            newsum =  low_num + hi_num

            if newsum > two_sum_target:
                hi -= 1
            elif newsum < two_sum_target:
                lo += 1
            else:
                solution.append([four_sum_num, three_sum_num, low_num, hi_num])
                while lo < hi and sorted_arr[lo] == low_num: lo += 1
                while lo < hi and sorted_arr[hi] == hi_num: hi -= 1

    def three_sum(three_sum_start_index, four_sum_num):
        three_sum_i = three_sum_start_index
        while three_sum_i < n-2:
            three_sum_num = sorted_arr[three_sum_i]
            two_sum_2ptr(three_sum_i+1, four_sum_num, three_sum_num)
            while three_sum_i < n and sorted_arr[three_sum_i] == three_sum_num: three_sum_i += 1

    i = 0
    while i < n-3:
        num = sorted_arr[i]
        three_sum(i+1, num)
        while i < n and sorted_arr[i] == num: i += 1
        
    return solution


class Testcase(unittest.TestCase):
    def test_example1(self):
        arr = [0, 0, 1, 3, 2, -1]
        target = 3
        actual = four_sum(arr, target)
        expected = [[-1, 0, 1, 3], [0, 0, 1, 2]]
        self.assertListEqual(expected, actual, "Example1") 

    def test_zeros(self):
        arr = [0, 0, 0, 0, 0]
        target = 0
        actual = four_sum(arr, target)
        expected = [[0, 0, 0, 0]]
        self.assertListEqual(expected, actual, "zeros") 
    
    def test_less_zeros(self):
        arr = [0, 0, 1]
        target = 0
        actual = four_sum(arr, target)
        expected = []
        self.assertListEqual(expected, actual, "less_zeros") 

if __name__ == '__main__':
    unittest.main()