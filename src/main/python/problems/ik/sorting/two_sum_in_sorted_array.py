# coding:: utf-8
#
# 2 Sum In A Sorted Array
#   Given an array sorted in non-decreasing order and a target number, 
#       find the indices of the two values from the array that sum up to the given target number.
#
#   In case when no answer exists, return an array of size two with both values equal to -1, i.e., [-1, -1]
#   In case when multiple answers exist, you may return any of them.
#   The order of the indices returned does not matter.
#   A single index cannot be used twice.
#
# Example 1:
#   Input: nums = [1, 2, 3, 5, 10], target = 7
#   Output: [1, 3]
#   Explanation: Sum of the elements at index 1 and 3 is 7.
#
# Constraints:
#   2 <= nums.length <= 10^5
#   -10^5 <= nums[i] <= 10^5
#   -10^5 <= target <= 10^5
#   Array can contain duplicate elements.

import unittest
from typing import List

def pair_sum_sorted_array(nums, target):
    """
    Args:
     numbers(list_int32)
     target(int32)
    Returns:
     list_int32
    """
    # Solution:
    #   with a sorted array, we can use two pointer from each side
    #       to compute the sum, compare and traverse accordingly.
    #       if sum > target make the sum lower by decreasing one of pair (right pointer)
    #       if sum < target make the sum higher by increaseing one of pair (left pointer)
    #   Time complexity: o(n)
    #   Space complexity: O(1)

    # Edge cases:
    if nums is None or len(nums) < 2:
        return []
    
    lo = 0
    hi = len(nums)-1

    while lo < hi:
        new_sum = nums[lo] + nums[hi]
        if new_sum > target:
            hi -= 1
        elif new_sum < target:
            lo += 1
        else:
            return [lo, hi]
            
    return [-1, -1]

class Testcase(unittest.TestCase):
    def test_example1(self):
        input = [2,7,11,15]
        target = 9
        actual = pair_sum_sorted_array(input, target)
        expected = [0, 1]
        self.assertListEqual(expected, actual, "Example1") 

    def test_example2(self):
        input = [2, 3, 4]
        target = 6
        actual = pair_sum_sorted_array(input, target)
        expected = [0, 2]
        self.assertListEqual(expected, actual, "Example2") 

    def test_example3(self):
        input = [3, 3]
        target = 6
        actual = pair_sum_sorted_array(input, target)
        expected = [0, 1]
        self.assertListEqual(expected, actual, "Example3") 

    def test_with_zero(self):
        input = [0, 1, 3]
        target = 3
        actual = pair_sum_sorted_array(input, target)
        expected = [0, 2]
        self.assertListEqual(expected, actual, "with_zero") 

if __name__ == '__main__':
    unittest.main()