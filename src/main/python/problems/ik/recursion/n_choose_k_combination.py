# coding:: utf-8
#
# N Choose K Combinations
#   Given two integers n and k, find all the possible unique combinations of k numbers in range 1 to n.
#   The answer can be returned in any order.
# Example 1:
#   Input: n = 5, k = 2
#   Output: [ [1, 2], [1, 3], [1, 4], [1, 5], [2, 3], [2, 4], [2, 5], [3, 4], [3, 5], [4, 5] ]
# 
# Example 2:
#   Input: n = 6, k = 6
#   Output: [ [1, 2, 3, 4, 5, 6] ]
# 
#  Constraints:
#   1 <= n <= 20
#   1 <= k <= n

import unittest
import random
from typing import List

def find_combinations(n, k):
    """
    Args:
     n(int32)
     k(int32)
    Returns:
     list_list_int32
    """
    # Solution:
    #   c(n, k) = c(n, n-k)
    #   c(n, k) = c(n-1, k-1) + c(n-1, k) i.e. sum of combinations with kth element and without kth element
    #   Time Complexity: O(2^n)
    #   Space Complexity: O(n)
    #
    # Edge cases:
    if k > n:
        return []
    
    combinations = []
    def choose(cur: int, combination: List[int]) -> None:
        if len(combination) == k:
            combinations.append(list(combination))
            return
        
        if cur == n+1:
            return
        
        combination.append(cur)
        choose(cur+1, combination)
        combination.remove(cur)

        choose(cur+1, combination)

    choose(1, [])
    return combinations
    
class Testcase(unittest.TestCase):
    def test_example1(self):
        n = 5
        k = 2
        actual = find_combinations(n, k)
        expected = [ [1, 2], [1, 3], [1, 4], [1, 5], [2, 3], [2, 4], [2, 5], [3, 4], [3, 5], [4, 5] ]
        self.assertListEqual(expected, actual, "Example1") 

    def test_example2(self):
        n = 6
        k = 6
        actual = find_combinations(n, k)
        expected = [ [1, 2, 3, 4, 5, 6] ]
        self.assertListEqual(expected, actual, "Example2") 

    def test_one(self):
        n = 1
        k = 1
        actual = find_combinations(n, k)
        expected = [ [1] ]
        self.assertListEqual(expected, actual, "one") 
    
    def test_zero(self):
        n = 100
        k = 0
        actual = find_combinations(n, k)
        expected = [ [] ]
        self.assertListEqual(expected, actual, "zero") 

if __name__ == '__main__':
    unittest.main()