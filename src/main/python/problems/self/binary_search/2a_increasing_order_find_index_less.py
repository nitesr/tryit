"""
Given a list of increasing order of elements in an array and target
    find the index on array such that all elements to left of index 
        are less than target
"""
from typing import List

def binary_search(nums: List[int], target: int) -> int:
    # edge case
    if not nums or len(nums) == 0:
        return 0
    
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
        {"nums": [1, 2, 3, 4, 5], "target": 3, "expected": 2, "description": "exists in middle"}
        ,{"nums": [1, 2, 3, 4, 5], "target": 2, "expected": 1, "description": "exists in left half"}
        ,{"nums": [1, 2, 3, 4, 5], "target": 4, "expected": 3, "description": "exists in right half"}
        ,{"nums": [1, 4, 7, 10, 18, 19, 21], "target": 8, "expected": 3, "description": "missing element"}
        
        # Edge cases
        ,{"nums": [], "target": 5, "expected": 0, "description": "zero elements"}
        ,{"nums": [1], "target": 1, "expected": 0, "description": "one element, exits"}
        ,{"nums": [1], "target": 2, "expected": 1, "description": "one element, greater"}
        ,{"nums": [1], "target": -1, "expected": 0, "description": "one element, lesser"}
        
       
        # Boundary cases
        ,{"nums": [1, 2, 3, 4, 5], "target": 1, "expected": 0, "description": "first elment"}
        ,{"nums": [1, 2, 3, 4, 5], "target": 5, "expected": 4, "description": "last elment"}
        ,{"nums": [1, 4, 7, 10, 18, 19, 21], "target": 22, "expected": 7, "description": "missing element, next to last"}
        ,{"nums": [1, 4, 7, 10, 18, 19, 21], "target": 0, "expected": 0, "description": "missing element, previous to first"}
    ]

    def test_testcases(self):
        for test_case in self.TEST_CASES:
            actual = binary_search(test_case['nums'], test_case['target'])
            self.assertEqual(test_case['expected'], actual, f"nums={test_case['nums']} target={test_case['target']}, {test_case['description']}")

if __name__ == '__main__':
    unittest.main()