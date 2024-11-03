# coding:: utf-8
#
# Tower Of Hanoi
#   Tower of Hanoi is a mathematical puzzle where we have three pegs and n disks. 
#   The objective of the puzzle is to move the entire stack to another peg, obeying the following simple rules:
#       Only one disk can be moved at a time.
#       Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack i.e. 
#           a disk can only be moved if it is the uppermost disk on a stack.
#       No disk may be placed on top of a smaller disk.
#
#   Given n denoting the number of disks in the first peg, return all the steps required to move all disks 
#       from the first peg to the third peg in minimal number of steps.
#
#   Return a 2d integer array containing all the steps taken to move all n disks from the first peg 
#       to the third peg in minimal number of steps. 
#   Each row will have two integers denoting from peg and to peg, for example, 
#       if the ith row is [2, 3], then it means in this step, we moved the top disk on peg 2 to peg 3.
#
# Example 1:
#   Input: n = 4
#   Output: [ [1, 2], [1, 3], [2, 3], [1, 2], [3, 1], [3, 2], [1, 2], [1, 3], [2, 3], [2, 1], [3, 1], [2, 3], [1, 2], [1, 3], [2, 3] ]
#   Explanation:
#       state: First peg: [1, 2, 3, 4], Second Peg: [], Third Peg: []
#       1. [1, 2] = Shift top disk of the first peg to top of the second peg.
#       state: First peg: [2, 3, 4], Second Peg: [1], Third Peg: []
#       2. [1, 3] = Shift top disk of the first peg to top of the third peg.
#       state: First peg: [3, 4], Second Peg: [1], Third Peg: [2]
#       ....
#       Finally, state: First peg: [], Second Peg: [], Third Peg: [1 2 3 4]
#       
# 
#  Constraints:
#   1 <= n <= 20

import unittest
import random
from typing import List

def tower_of_hanoi(n):
    """
    Args:
     n(int32)
    Returns:
     list_list_int32
    """
    # Solution:
    #   move(n, src_peg, dst_peg)
    #       move(n-1, src_peg, aux_peg)
    #       move last disk from src_peg to dst_peg
    #       move(n-1, aux_peg, dst_peg)
    #   Time Complexity: O(2^n)
    #   Space Compelxity: O(n)
    #
    # Edge cases:
    if n == 0:
        return []
    
    disk_movements = []
    def move_disks(n: int, src_peg: int, dst_peg: int, aux_peg: int) -> None:
        if n > 1:
            move_disks(n-1, src_peg, aux_peg, dst_peg)
        disk_movements.append([src_peg, dst_peg])
        if n > 1:
            move_disks(n-1, aux_peg, dst_peg, src_peg)

    move_disks(n, 1, 3, 2)
    return disk_movements

    
class Testcase(unittest.TestCase):
    def test_example1(self):
        n = 4
        actual = tower_of_hanoi(n)
        expected = [ [1, 2], [1, 3], [2, 3], [1, 2], [3, 1], [3, 2], [1, 2], [1, 3], [2, 3], [2, 1], [3, 1], [2, 3], [1, 2], [1, 3], [2, 3] ]
        self.assertListEqual(expected, actual, "Example1") 

    def test_zero(self):
        n = 0
        actual = tower_of_hanoi(n)
        expected = []
        self.assertListEqual(expected, actual, "zero") 
    
    def test_one(self):
        n = 1
        actual = tower_of_hanoi(n)
        expected = [[1, 3]]
        self.assertListEqual(expected, actual, "one") 
        
    def test_two(self):
        n = 2
        actual = tower_of_hanoi(n)
        expected = [[1, 2], [1, 3], [2, 3]]
        self.assertListEqual(expected, actual, "two") 
        

if __name__ == '__main__':
    unittest.main()