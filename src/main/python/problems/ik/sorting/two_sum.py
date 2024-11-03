# coding:: utf-8
#
# Leet Code: 1. Two Sum
#   Given an array of integers nums and an integer target, 
#       return indices of the two numbers such that they add up to target.

#   You may assume that each input would have exactly one solution, 
#       and you may not use the same element twice.
#   You can return the answer in any order.
#
# Example 1:
#   Input: nums = [2,7,11,15], target = 9
#   Output: [0,1]
#   Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
#
# Example 2:
#   Input: nums = [3,2,4], target = 6
#   Output: [1,2]
#
# Example 3:
#   Input: nums = [3,3], target = 6
#   Output: [0,1]
#
# Constraints:
#   2 <= nums.length <= 10^4
#   -10^9 <= nums[i] <= 10^9
#   -10^9 <= target <= 10^9
#   Only one valid answer exists.
#   Can you come up with an algorithm that is less than O(n^2) time complexity?

import unittest
from typing import List

def two_sum(nums : List[int], target: int) -> List[int]:
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    # Solution:
    #   Using hashmap we can check of the target-arr[i] exists
    #       key - number and value - index
    #   Time complexity: O(n)
    #   Space complexity: O(n)

    # Edge cases:
    if nums is None or len(nums) < 2:
        return []
    
    store = {}
    for i in range(len(nums)):
        other_num = target - nums[i]
        if other_num in store:
            return [store[other_num], i]
        store[nums[i]] = i
            
    return []

class Testcase(unittest.TestCase):
    def test_example1(self):
        input = [2,7,11,15]
        target = 9
        actual = two_sum(input, target)
        expected = [0, 1]
        self.assertListEqual(expected, actual, "Example1") 

    def test_example2(self):
        input = [3, 2, 4]
        target = 6
        actual = two_sum(input, target)
        expected = [1, 2]
        self.assertListEqual(expected, actual, "Example2") 

    def test_example3(self):
        input = [3, 3]
        target = 6
        actual = two_sum(input, target)
        expected = [0, 1]
        self.assertListEqual(expected, actual, "Example3") 

    def test_with_zero(self):
        input = [3, 0, 1]
        target = 3
        actual = two_sum(input, target)
        expected = [0, 1]
        self.assertListEqual(expected, actual, "with_zero") 

if __name__ == '__main__':
    unittest.main()