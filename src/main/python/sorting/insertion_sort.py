# coding:: utf-8
#
# Leetcode Problem: 912. Sort an Array
#   Given an array of integers nums, sort the array in ascending order and return it.
#
# Example 1:
#   Input: nums = [5,2,3,1]
#   Output: [1,2,3,5]
#   Explanation: After sorting the array, 
#       the positions of some numbers are not changed (for example, 2 and 3), 
#        while the positions of other numbers are changed (for example, 1 and 5).
#
# Example 2:
#   Input: nums = [5,1,1,2,0,0]
#   Output: [0,0,1,1,2,5]
#   Explanation: Note that the values of nums are not necessairly unique.
#
# Constraints:
#   1 <= nums.length <= 5 * 10^4
#   -5 * 10^4 <= nums[i] <= 5 * 10^4

import unittest
from typing import List

def swap(nums: List[int], src_pos: int, dest_pos: int) -> List[int]:
    if src_pos == dest_pos:
        return nums
    
    nums[src_pos], nums[dest_pos] = nums[dest_pos], nums[src_pos]
    return nums

def insertion_sort(nums: List[int]) -> List[int]:
    # Solution:
    #   keep sorting the array from left by adding/inserting a new element at each time
    if nums is None or len(nums) <= 1:
        return nums

    for i in range(0, len(nums)):
        for j in range(i, 0, -1):
            if nums[j] < nums[j-1]:
                swap(nums, j-1, j)
            else:
                break
    
    return nums



class Testcase(unittest.TestCase):
    def test_example1(self):
        nums = [5,2,3,1]
        actual = insertion_sort(nums)
        expected = [1,2,3,5]
        self.assertListEqual(expected, actual, "Example1")
    
    def test_example2(self):
        nums = [5,1,1,2,0,0]
        actual = insertion_sort(nums)
        expected = [0,0,1,1,2,5]
        self.assertListEqual(expected, actual, "Example2")
    
    def test_empty_list(self):
        nums = []
        actual = insertion_sort(nums)
        expected = []
        self.assertListEqual(expected, actual, "empty_list")

    def test_null_list(self):
        nums = None
        actual = insertion_sort(nums)
        expected = None
        self.assertEqual(expected, actual, "null_list")

    def test_list_size_1(self):
        nums = [10]
        actual = insertion_sort(nums)
        expected = [10]
        self.assertListEqual(expected, actual, "list_size_1")

    def test_list_size_2(self):
        nums = [1, 2]
        actual = insertion_sort(nums)
        expected = [1, 2]
        self.assertListEqual(expected, actual, "list_size_2")
    
    def test_list_size_3(self):
        nums = [3, 1, 2]
        actual = insertion_sort(nums)
        expected = [1, 2, 3]
        self.assertListEqual(expected, actual, "list_size_3")

    def test_sorted_list(self):
        nums = [1, 2, 2, 3]
        actual = insertion_sort(nums)
        expected = [1, 2, 2, 3]
        self.assertListEqual(expected, actual, "sorted_list")

    def test_negative_value_list(self):
        nums = [1, -2, 2, -3]
        actual = insertion_sort(nums)
        expected = [-3, -2, 1, 2]
        self.assertListEqual(expected, actual, "negative_value_list")

    def test_repeated_values_list(self):
        nums = [1, 1, 1, 1, 1]
        actual = insertion_sort(nums)
        expected = [1, 1, 1, 1, 1]
        self.assertListEqual(expected, actual, "repeated_values_list")

if __name__ == '__main__':
    unittest.main()
