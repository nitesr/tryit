# coding:: utf-8
#
# N Queen Problem
#   Given an integer n, find all possible ways to position n queens on an n×n chessboard 
#       so that no two queens attack each other. A queen in chess can move horizontally, vertically, or diagonally.
#
#   Do solve the problem using recursion first even if you see some non-recursive approaches.
#   The function must return a two-dimensional array of strings representing the arrangements. 
#       Size of the array must be m×n where m is the number of distinct arrangements.
#       Each string must be n characters long, and the strings' characters may be 
#       either q (for a queen) or - (for an empty position on the chessboard). 
#   Valid arrangements may appear in the output in any order.
#
# Example 1:
#   Input: n = 4
#   Output: [ 
#               ["--q-", "q---", "---q", "-q--"],
#               ["-q--", "---q", "q---", "--q-"] 
#           ]
#   Explanation: There are two distinct ways four queens can be positioned on a 4×4 chessboard without attacking each other. 
#       The positions may appear in the output in any order. 
#       So the same two positions in different order would be another correct output.
#
# Example 2:
#   Input: n = 2
#   Output: []
#   Explanation: No way to position two queens on a 2×2 chessboard without them attacking each other - so empty array.
#
#  Constraints:
#   1 <= n <= 12

import unittest
import random

from typing import List
def find_all_arrangements(n):
    """
    Args:
     n(int32)
    Returns:
     list_list_str
    """
    # Solution:
    #  recursively try the queen in each cell row by row (or col by col) as only one queen is possible
    #       per row. As we try we need to ensure the queen is not crossing path with previous queens 
    #       by column or diagonal rule. The row rule is taken care before selecting the cell.
    #
    #   the rule check takes O(n^2) time in naive approach of checking each cell, instead we can maintain
    #       a set of columns and diagonals used.  For diagonal rule, (row-col) and (row+col) gives 
    #       the diagonals / and \. e.g. in 4x4 if queen is placed in 1x2 the diagonals are 
    #       1 (1-2, 0-1, 2-3) and 3 (1+2, 0+3, 2+1)
    #
    #
    #   base condition: past the last row
    #   constraints: backtrace on violating the rules
    #
    #   Time Complexity: O(n^n+1)
    #   Space Compelxity: O(n) - call stack, O(n^2) - auxilary, O(n^n) - output
    #
    # Edge cases:
    if n < 1:
        return []
    
    working_col_set = set()
    working_backslash_set = set()
    working_fwdslash_set = set()

    arrangements = []
    def helper(row, arrangement):
        
        if row == n:
            arrangements.append(list(arrangement))
            return
        
        for col in range(n):
            diag_backslash = row-col
            diag_fwdslash = row+col
            # print(row, col, working_col_set, working_backslash_set, working_fwdslash_set, arrangement)
            if not col in working_col_set \
                and not diag_backslash in working_backslash_set \
                and not diag_fwdslash in working_fwdslash_set:

                # valid to place queen in row,col
                working_col_set.add(col)
                working_backslash_set.add(diag_backslash)
                working_fwdslash_set.add(diag_fwdslash)

                arrangement.append(''.join([ *['-']*col, 'q', *['-']*(n-col-1) ]))
                helper(row+1, arrangement)
                arrangement.pop()

                working_col_set.remove(col)
                working_backslash_set.remove(diag_backslash)
                working_fwdslash_set.remove(diag_fwdslash)

    helper(0, [])
    return arrangements
    
class Testcase(unittest.TestCase):
    def test_example1(self):
        n = 4
        actual = find_all_arrangements(n)
        expected = [ ["-q--", "---q", "q---", "--q-"], ["--q-", "q---", "---q", "-q--"],  ]
        self.assertListEqual(expected, actual, "Example1") 

    def test_example2(self):
        n = 2
        actual = find_all_arrangements(n)
        expected = [ ]
        self.assertListEqual(expected, actual, "Example2") 
    
    def test_one(self):
        n = 1
        actual = find_all_arrangements(n)
        expected = [['q']]
        self.assertListEqual(expected, actual, "one") 
        

if __name__ == '__main__':
    unittest.main()