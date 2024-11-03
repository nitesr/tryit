# coding:: utf-8
#
# Merge One Sorted Array Into Another
#   First array has n positive numbers, and they are sorted in the non-descending order.
#   Second array has 2n numbers: first n are also positive and sorted in the same way but 
#       the last n are all zeroes.
#   Merge the first array into the second and return the latter. 
#   You should get 2n positive integers sorted in the non-descending order.
#
# Example 1:
#   Input: 
#       first = [1, 3, 5]
#       second = [2, 4, 6, 0, 0, 0]
#   Output: [1, 2, 3, 4, 5, 6]
#
# Constraints:
#   1 <= second.length <= 10^5
#   1 <= array elements (except those zeroes) <= 2 * 109
#   You can use only constant auxiliary space.
#   
import unittest
import random
from typing import List

def merge_one_into_another(first: List[int], second: List[int]) -> List[int]:
    """
    Args:
     first(list_int32)
     second(list_int32)
    Returns:
     list_int32
    """
    # Solution:
    #   Use two pointers and merge the arrays in a single pass as entries are 
    #       in non-descending order
    #   We need to traverse in descending order as the second array is empty at the end.

    # Edge cases:
    if second is None:
        return []
    
    if first is None or len(first) == 0:
        return second

    if len(second) < len(first):
        return []
    
    first_ptr = len(first) - 1
    second_ptr = len(second) - len(first) - 1

    merge_ptr = len(second) - 1

    while first_ptr >= 0 and second_ptr >= 0:
        if first[first_ptr] > second[second_ptr]:
            second[merge_ptr] = first[first_ptr]
            first_ptr -= 1
        else:
            second[merge_ptr] = second[second_ptr]
            second_ptr -= 1
        merge_ptr -= 1

    while first_ptr >= 0:
        second[merge_ptr] = first[first_ptr]
        first_ptr -= 1
        merge_ptr -= 1

    while second_ptr >= 0:
        second[merge_ptr] = second[second_ptr]
        second_ptr -= 1
        merge_ptr -= 1

    return second

class Testcase(unittest.TestCase):
    def test_example1(self):
        first = [1, 3, 5]
        second = [2, 4, 6, 0, 0, 0]
        actual = merge_one_into_another(first, second)
        expected = [1, 2, 3, 4, 5, 6]
        self.assertListEqual(expected, actual, "Example1") 

    def test_empty_first(self):
        first = []
        second = [2, 4, 6]
        actual = merge_one_into_another(first, second)
        expected = [2, 4, 6]
        self.assertListEqual(expected, actual, "empty_first") 
    
    def test_singleton_first(self):
        first = [1]
        second = [2, 4, 6, 0]
        actual = merge_one_into_another(first, second)
        expected = [1, 2, 4, 6]
        self.assertListEqual(expected, actual, "singleton_first")

    def test_first_before_second(self):
        first = [1, 2]
        second = [4, 6, 8, 9, 0, 0]
        actual = merge_one_into_another(first, second)
        expected = [1, 2, 4, 6, 8, 9]
        self.assertListEqual(expected, actual, "first_before_second") 

    def test_second_before_first(self):
        first = [4, 6, 8, 9]
        second = [1, 2, 0, 0, 0, 0]
        actual = merge_one_into_another(first, second)
        expected = [1, 2, 4, 6, 8, 9]
        self.assertListEqual(expected, actual, "second_before_first") 

    def test_interlaced(self):
        first = [1, 3, 5, 7]
        second = [2, 4, 6, 0, 0, 0, 0]
        actual = merge_one_into_another(first, second)
        expected = [1, 2, 3, 4, 5, 6, 7]
        self.assertListEqual(expected, actual, "interlaced") 

    def test_all_same(self):
        first = [1, 1, 1, 1]
        second = [1, 1, 1, 0, 0, 0, 0]
        actual = merge_one_into_another(first, second)
        expected = [1, 1, 1, 1, 1, 1, 1]
        self.assertListEqual(expected, actual, "all_same") 

if __name__ == '__main__':
    unittest.main()