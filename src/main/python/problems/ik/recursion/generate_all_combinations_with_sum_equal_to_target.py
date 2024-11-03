# coding:: utf-8
#
# Generate All Combinations With Sum Equal To Target
#   Given an integer array, generate all the unique combinations of the array numbers that sum up to a given target value.
#
#   Each number in the array can be used exactly once.
#   All the returned combinations must be different. Two combinations are considered different 
#      if their sorted version is different.
#   The order of combinations and the order of the numbers inside a combination does not matter.

# Example 1:
#   Input: arr = [1, 2, 3], target = 3
#   Output: [ [3], [1, 2] ]
#
# Example 2:
#   Input: arr = [1, 1, 1, 1], target = 2
#   Output: [ [1, 1] ]
#
#  Constraints:
#   1 <= len(arr) <= 25
#   1 <= arr[i] <= 100
#   1 <= target <= 2500

import unittest
import random
from typing import List

def generate_all_combinations(arr, target):
    """
    Args:
     arr(list_int32)
     target(int32)
    Returns:
     list_list_int32
    """
    # Solution:
    #   recursively iterate through each available number and branch out it being part of subset and not
    #       as duplicates are allowed, we could end up with duplicate subsets on choosing one duplicate over the other
    #       the distinction should be based on how many duplicate numbers we can to include part of subset. e.g () vs (1) vs (1,1)
    #           compared to () vs (1) vs (2), (1,2)
    #      base condition: if there are no numbers to choose from we can collect the subset with target sum
    #      contraint: we can exit from the subtree early 
    #           if current sum is exceeding the next target
    #           if remaining elments sum is less than the next target
    #           
    #
    #   Time Complexity: O(n * 2^n) -  n times is to collect the subset on last node for 2^n nodes
    #   Space Compelxity: O(n) - call stack, O(n) - auxilary, O(n * 2^n) - output
    #
    # Edge cases:
    if arr is None or len(arr) == 0:
        return []
    
    sorted_arr = sorted(arr)

    combinations = []
    def helper(ptr, combination, next_target, remaining_sum):

        # this is possible before traversing the sub-tree because
        #   there will be a path (leaf) not choosing any of the remaining elements
        #   which meets the next_target
        if next_target == 0:
            combinations.append(combination[:])
            return
        
        if ptr == len(sorted_arr):    
            return

        # this is possible only because there are no negative numbers, the sum can only increase
        if next_target < 0 or remaining_sum < next_target:
            return
        
        next_ptr = ptr
        while next_ptr < len(sorted_arr) and sorted_arr[next_ptr] == sorted_arr[ptr]: 
            remaining_sum -= sorted_arr[next_ptr]
            next_ptr += 1
            
        # exclude
        helper(next_ptr, combination, next_target, remaining_sum)

        # include
        cur_sum = 0
        for i in range(ptr, next_ptr):
            cur_sum += sorted_arr[ptr]
            combination.append(sorted_arr[ptr])
            helper(next_ptr, combination, next_target-cur_sum, remaining_sum)

        for _ in range(ptr, next_ptr):
            combination.pop()

    helper(0, [], target, sum(sorted_arr))
    return combinations

from time import time
class Testcase(unittest.TestCase):
    def test_example1(self):
        arr = [1, 2, 3]
        target = 3
        actual = generate_all_combinations(arr, target)
        expected = [ [3], [1, 2] ]
        self.assertListEqual(expected, actual, "Example1") 

    def test_zero(self):
        arr = []
        target = 0
        actual = generate_all_combinations(arr, target)
        expected = []
        self.assertListEqual(expected, actual, "zero") 
    
    def test_one(self):
        arr = [1]
        target = 1
        actual = generate_all_combinations(arr, target)
        expected = [ [1] ]
        self.assertListEqual(expected, actual, "one") 
        
    def test_two(self):
        arr = [1, 2, 1, 1]
        target = 2
        actual = generate_all_combinations(arr, target)
        expected = [ [2], [1, 1] ]
        self.assertListEqual(expected, actual, "two") 

    
    def test_scale(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
        target = 300
        t0 = time()
        generate_all_combinations(arr, target)
        t1 = time()
        print(t1-t0)

if __name__ == '__main__':
    unittest.main()