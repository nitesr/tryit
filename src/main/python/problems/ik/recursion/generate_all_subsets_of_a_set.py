# coding:: utf-8
#
# Generate All Subsets Of A Set
#   Generate ALL possible subsets of a given set. 
#   The set is given in the form of a string s containing distinct lowercase characters 'a' - 'z'.
#
#   Any set is a subset of itself.
#   Empty set is a subset of any set.
#   Output contains ALL possible subsets of given string.
#   Order of strings in the output does not matter. E.g. s = "a", arrays ["", "a"] and ["a", ""] both will be accepted.
#   Order of characters in any subset must be same as in the input string. 
#       For s = "xy", array ["", "x", "y", "xy"] will be accepted, but ["", "x", "y", "yx"] will not be accepted.
# Example 1:
#   Input: s = "xy"
#   Output: ["", "x", "y", "xy"]
#
#  Constraints:
#   0 <= length of s <= 19
#   s only contains distinct lowercase English letters.

import unittest
import random
from typing import List


def generate_all_subsets(s):
    """
    Args:
     s(str)
    Returns:
     list_str
    """
    # Solution:
    #   decrease and conquer: recursively add additional character to all the subsets before to get all subsets
    #       for each character - choose to be part of set or not part of set.
    #           and recursively try it
    #
    #   Time Complexity: 2 branches on each node till n levels T(n * 2^n) additional n to copy the subset.
    #   Space Compelxity: O(n) for call stack + O(n) for maintaining set + O(2^n) for output
    #
    # Edge cases:
    if s is None:
        return []
    
    subsets = []
    def collect_subsets(cur_pos, subset: List[str]) -> None:
        if cur_pos == len(s):
            subsets.append(''.join(subset))
            return
        
        collect_subsets(cur_pos+1, subset)

        subset.append(s[cur_pos])
        collect_subsets(cur_pos+1, subset)
        subset.pop()

    collect_subsets(0, [])
    return subsets
    
class Testcase(unittest.TestCase):
    def test_example1(self):
        s = "xy"
        actual = generate_all_subsets(s)
        expected = ["", "y", "x", "xy"]
        self.assertListEqual(expected, actual, "Example1") 

    def test_zero(self):
        s = ""
        actual = generate_all_subsets(s)
        expected = [""]
        self.assertListEqual(expected, actual, "zero") 
    
    def test_one(self):
        s = "x"
        actual = generate_all_subsets(s)
        expected = [ "", "x" ]
        self.assertListEqual(expected, actual, "one") 
        

if __name__ == '__main__':
    unittest.main()