# coding:: utf-8
#
# Permute Array Of Unique Integers
#   Given an array of unique numbers, return in any order all its permutations.
#
# Example 1:
#   Input: arr = [1, 2, 3]
#   Output: [ [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2] ]
#
#  Constraints:
#   1 <= len(arr) <= 9
#   0 >= arr[i] <= 99

import unittest
import random
from typing import List

def get_permutations(arr):
    """
    Args:
     arr(list_int32)
    Returns:
     list_list_int32
    """
    # Solution:
    #   recursively branch out with branches based on available elments
    #       permute_arr(available_elements, slate)
    #           for each element available do permute_arr(available_elements - element, element + slate)
    #       base condition: when no available_elements collect the slate
    #
    #   Time Complexity: O(n! . n) 
    #      there are n levels and at each level there are Prod(l) nodes 
    #        where l is level at last level there are n! nodes
    #      At last level each node does O(n) work to collect the slate
    #   Space Compelxity: O(n) callstack + O(n) string + O(n!) output
    #
    # Edge cases:
    if len(arr) == 0:
        return []
    
    permutes = []
    def permute_arr(cur_pos: int, avail_arr: List[int], slate: List[int]) -> None:
       if len(avail_arr) == cur_pos:
           permutes.append(list(slate))
           return
       
       for i in range(cur_pos, len(avail_arr)):
           slate.append(avail_arr[i])
           avail_arr[cur_pos], avail_arr[i] = avail_arr[i], avail_arr[cur_pos]
           
           permute_arr(cur_pos+1, avail_arr, slate)

           avail_arr[cur_pos], avail_arr[i] = avail_arr[i], avail_arr[cur_pos]
           slate.pop()

    permute_arr(0, arr, [])
    return permutes
    
class Testcase(unittest.TestCase):
    def test_example1(self):
        arr = [1, 2, 3]
        actual = get_permutations(arr)
        expected = [ [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2] ]
        self.assertListEqual(expected, actual, "Example1") 

    def test_zero(self):
        arr = []
        actual = get_permutations(arr)
        expected = []
        self.assertListEqual(expected, actual, "zero") 
    
    def test_one(self):
        arr = [1]
        actual = get_permutations(arr)
        expected = [ [1] ]
        self.assertListEqual(expected, actual, "one") 
        
    def test_two(self):
        arr = [1, 2]
        actual = get_permutations(arr)
        expected = [ [1, 2], [2, 1] ]
        self.assertListEqual(expected, actual, "two") 
        

if __name__ == '__main__':
    unittest.main()