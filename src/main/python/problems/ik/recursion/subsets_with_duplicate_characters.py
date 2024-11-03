# coding:: utf-8
#
# Subsets With Duplicate Characters
#   Given a string that might contain duplicate characters, find all the possible distinct subsets of that string.
#
#   All the subset strings should be individually sorted.
#   The order of the output strings does not matter.
#
# Example 1:
#   Input: s = "aab"
#   Output: ["", "a", "aa", "aab", "ab", "b"]
#
# Example 2:
#   Input: s = "ab"
#   Output: ["", "a", "ab", "b"]
#
#  Constraints:
#   1 <= length of the string <= 15
#   String consists of lowercase English letters

import unittest
import random

from typing import List
def get_distinct_subsets(s):
    """
    Args:
     s(str)
    Returns:
     list_str
    """
    # Solution:
    #     recursively iterate through each available character and branch out it being part of subset and not
    #       as duplicates are allowed, we could end up with duplicate subsets on choosing one duplicate over the other
    #       the distinction should be based on how many duplicate chars we can to include part of subset. e.g '' vs 'a' vs 'aaa'
    #           compared to '' vs 'a' vs 'b'
    #      base condition: if there are no chars to choose from we can collect the subset
    #
    #   Time Complexity: O(n*2^n)
    #   Space Compelxity: O(n) - call stack, O(n) - auxilary space, O(2^n) - output
    #
    # Edge cases:
    if s is None:
        return []
    
    if len(s) == 0:
        return [""]
    
    s_sorted = list(sorted([ s[i] for i in range(len(s)) ]))
    s_tuples = [(s_sorted[0], 1)]
    for i in range(1, len(s_sorted)):
        if s_sorted[i] != s_sorted[i-1]:
            s_tuples.append((s_sorted[i], 1))
        else:
           s_tuples[-1] = (s_sorted[i], s_tuples[-1][1]+1)
    del s_sorted

    subsets = []
    def gen_distinct_subsets_helper(ptr, subset):
        if ptr == len(s_tuples):
            subsets.append(''.join(subset))
            return

        # exclude
        gen_distinct_subsets_helper(ptr+1, subset)

        # include
        working_set = []
        for i in range(1, s_tuples[ptr][1]+1):
            working_set.append(s_tuples[ptr][0])
            subset.append(''.join(working_set))
            gen_distinct_subsets_helper(ptr+1, subset)
            subset.pop()
        

    gen_distinct_subsets_helper(0, [])
    return subsets

def get_distinct_subsets_sol1(str):
    str = sorted(str)
    result = []

    def helper(slate, n):
        result.append(''.join(slate))
        if n == len(str):
            return

        unique = set()
        for index in range(n, len(str)):
            if str[index] not in unique:
                unique.add(str[index])

                slate.append(str[index])
                helper(slate, index + 1)
                slate.pop()

    helper([], 0)
    return result

class Testcase(unittest.TestCase):
    def test_example1(self):
        s = "aab"
        actual = get_distinct_subsets_sol1(s)
        expected =  ["", "a", "ab", "aa", "aab", "b"]
        self.assertEqual(len(expected), len(actual))

    def test_example2(self):
        s = "ab"
        actual = get_distinct_subsets_sol1(s)
        expected =  ["", "a", "b", "ab"]
        self.assertEqual(len(expected), len(actual))

    def test_zero(self):
        s = ""
        actual = get_distinct_subsets_sol1(s)
        expected = [""]
        self.assertListEqual(expected, actual, "zero") 
    
    def test_one(self):
        s = "a"
        actual = get_distinct_subsets_sol1(s)
        expected = ["", "a"]
        self.assertListEqual(expected, actual, "one") 
        
        
    def test_multi_duplicate(self):
        s = "aabbbcc"
        actual = get_distinct_subsets_sol1(s)
        self.assertEqual(36 , len(actual), "multi_duplicate") 

if __name__ == '__main__':
    unittest.main()