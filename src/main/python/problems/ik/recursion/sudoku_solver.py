# coding:: utf-8
#
# Sudoku Solver
#   Given a partially filled two-dimensional array, fill all the unfilled cells such that 
#   each row, each column and each 3 x 3 subgrid 
#   (as highlighted below by bolder lines) has every digit from 1 to 9 exactly once.
#   Unfilled cells have a value of 0 on the given board.
#
#   You can assume that any given puzzle will have exactly one solution.
# Example 1:
#   Input: 9x9 board
#   Output: 9x9 solved board
#
#  Constraints:
#   Size of the input array is exactly 9 x 9
#   0 <= value in the input array <= 9

import unittest
import random

from typing import List
def solve_sudoku_puzzle(board):
    """
    Args:
     board(list_list_int32)
    Returns:
     list_list_int32
    """
     # Solution:
    #   try 1-9 on each empty cell recursively 
    #    if there are no options then backtrack and try next number
    #.  base condition if row == n, add solution
    #
    # Time complexity: 10^(n*n)
    # Space complexity: O(n*n)
    #
    # Edge case:
    if board is None or len(board) % 3 != 0 or len(board[0]) % 3 != 0:
        return board
    n = len(board)
    solution = [ [False] * n for r in range(n)]
    row_memo =  [ [False] * n for _ in range(n) ]
    col_memo =  [ [False] * n for _ in range(n) ]
    grid_memo =  [ [False] * n for _ in range((n * n // 9)) ]
    
    def compute_grid_idx(row, col):
        return (row // 3) * (n // 3) +  (col // 3)
    
    def add_entry(row, col, val):
        row_memo[row][val-1] = True
        col_memo[col][val-1] = True
        grid_idx = compute_grid_idx(row, col)
        grid_memo[grid_idx][val-1] = True
        
    def pop_entry(row, col, val):
        row_memo[row][val-1] = False
        col_memo[col][val-1] = False
        grid_idx = compute_grid_idx(row, col)
        grid_memo[grid_idx][val-1] = False
        
    def is_valid(row, col, val) -> bool:
        grid_idx = compute_grid_idx(row, col)
        
        return not row_memo[row][val-1] \
            and not  col_memo[col][val-1] \
            and not grid_memo[grid_idx][val-1]
    
    def solve_helper(row, col) -> bool:
        if row == n  and col == 0:
            return True
        elif row ==  n:
            return False
        
        new_col = 0 if col+1 == n else col+1
        new_row = row+1 if col+1 == n else row
        if board[row][col] != 0:
            solution[row][col] = board[row][col]
            return solve_helper(new_row, new_col)
        
        for i in range(1, 10):
            if is_valid(row, col, i):
                solution[row][col] = i
                add_entry(row, col, i)
                if solve_helper(new_row, new_col):
                    return True
                pop_entry(row, col, i)
                
        return False
    
    for r in range(n):
        for c in range(n):
            if board[r][c] != 0:
                add_entry(r, c, board[r][c])
    solve_helper(0, 0)
    
    return solution
    
class Testcase(unittest.TestCase):
    def test_example1(self):
        board = [
                    [8, 4, 9, 0, 0, 3, 5, 7, 0],
                    [0, 1, 0, 0, 0, 0, 0, 0, 0],
                    [7, 0, 0, 0, 9, 0, 0, 8, 3],
                    [0, 0, 0, 9, 4, 6, 7, 0, 0],
                    [0, 8, 0, 0, 5, 0, 0, 4, 0],
                    [0, 0, 6, 8, 7, 2, 0, 0, 0],
                    [5, 7, 0, 0, 1, 0, 0, 0, 4],
                    [0, 0, 0, 0, 0, 0, 0, 1, 0],
                    [0, 2, 1, 7, 0, 0, 8, 6, 5]
                ]
        actual = solve_sudoku_puzzle(board)
        expected = [
                    [8, 4, 9, 1, 6, 3, 5, 7, 2],
                    [3, 1, 5, 2, 8, 7, 4, 9, 6],
                    [7, 6, 2, 4, 9, 5, 1, 8, 3],
                    [1, 5, 3, 9, 4, 6, 7, 2, 8],
                    [2, 8, 7, 3, 5, 1, 6, 4, 9],
                    [4, 9, 6, 8, 7, 2, 3, 5, 1],
                    [5, 7, 8, 6, 1, 9, 2, 3, 4],
                    [6, 3, 4, 5, 2, 8, 9, 1, 7],
                    [9, 2, 1, 7, 3, 4, 8, 6, 5]
                ]
        self.assertListEqual(expected, actual, "Example1")
        
        
if __name__ == '__main__':
    unittest.main()