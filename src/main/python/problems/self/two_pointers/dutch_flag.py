"""
Given an array nums with n objects colored red, white, or blue, 
    sort them in-place so that objects of the same color are adjacent, 
    with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color 
    red, white, and blue, respectively.

You must solve this problem without using the library's sort function.


Example 1:

    Input: nums = [2,0,2,1,1,0]
    Output: [0,0,1,1,2,2]

Example 2:

    Input: nums = [2,0,1]
    Output: [0,1,2]
 

Constraints:
    n == nums.length
    1 <= n <= 300
    nums[i] is either 0, 1, or 2.
"""
from typing import List

def sort_colors(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.

    there are three colors, 
        we can sort first and last color 
            and the middle color gets automatically sorted

        for each iteration,
            based on color either swap with left or right parition
        
        TC: O(n)
        SC: O(1)
    """
    FIRST_COLOR = 0
    LAST_COLOR = 2

    left, right = 0, len(nums) - 1

    i = 0
    while i >= left and i <= right:
        if nums[i] == FIRST_COLOR:
            nums[i], nums[left] = nums[left], nums[i]
            left += 1
        elif nums[i] == LAST_COLOR:
            nums[i], nums[right] = nums[right], nums[i]
            right -= 1
        else:
            i += 1

        if i < left:
            i = left


import unittest
class TestDutchFlag(unittest.TestCase):
    TEST_CASES = [
        # Basic cases
        {"nums": [2,0,2,1,1,0], "expected": [0,0,1,1,2,2], "description": "Example 1"}
        ,{"nums": [2,0,1], "expected": [0, 1, 2], "description": "Example 2"}
        ,{"nums": [2, 2, 1, 1, 0, 0], "expected": [0,0,1,1,2,2], "description": "reverse order"}
        ,{"nums": [0, 0, 0], "expected": [0, 0, 0], "description": "all zeros"}
        ,{"nums": [1, 1, 1], "expected": [1, 1, 1], "description": "all ones"}
        ,{"nums": [2, 2, 2], "expected": [2, 2, 2], "description": "all twos"}
        
        # Edge cases
        ,{"nums": [], "expected": [], "description": "empty array"}

        # Boundary cases
        ,{"nums": [1], "expected": [1], "description": "only one one"}
        ,{"nums": [0], "expected": [0], "description": "only one zero"}
        ,{"nums": [2], "expected": [2], "description": "only one two"}
    ]


    def test_testcases(self):
        for test_case in self.TEST_CASES:
            try:
                sort_colors(test_case['nums'])
                self.assertEqual(test_case['expected'], test_case['nums'], f"{test_case['description']}")
            except ValueError as e:
                print(test_case['description'], e)
                raise e

if __name__ == '__main__':
    unittest.main()


