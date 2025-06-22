"""
Given an integer array nums, find the subarray with the largest sum, and return its sum.
53. Maximum Subarray: https://leetcode.com/problems/maximum-subarray/description/

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
"""
from typing import List

def max_sum_subarray(nums: List[int]) -> int:
    """
        if max_sum[i] = maximum of all subarrays ending with i element
            then we can give
                if i < n-1, max_sum[i + 1] = max(nums[i + 1], max_sum[i + 1] + nums[i])
        
        and overall max = max(max_sum)

        TC: O(n)
        SC: O(1)
    """
    if not nums or len(nums) == 0:
        return 0
    
    max_last_sum = nums[0]
    max_sum = nums[0]

    for i in range(1, len(nums)):
        max_last_sum = max(nums[i], nums[i] + max_last_sum)
        max_sum = max(max_sum, max_last_sum)
    
    return max_sum

import unittest
class TestMaxSumSubArray(unittest.TestCase):
    TEST_CASES = [
        # Basic cases
        {"nums": [-2,1,-3,4,-1,2,1,-5,4], "expected": 6, "description": "Example 1"}
        ,{"nums": [5,4,-1,7,8], "expected": 23, "description": "Example 3"}
        
        # Edge cases
        ,{"nums": [1], "expected": 1, "description": "Example 2"}
        ,{"nums": [], "expected": 0, "description": "empty array"}
        ,{"nums": [1, -1], "expected": 1, "description": "two length array"}
        ,{"nums": [1, 1, 1], "expected": 3, "description": "three lenght duplicate elments"}

        # Boundary cases
    ]


    def test_testcases(self):
        for test_case in self.TEST_CASES:
            try:
                actual = max_sum_subarray(test_case['nums'])
                self.assertEqual(test_case['expected'], actual, f"{test_case['description']}")
            except ValueError as e:
                print(test_case['description'], e)
                raise e

if __name__ == '__main__':
    unittest.main()

