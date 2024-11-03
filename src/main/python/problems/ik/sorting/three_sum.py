# coding:: utf-8
#
# 3 Sum
#   Given an integer array arr of size n, find all magic triplets in it.
#   Magic triplet is a group of three numbers whose sum is zero.
#   Note that magic triplets may or may not be made of consecutive numbers in arr.
#   Notice that the solution set must not contain duplicate triplets.
#
# Example 1:
#   Input: 
#       arr = [10, 3, -4, 1, -6, 9]
#   Output: ["10,-4,-6", "3,-4,1"]
#
# Example 2:
#   Input: 
#       arr = [-1,0,1,2,-1,-4]
#   Output: ["-1,-1,2", "-1,0,1"]
#
# Example 3:
#   Input: 
#       arr = [0,0,0]
#   Output: ["0,0,0"]
#
# Example 4:
#   Input: 
#       arr = [0,0,0,0,0,0]
#   Output: ["0,0,0"]
#
# Constraints:
#   1 <= n <= 2000
#   -1000 <= any element of arr <= 1000
#   arr may contain duplicate numbers
#   arr is not necessarily sorted
#
# Notes:
#   Function must return an array of strings. 
#       Each string (if any) in the array must represent a unique magic triplet 
#       and strictly follow this format: "1,2,-3" (no whitespace, one comma between numbers).
#   Order of the strings in the array is insignificant. 
#       Order of the integers in any string is also insignificant. 
#       For example, if ["1,2,-3", "1,-1,0"] is a correct answer, 
#       then ["0,1,-1", "1,-3,2"] is also a correct answer.
#   Triplets that only differ by order of numbers are considered duplicates, 
#       and duplicates must not be returned. 
#       For example, if "1,2,-3" is a part of an answer, 
#       then "1,-3,2", "-3,2,1" or any permutation of the same numbers 
#       may not appear in the same answer (though any one of them may appear instead of "1,2,-3").

import unittest
import random
from typing import List

def two_sum(nums: List[int], start: int, target: int) -> List[int]:
    store = {}
    sol = []
    for i in range(start, len(nums)):
        if nums[i] in store and store[nums[i]]:
            continue

        other_num = target - nums[i]
        if other_num in store and not store[other_num]:
            sol.append([other_num, nums[i]])
            store[other_num] = True
            store[nums[i]] = True
        else:
            store[nums[i]] = False
    
    return sol



def find_zero_sum(arr : List[int]) -> List[str]:
    """
    Args:
     arr(list_int32)
    Returns:
     list_str
    """
    # Solution:
    #    We can leverage two sum solution. 
    #       Iterate over the array and find two integers whose sum is -arr[i]
    #
    # Edge cases:
    if arr is None or len(arr) < 3:
        return []
    
    sorted_arr = sorted(arr)
    n = len(sorted_arr)
    solution = []

    def two_sum_2ptr(arr_start_index, target):
        lo = arr_start_index
        hi = n-1

        while lo < hi:
            low_num = sorted_arr[lo]
            hi_num =  sorted_arr[hi]
            newsum =  low_num + hi_num

            if newsum > target:
                hi -= 1
            elif newsum < target:
                lo += 1
            else:
                solution.append(f"{-target},{low_num},{hi_num}")
                while lo < hi and sorted_arr[lo] == low_num: lo += 1
                while lo < hi and sorted_arr[hi] == hi_num: hi -= 1

    i = 0
    while i < n-2:
        num = sorted_arr[i]
        two_sum_2ptr(i+1, -num)
        while i < n and sorted_arr[i] == num: i += 1
        
    return solution


class Testcase(unittest.TestCase):
    def test_example1(self):
        arr = [10, 3, -4, 1, -6, 9]
        actual = find_zero_sum(arr)
        expected = ["-6,-4,10", "-4,1,3"]
        self.assertListEqual(expected, actual, "Example1") 

    def test_example2(self):
        arr = [-1,0,1,2,-1,-4]
        actual = find_zero_sum(arr)
        expected = ["-1,-1,2", "-1,0,1"]
        self.assertListEqual(expected, actual, "Example2")  
        
    def test_example3(self):
        arr = [0,0,0]
        actual = find_zero_sum(arr)
        expected = ["0,0,0"]
        self.assertListEqual(expected, actual, "Example3")  
        
    def test_example4(self):
        arr = [0,0,0,0,0,0]
        actual = find_zero_sum(arr)
        expected = ["0,0,0"]
        self.assertListEqual(expected, actual, "Example4") 

    def test_one_pair(self):
        arr = [10, 3, -4, -6]
        actual = find_zero_sum(arr)
        expected = ["-6,-4,10"]
        self.assertListEqual(expected, actual, "one_pair") 

    def test_no_pair(self):
        arr = [10, 3, -5, -6]
        actual = find_zero_sum(arr)
        expected = []
        self.assertListEqual(expected, actual, "no_pair") 

    def test_len_3_found(self):
        arr = [10, -4, -6]
        actual = find_zero_sum(arr)
        expected = ["-6,-4,10"]
        self.assertListEqual(expected, actual, "len_3_found") 

    def test_len_3_notfound(self):
        arr = [10, -4, -10]
        actual = find_zero_sum(arr)
        expected = []
        self.assertListEqual(expected, actual, "len_3_notfound") 

    def test_same_pairs(self):
        arr = [10, -4, -6, 3, -4, -6, 10, 3, 0, -3]
        actual = find_zero_sum(arr)
        expected = ["-6,-4,10", "-6,3,3", "-3,0,3"]
        self.assertListEqual(expected, actual, "same_pairs") 

if __name__ == '__main__':
    unittest.main()