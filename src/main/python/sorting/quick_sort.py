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

def pivot(nums: List[int], start: int, end: int) -> int:
    return start

def partition(nums: List[int], start: int, end: int, pvt: int) -> int:

    # swap the pvt element to start
    nums[start], nums[pvt] = nums[pvt], nums[start]
    pvt = start

    ins_pos = start + 1

    for i in range(start+1, end):
        if nums[i] <= nums[pvt]:
            nums[i], nums[ins_pos] = nums[ins_pos], nums[i]
            ins_pos += 1
    
    nums[ins_pos-1], nums[pvt] = nums[pvt], nums[ins_pos-1]
    return ins_pos-1

def quick_sort(nums: List[int]) -> List[int]:
    # Solution:
    #   find a pivot and partition the array such that the pivot element is in its location
    #       (i.e. all elements <= pivot are left of pivot and > are right)
    #   recursively do the same operation on left partition and right partition
    #   till the array is sorted.

    if nums is None or len(nums) <= 1:
        return nums
    
    def quick_sort_internal(nums: List[int], start: int, end: int) -> None:
        # if not more than 1 element
        if end - start <= 1:
            return
        
        pvt = pivot(nums, start, end)
        par = partition(nums, start, end, pvt)

        # sort left of partition
        quick_sort_internal(nums, start, par)
        
        # sort right of partition
        quick_sort_internal(nums, par+1, end)

        return nums
    
    return quick_sort_internal(nums, 0, len(nums))


class Testcase(unittest.TestCase):
    def test_example1(self):
        nums = [5,2,3,1]
        actual = quick_sort(nums)
        expected = [1,2,3,5]
        self.assertListEqual(expected, actual, "Example1")
    
    def test_example2(self):
        nums = [5,1,1,2,0,0]
        actual = quick_sort(nums)
        expected = [0,0,1,1,2,5]
        self.assertListEqual(expected, actual, "Example2")
    
    def test_empty_list(self):
        nums = []
        actual = quick_sort(nums)
        expected = []
        self.assertListEqual(expected, actual, "empty_list")

    def test_null_list(self):
        nums = None
        actual = quick_sort(nums)
        expected = None
        self.assertEqual(expected, actual, "null_list")

    def test_list_size_1(self):
        nums = [10]
        actual = quick_sort(nums)
        expected = [10]
        self.assertListEqual(expected, actual, "list_size_1")

    def test_list_size_2_sorted(self):
        nums = [1, 2]
        actual = quick_sort(nums)
        expected = [1, 2]
        self.assertListEqual(expected, actual, "list_size_2_sorted")
    
    def test_list_size_2(self):
        nums = [2, 1]
        actual = quick_sort(nums)
        expected = [1, 2]
        self.assertListEqual(expected, actual, "list_size_2")

    def test_list_size_3(self):
        nums = [3, 1, 2]
        actual = quick_sort(nums)
        expected = [1, 2, 3]
        self.assertListEqual(expected, actual, "list_size_3")

    def test_sorted_list(self):
        nums = [1, 2, 2, 3]
        actual = quick_sort(nums)
        expected = [1, 2, 2, 3]
        self.assertListEqual(expected, actual, "sorted_list")

    def test_negative_value_list(self):
        nums = [1, -2, 2, -3]
        actual = quick_sort(nums)
        expected = [-3, -2, 1, 2]
        self.assertListEqual(expected, actual, "negative_value_list")

    def test_repeated_values_list(self):
        nums = [1, 1, 1, 1, 1]
        actual = quick_sort(nums)
        expected = [1, 1, 1, 1, 1]
        self.assertListEqual(expected, actual, "repeated_values_list")

if __name__ == '__main__':
    unittest.main()
