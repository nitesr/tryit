# coding:: utf-8
#
# 3 Sum Smaller
#  Given a list of numbers, count the number of triplets having a sum less than a given target.
#
#   The original array's indexes identify a triplet. Therefore, any two triplets 
#       will differ if they are denoted by a different triplet of indexes, 
#       even if the values present at those indexes are the same. 
#       Please observe Example Two for more details on this.
#
# Example 1:
#   Input: numbers = [5, 0, -1, 3, 2], target = 4
#   Output: 2
#   Explanation: {numbers[1], numbers[2], numbers[3]} and {numbers[1], numbers[2], numbers[4]} 
#       are the triplets having sum less than 4
#
# Example 2:
#   Input: numbers = [2, 2, 2, 1], target = 7
#   Output: 4
#   Explanation:  {numbers[0], numbers[1], numbers[2]}, {numbers[0], numbers[1], numbers[3]}, 
#       {numbers[0], numbers[2], numbers[3]} and {numbers[1], numbers[2], numbers[3]} 
#       are the triplets having sum less than 7
#
# Constraints:
#   3 <= size of the input list <= 10^3
#   -10^5 <= any element of the input list <= 10^5
#   -10^9 <= target number <= 10^9

import unittest
from typing import List

def count_pairs(target: int, numbers: List[int], start: int) -> int:
    lo = start
    hi = len(numbers)-1
    sol = 0

    while lo < hi:
        new_sum = numbers[lo] + numbers[hi]
        if new_sum >= target:
            hi -= 1
        else:
            sol += hi - lo # lo can make pairs with all its right till hi
            lo += 1
    return sol

def count_triplets(target: int, numbers: List[int]) -> int:
    # Solution:
    #  We can leverage two_sum solution to solve it.
    #   For each entry in array, assume its part of of triplet 
    #       and find the pair which is less than target-value. Here we can use two pointer to find the pairs.
    #   For this we need to initially sort the array.

    # Edge cases:
    if numbers is None or len(numbers) < 3:
        return 0
    
    sol = 0
    numbers.sort()
    for i in range(len(numbers)-1):
        pair_target = target-numbers[i]
        if pair_target > numbers[i] + numbers[i+1]:
            sol += count_pairs(pair_target, numbers, i+1)

    return sol

class Testcase(unittest.TestCase):
    def test_example1(self):
        numbers = [5, 0, -1, 3, 2]
        target = 4
        actual = count_triplets(target, numbers)
        expected = 2
        self.assertEqual(expected, actual, "Example1") 

    def test_example2(self):
        numbers = [2, 2, 2, 1]
        target = 7
        actual = count_triplets(target, numbers)
        expected = 4
        self.assertEqual(expected, actual, "Example2") 

    def test_zero_triplets(self):
        numbers = [2, 2, 2, 2]
        target = 4
        actual = count_triplets(target, numbers)
        expected = 0
        self.assertEqual(expected, actual, "zero_triplets") 

    def test_less_than_three(self):
        numbers = [2, 2]
        target = 4
        actual = count_triplets(target, numbers)
        expected = 0
        self.assertEqual(expected, actual, "less_than_three") 

    def test_exactly_three(self):
        numbers = [2, 2, 2]
        target = 8
        actual = count_triplets(target, numbers)
        expected = 1
        self.assertEqual(expected, actual, "exactly_three") 

if __name__ == '__main__':
    unittest.main()