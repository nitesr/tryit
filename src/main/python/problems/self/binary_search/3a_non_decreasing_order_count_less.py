"""
Given a list of non-decreasing order of elements in an array and target
    find number of elements that are less than target
"""
from typing import List

def binary_search(nums: List[int], target: int) -> int:
    # edge case
    if not nums or len(nums) == 0:
        return 0
    
    if target < nums[0]:
        return 0
    
    if target > nums[-1]:
        return len(nums)
    
    left, right = 0, len(nums)-1
    while left <= right:
        mid = left + (right - left) // 2
        if target > nums[mid]:
            left = mid + 1
        else:
            right = mid - 1
    
    return left

import unittest
class Testcase(unittest.TestCase):
    TEST_CASES = [
        # Basic cases
        {"nums": [1, 2, 2, 3, 3, 4, 5], "target": 3, "expected": 3, "description": "exists in middle"}
        ,{"nums": [1, 2, 3, 4, 5], "target": 2, "expected": 1, "description": "exists in left half"}
        ,{"nums": [1, 2, 3, 3, 4, 5], "target": 4, "expected": 4, "description": "exists in right half"}
        ,{"nums": [1, 1, 4, 4, 7, 7, 18, 19, 21], "target": 8, "expected": 6, "description": "missing element"}
        
        # Edge cases
        ,{"nums": [], "target": 5, "expected": 0, "description": "zero elements"}
        ,{"nums": [1], "target": 1, "expected": 0, "description": "one element, exits"}
        ,{"nums": [1], "target": 2, "expected": 1, "description": "one element, greater"}
        ,{"nums": [1], "target": -1, "expected": 0, "description": "one element, lesser"}
        ,{"nums": [2, 2, 2, 2, 2, 2], "target": 3, "expected": 6, "description": "all same elements, greater"}
        ,{"nums": [2, 2, 2, 2, 2, 2], "target": 1, "expected": 0, "description": "all same elements, lesser"}
        
       
        # Boundary cases
        ,{"nums": [1, 1, 1, 2, 3, 4, 5, 5, 5, 5], "target": 1, "expected": 0, "description": "first elment"}
        ,{"nums": [1, 1, 1, 2, 3, 4, 5, 5, 5, 5], "target": 5, "expected": 6, "description": "last elment"}
        ,{"nums": [1, 1, 4, 4, 7, 7, 18, 19, 21, 21], "target": 22, "expected": 10, "description": "missing element, next to last"}
        ,{"nums": [1, 1, 4, 4, 7, 7, 18, 19, 21, 21], "target": 0, "expected": 0, "description": "missing element, previous to first"}
    ]

    def test_testcases(self):
        for test_case in self.TEST_CASES:
            actual = binary_search(test_case['nums'], test_case['target'])
            self.assertEqual(test_case['expected'], actual, f"nums={test_case['nums']} target={test_case['target']}, {test_case['description']}")

if __name__ == '__main__':
    unittest.main()