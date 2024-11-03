# coding:: utf-8
#
# Permute Array Of Integers Duplicates Allowed
#   Given an array of numbers with possible duplicates, return all of its permutations in any order.
#
# Example 1:
#   Input: arr = [1, 2, 2]
#   Output: [ [1, 2, 2], [2, 1, 2], [2, 2, 1] ]
#
#  Constraints:
#   1 <= len(arr) <= 9
#   0 >= arr[i] <= 9

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
    #   recursively fill the blank with unique integers
    #   base condition:  ptr == len(s) then collect the permute
    #
    #   Time Complexity: O(n! * n)
    #   Space Compelxity: O(n) - call stack + O(n) for working list + O(n!) - for output
    #
    # Edge cases:
    if len(arr) == 0:
        return []
    
    permutes = []
    def permute_arr(cur_pos: int, avail_arr: List[int], slate) -> None:
       if len(avail_arr) == cur_pos:
           permutes.append(list(slate))
           return
       
       uniq_values = set()
       for i in range(cur_pos, len(avail_arr)):
           if avail_arr[i] in uniq_values:
               continue
           else:
               uniq_values.add(avail_arr[i])

           slate.append(avail_arr[i])
           avail_arr[cur_pos], avail_arr[i] = avail_arr[i], avail_arr[cur_pos]
           
           permute_arr(cur_pos+1, avail_arr, slate)

           avail_arr[cur_pos], avail_arr[i] = avail_arr[i], avail_arr[cur_pos]
           slate.pop()

    arr.sort()
    permute_arr(0, arr, [])
    return permutes
    
class Testcase(unittest.TestCase):
    def test_example1(self):
        arr = [1, 2, 2]
        actual = get_permutations(arr)
        expected =  [ [1, 2, 2], [2, 1, 2], [2, 2, 1] ]
        self.assertListEqual(expected, actual, "Example1")
        self.assertEqual(3, len(actual))

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
        arr = [1, 1]
        actual = get_permutations(arr)
        expected = [ [1, 1] ]
        self.assertListEqual(expected, actual, "two") 
        
        
    def test_multi_duplicate(self):
        arr = [3, 3, 8, 8, 8, 9, 9]
        actual = get_permutations(arr)
        self.assertEqual(7 * 6 * 5 , len(actual), "multi_duplicate") 
        

if __name__ == '__main__':
    unittest.main()