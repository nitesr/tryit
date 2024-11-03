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

def get_smallest_element_index(nums: List[int], start: int) -> int:
    # Solution:
    #   Iterate over and get smallest element index

    smallest_element_index = start

    i = start+1
    while i < len(nums):
        smallest_element = min(nums[smallest_element_index], nums[i])
        if smallest_element != nums[smallest_element_index]:
            smallest_element_index = i
        i += 1

    return smallest_element_index

def swap(nums: List[int], src_pos: int, dest_pos: int) -> List[int]:
    if src_pos == dest_pos:
        return nums
    
    nums[src_pos], nums[dest_pos] = nums[dest_pos], nums[src_pos]
    return nums

def selection_sort(nums: List[int]) -> List[int]:
    # Solution:
    #   Iterate over all the array positions and 
    #       find the smallest element on the right of the position on each iteration
    if nums is None or len(nums) <= 1:
        return nums

    n = len(nums)

    for i in range(n):
        smallest_element_index = get_smallest_element_index(nums, i)
        swap(nums, smallest_element_index, i)
        
    return nums

class Testcase(unittest.TestCase):
    def test_example1(self):
        nums = [5,2,3,1]
        actual = selection_sort(nums)
        expected = [1,2,3,5]
        self.assertListEqual(expected, actual, "Example1")
    
    def test_example2(self):
        nums = [5,1,1,2,0,0]
        actual = selection_sort(nums)
        expected = [0,0,1,1,2,5]
        self.assertListEqual(expected, actual, "Example2")
    
    def test_empty_list(self):
        nums = []
        actual = selection_sort(nums)
        expected = []
        self.assertListEqual(expected, actual, "empty_list")

    def test_null_list(self):
        nums = None
        actual = selection_sort(nums)
        expected = None
        self.assertEqual(expected, actual, "null_list")

    def test_list_size_1(self):
        nums = [10]
        actual = selection_sort(nums)
        expected = [10]
        self.assertListEqual(expected, actual, "list_size_1")

    def test_list_size_2(self):
        nums = [1, 2]
        actual = selection_sort(nums)
        expected = [1, 2]
        self.assertListEqual(expected, actual, "list_size_2")

    def test_sorted_list(self):
        nums = [1, 2, 2, 3]
        actual = selection_sort(nums)
        expected = [1, 2, 2, 3]
        self.assertListEqual(expected, actual, "sorted_list")

    def test_negative_value_list(self):
        nums = [1, -2, 2, -3]
        actual = selection_sort(nums)
        expected = [-3, -2, 1, 2]
        self.assertListEqual(expected, actual, "negative_value_list")

if __name__ == '__main__':
    unittest.main()

