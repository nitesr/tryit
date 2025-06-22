"""
Given an integer array nums and an integer k, 
    return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, 
    not the kth distinct element.

Example 1:
    Input: nums = [3,2,1,5,6,4], k = 2
    Output: 5  [6] [5] [3, 2, 1]

Example 2:
    Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
    Output: 4 [5, 5, 6] [4] [3, 2, 3, 1, 2]
 

Constraints:
    1 <= k <= nums.length <= 10^5
    -10^4 <= nums[i] <= 10^4
"""
from typing import List
import random
from heapq import heappush, heappop, heapify

def using_heap(nums: List[int], k: int) -> int:
    """
    maintain a min heap with k largest elements
    the top of the heap at the end of array is kth largest

    for num in nums: 
        if num > heap_peak then pop peak and push to heap
    heap_peak is the kth largest
    """
    if k == 1:
        return max(nums)

    if k == len(nums):
        return min(nums)

    min_heap = [nums[i] for i in range(k)]
    heapify(min_heap)

    for i in range(k, len(nums)):
        if nums[i] > min_heap[0]:
            heappop(min_heap)
            heappush(min_heap, nums[i])

    return min_heap[0]

def using_enhanced_quickselect(nums: List[int], k: int) -> int:
    """
    partition array into three parts i.e [less] [equal] [greater]
    equal[i] is len(greatest) + 1 largest element

    if k (from left) can fall in greater or less range, 
        k is in less then scope the search to less array
        else scope the search to greater array
    """
    def threepart_quick_select(pvt_idx, start, end):
        nums[start], nums[pvt_idx] = nums[pvt_idx], nums[start]

        p, e = start, start
        for i in range(start + 1, end + 1):
            if nums[i] == nums[start]:
                e += 1
                nums[i], nums[e] = nums[e], nums[i]
            elif nums[i] < nums[start]:
                e += 1
                nums[e], nums[i] = nums[i], nums[e]
                p += 1
                nums[p], nums[e] = nums[e], nums[p]

        nums[p], nums[start] = nums[start], nums[p]
        return (p, e)

    start, end = 0, len(nums) - 1

    while start <= end:
        pvt_idx = random.randint(start, end)
        p = threepart_quick_select(pvt_idx, start, end)
        g = (len(nums) - p[0], len(nums) - p[1])

        if k >= g[1] and k <= g[0]:
            return nums[p[0]]
        elif k > g[0]:  # left of partition
            start, end = start, p[0] - 1
        else:  # right of partition
            start, end = p[1] + 1, end


def using_quickselect(nums: List[int], k: int) -> int:
    def quick_select(pvt_idx, start, end):
        nums[start], nums[pvt_idx] = nums[pvt_idx], nums[start]

        par = start
        for i in range(start + 1, end + 1):
            if nums[i] <= nums[start]:
                par += 1
                nums[par], nums[i] = nums[i], nums[par]

        nums[start], nums[par] = nums[par], nums[start]
        return par

    start, end = 0, len(nums) - 1

    while start <= end:
        pvt_idx = random.randint(start, end)
        par = quick_select(pvt_idx, start, end)
        g = len(nums) - par
        if g == k:
            return nums[par]
        elif g > k:
            start, end = par + 1, end
        else:
            start, end = start, par - 1

def find_kth_largest(nums: List[int], k: int) -> int:
    # return using_heap(nums, k)
    # return using_quickselect(nums, k)
    return using_enhanced_quickselect(nums, k)

import unittest
class TestFindKthLargest(unittest.TestCase):
    TEST_CASES = [
        # Basic cases
        {"nums": [3,2,1,5,6,4], "k": 2, "expected": 5, "description": "Example 1"}
        ,{"nums": [3,2,3,1,2,4,5,5,6], "k": 4, "expected": 4, "description": "Example 2"}
        ,{"nums": [5,2,4,1,3,6,0], "k": 4, "expected": 3, "description": "Example 3"}
        ,{"nums": [3,2,3,1,2,4,5,5,6], "k": 3, "expected": 5, "description": "in equal part"}


        # Edge cases
        ,{"nums": [1], "k": 1, "expected": 1, "description": "single element"}
        ,{"nums": [1, 1, 1, 1, 1, 1, 1], "k": 3, "expected": 1, "description": "all same elements"}

        # Boundary cases
        ,{"nums": [2,1], "k": 1, "expected": 2, "description": "right most"}
        ,{"nums": [2,1], "k": 2, "expected": 1, "description": "left most"}
        
    ]


    def test_testcases(self):
        for test_case in self.TEST_CASES:
            try:
                actual = find_kth_largest(test_case['nums'], test_case['k'])
                self.assertEqual(test_case['expected'], actual, f"{test_case['description']}")
            except ValueError as e:
                print(test_case['description'], e)
                raise e

if __name__ == '__main__':
    unittest.main()

