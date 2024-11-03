# coding:: utf-8
#
# Two Sum II
#   Given an array of integers nums and an integer target, 
#       return all combinations of the two numbers such that they add up to target.
#   Note:
#       Solution set must not contain duplicate couples.
#       You may not use the same element twice.
#       You can return the answer in any order.
#       The order of the output and the order of the couple does not matter
#
# Example 1:
#   Input: nums = [2,7,11,15], target = 9
#   Output: [[2,7]] or [[7,2]]
#   Explanation: Because 2 + 7 == 9 and its the only combination, we return [[2,7]].
#
# Example 2:
#   Input: nums = [1,2,1,1,0], target = 2
#   Output: [[1,1],[2,0]] or [[1,1],[0,2]] or [[0,2],[1,1]] or [[2,0],[1,1]]
#   Explanation: We have four sets of couples with sum = 2. ([1,1], [1,1], [1,1], [2,0])
#       out of which unique couples are [1,1] and [2,0]
#
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

    # Edge cases:
    if nums is None or len(nums) < 2:
        return []
    
    store = {}
    sol = []
    for i in range(len(nums)):
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

class Testcase(unittest.TestCase):
    def test_example1(self):
        input = [2,7,11,15]
        target = 9
        actual = two_sum(input, target)
        expected = [[2, 7]]
        self.assertListEqual(expected, actual, "Example1") 

    def test_example2(self):
        input = [1, 2, 1, 1, 0]
        target = 2
        actual = two_sum(input, target)
        expected = [[1, 1],[2, 0]]
        self.assertListEqual(expected, actual, "Example2") 

    def test_with_zero(self):
        input = [3, 0, 1]
        target = 3
        actual = two_sum(input, target)
        expected = [[3, 0]]
        self.assertListEqual(expected, actual, "with_zero")
    
    def test_duplicate_couples(self):
        input = [1, 2, 2, 1, 1, 3, 0]
        target = 3
        actual = two_sum(input, target)
        expected = [[1, 2],[3, 0]]
        self.assertListEqual(expected, actual, "duplicate_couples") 


if __name__ == '__main__':
    unittest.main()