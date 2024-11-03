# coding:: utf-8
#
# Segregate Even And Odd Numbers
#   Given an array of numbers, rearrange them in-place so that even numbers appear before odd ones.
#
# Example 1:
#   Input: nums = [1, 2, 3, 4]
#   Output: [4, 2, 3, 1]
#   Explanation: The order within the group of even numbers does not matter; 
#       same with odd numbers. So the following are also correct outputs: 
#           [4, 2, 1, 3], [2, 4, 1, 3], [2, 4, 3, 1].
#
# Constraints:
#   1 <= nums.length <= 10^5
#   1 <= nums[i] <= 10^9
#
#
# Notes:
#   It is important to practice solving this problem by rearranging numbers in-place.
#   There is no need to preserve the original order within the even and within the odd numbers.
#   We look for a solution of the linear time complexity that uses constant auxiliary space

import unittest
from typing import List

def segregate_evens_and_odds(nums: List[int]) -> List[int]:
    """
    Args:
     nums(list_int32)
    Returns:
     list_int32
    """

    # Solution: as we navigate the array we can keep a separator for evens
    #   and keep swapping evens with advancing the separtor.
    #   similar to partition mechanism in quicksort.
    # Time complexity: O(n)
    # Space complexity: O(1)

    # edge cases
    if nums is None or len(nums) < 2:
        return nums
    
    even_end = 0
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            nums[even_end], nums[i] = nums[i], nums[even_end]
            even_end += 1

    return nums
    
class Testcase(unittest.TestCase):
    def test_example1(self):
        nums = [1, 2, 3, 4]
        actual = segregate_evens_and_odds(nums)
        expected = [2, 4, 3, 1]
        self.assertListEqual(expected, actual, "Example1")

    def test_none(self):
        nums = None
        actual = segregate_evens_and_odds(nums)
        expected = None
        self.assertEqual(expected, actual, "None")

    def test_empty(self):
        nums = []
        actual = segregate_evens_and_odds(nums)
        expected = []
        self.assertListEqual(expected, actual, "empty")

    def test_max_num(self):
        nums = [10**9, 10**6]
        actual = segregate_evens_and_odds(nums)
        expected = [10**9, 10**6]
        self.assertListEqual(expected, actual, "max_num")

    def test_len_1(self):
        nums = [2]
        actual = segregate_evens_and_odds(nums)
        expected = [2]
        self.assertListEqual(expected, actual, "len_1")

    def test_len_2(self):
        nums = [1, 2]
        actual = segregate_evens_and_odds(nums)
        expected = [2, 1]
        self.assertListEqual(expected, actual, "len_2")

    def test_len_3(self):
        nums = [2, 1, 3]
        actual = segregate_evens_and_odds(nums)
        expected = [2, 1, 3]
        self.assertListEqual(expected, actual, "len_3")

    def test_all_even(self):
        nums = [2, 4, 6]
        actual = segregate_evens_and_odds(nums)
        expected = [2, 4, 6]
        self.assertListEqual(expected, actual, "all_even")

    def test_all_odd(self):
        nums = [1, 3, 5]
        actual = segregate_evens_and_odds(nums)
        expected = [1, 3, 5]
        self.assertListEqual(expected, actual, "all_odd")

if __name__ == '__main__':
    unittest.main()