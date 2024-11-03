# coding:: utf-8
#
# How Many Binary Search Trees With N Nodes
#   Write a function that returns the number of distinct binary search trees that 
#   can be constructed with n nodes. For the purpose of this exercise, do solve the problem 
#   using recursion first even if you see some non-recursive approaches.
#
# Example 1:
#   Input: n = 1
#   Output: 1
#   Explanation: 1
#
# Example 2:
#   Input: n = 2
#   Output: 2
#   Explanation: 1 - 2 (right) and 2 - 1 (left)
#
# Example 3:
#   Input: n = 3
#   Output: 5
#
#  Constraints:
#   0 <= n <= 16

import unittest
import random
from typing import List



def how_many_bsts(n):
    """
    Args:
     n(int32)
    Returns:
     int64
    """
    # Solution:
    #   bst tree has lesser nodes on left and larger on right, recursively we
    #    can try number of left and right bsts with each available root 
    #    and multiple to get total number of bsts with the given root
    #    at end, add up for each available root.
    #   e.g. nodes -> [1, 2, 3, 4], each one can be a possible root
    #       for node 2, left [1] and right [3, 4]
    #           for left 1 node -> hits the base condition (returns 1)
    #           for right -> recursively try with roots 3 and 4 (returns 2)
    #           so number of bsts are 1 * 2 = 2 with root node as '2'.
    #       for node 1, left [] and right [2, 3, 4]
    #           for left -> no nodes so no subtrees 
    #   base condition: if n = 1, 1 bst
    #   
    #   Time Complexity: L0: n nodes, L1: n * n-1 nodes, L3: n * n-1 * n-2 nodes etc..
    #   Space Compelxity: O(n) - call stack
    #
    # Edge cases:
    if n == 0:
        return 0
    
    def helper(num_nodes) -> int:
        if num_nodes == 1:
            return 1
        
        total = 0
        for i in range(1, num_nodes+1):
            left = helper(i-1) if i > 1 else 1
            right = helper(num_nodes-i) if num_nodes > i else 1
            total += left * right
        return total

    return helper(n)
    
class Testcase(unittest.TestCase):
    def test_example1(self):
        n = 1
        actual = how_many_bsts(n)
        expected = 1
        self.assertEqual(expected, actual, "Example1") 

    def test_example2(self):
        n = 2
        actual = how_many_bsts(n)
        expected = 2
        self.assertEqual(expected, actual, "Example2") 

    def test_example3(self):
        n = 3
        actual = how_many_bsts(n)
        expected = 5
        self.assertEqual(expected, actual, "Example3") 

    def test_zero(self):
        n = 0
        actual = how_many_bsts(n)
        expected = 0
        self.assertEqual(expected, actual, "zero") 
        
if __name__ == '__main__':
    unittest.main()