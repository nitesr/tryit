"""
Given an array of integers nums and an integer target, 
    return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, 
    and you may not use the same element twice.

You can return the answer in any order.

Example 1:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
    Input: nums = [3,2,4], target = 6
    Output: [1,2]

Example 3:
    Input: nums = [3,3], target = 6
    Output: [0,1]
 

Constraints:
    2 <= nums.length <= 10^4
    -10^9 <= nums[i] <= 10^9
    -10^9 <= target <= 10^9
    Only one valid answer exists.
"""
from typing import List

def using_map(nums: List[int], target: int) -> List[int]:
    """
        use map to track the visited numbers
        if target - nums[i] in map then return i and found index

        TC: O(n)
        SC: O(n)
    """
    map = {}
    for i in range(len(nums)):
        other_num = target - nums[i]
        if other_num in map:
            return [map[other_num], i]
        else:
            map[nums[i]] = i
    
    return []
    
def using_sort(self, nums: List[int], target: int) -> List[int]:
    """
        sort the array
        for each index try to find the target - nums[index] in rest of the array
        as the array is sorted, we can use binary search

        TC: O(nlogn)
        SC: O(n)
    """
    sorted_nums = [(nums[i], i) for i in range(len(nums))]
    sorted_nums.sort()

    def search(start, end, num):
        l, r = start, end

        while l <= r:
            m = l + (r - l) // 2
            if sorted_nums[m][0] < num:
                l = m + 1
            else:
                r = m - 1

        return l

    left = 0
    end = len(sorted_nums) - 1
    while left < end:
        end = search(left + 1, end, target - sorted_nums[left][0])
        end = min(end, len(nums) - 1)

        if end < len(nums) and sorted_nums[end][0] == target - sorted_nums[left][0]:
            return list(sorted([sorted_nums[left][1], sorted_nums[end][1]]))

        left += 1

    return []

def using_twoptr(self, nums: List[int], target: int) -> List[int]:
    """
        sort the array
        use two pointers to search of sum equals to target

        min_sum = nums[0] + nums[1]
        max_sum = nums[-2] + nums[-1]

        min_sum <= target <= max_sum
        we can start left, right from both the extremes of array
            if we move left ptr the sum will increase
            if we move right ptr the sum will decrease
            using the above logic we move ptrs to find the target sum

        TC: O(nlogn)
        SC: O(n)
    """
    sorted_nums = [(nums[i], i) for i in range(len(nums))]
    sorted_nums.sort()

    left, right = 0, len(nums) - 1

    while left < right:
        twosum = sorted_nums[left][0] + sorted_nums[right][0]
        if twosum == target:
            return list(sorted([sorted_nums[left][1], sorted_nums[right][1]]))
        elif twosum < target:
            left += 1
        else:
            right -= 1

    return []

def two_sum(nums: List[int], target: int) -> List[int]:
    return using_map(nums, target)
    # return self.using_sort(nums, target)
    # return self.using_twoptr(nums, target)

import unittest
class TestDutchFlag(unittest.TestCase):
    TEST_CASES = [
        # Basic cases
        {"nums": [1, 4, 3, 0, -1, -8], "target": -8, "expected": [3, 5], "description": "sum with 0"}
        ,{"nums": [2, 0, 3, 0, -1, -8], "target": 0, "expected": [1, 3], "description": "0 sum with 0"}
        ,{"nums": [2, 0, 3, 0, -1, -8], "target": -6, "expected": [0, 5], "description": "negative target"}
        ,{"nums": [2, 0, 3, 0, -1, -8], "target": -5, "expected": [2,5], "description": "negative target 2"}
        
        # Edge cases
        ,{"nums": [], "target": 0, "expected": [], "description": "empty array"}

        # Boundary cases
        ,{"nums": [2,7,11,15], "target": 9, "expected": [0, 1], "description": "Example 1"}
        ,{"nums": [3,2,4], "target": 6, "expected": [1, 2], "description": "Example 2"}
        ,{"nums": [3,3], "target": 6, "expected": [0, 1], "description": "Example 3"}
        
    ]


    def test_testcases(self):
        for test_case in self.TEST_CASES:
            try:
                actual = two_sum(test_case['nums'], test_case['target'])
                self.assertEqual(test_case['expected'], actual, f"{test_case['description']}")
            except ValueError as e:
                print(test_case['description'], e)
                raise e

if __name__ == '__main__':
    unittest.main()
