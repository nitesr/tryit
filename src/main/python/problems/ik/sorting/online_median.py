# coding: utf-8
#
# Online Median
#   Given a list of numbers, the task is to insert these numbers into a stream 
#       and find the median of the stream after each insertion. If the median is a non-integer, consider it’s floor value.
#   The median of a sorted array is defined as the middle element when the number of elements is odd 
#       and the mean of the middle two elements when the number of elements is even.
#
# Example 1:
#   Input: stream = [3, 8, 5, 2]
#   Output: [3, 5, 5, 4]
#   Explanation:
#       Iteration 1 -> [3] -> sort -> [3] -> 3 (median)
#       Iteration 2 -> [3, 8] -> sort -> [3, 8] -> 5 (median)
#       Iteration 3 -> [3, 8, 5] -> sort -> [3, 5, 8] -> 5 (median)
#       Iteration 4 -> [3, 8, 5, 2] -> sort -> [2, 3, 5, 8] -> 4 (median)
#
#
# Constraints:
#   1 <= length of stream <= 10^5
#   1 <= any value in the stream <= 10^5
#   The stream can contain duplicates.


import unittest
import random
from typing import List



def online_median(stream):
    """
    Args:
     stream(list_int32)
    Returns:
     list_int32
    """
    # Solution:
    #   Have two heaps which divides the stream in two almost equal parts in length (left could be 1 greater than right)
    #       if two heaps are of equal length median is (left_heap[0] + right_heap[0]) // 2
    #       else it is left_heap[0]
    #   Time complexity: O(nlogn)
    #   Space complexity: O(n)
    # Edge cases:
    if stream is None or len(stream) == 0:
        return []
    
    sol = [stream[0]]
    left_heap = [-stream[0]]
    right_heap = []

    import heapq
    for num in stream[1:]:
        if num > -left_heap[0]:
            heapq.heappush(right_heap, num)
        else:
            heapq.heappush(left_heap, -num)
        
        if len(left_heap) > len(right_heap) + 1:
            temp = heapq.heappop(left_heap)
            heapq.heappush(right_heap, -temp)
        elif len(left_heap) < len(right_heap):
            temp = heapq.heappop(right_heap)
            heapq.heappush(left_heap, -temp)
        
        if len(left_heap) == len(right_heap):
            sol.append((-left_heap[0] + right_heap[0]) // 2)
        else:
            sol.append(-left_heap[0])

    return sol

class Testcase(unittest.TestCase):
    def test_example1(self):
        stream = [3, 8, 5, 2]
        actual = online_median(stream)
        expected = [3, 5, 5, 4]
        self.assertListEqual(expected, actual, "Example1")

    def test_increasing_order(self):
        stream = [1, 2, 3, 4, 5, 6]
        actual = online_median(stream)
        expected = [1, 1, 2, 2, 3, 3]
        self.assertListEqual(expected, actual, "increasing_order")

    def test_decreasing_order(self):
        stream = [6, 5, 4, 3, 2, 1]
        actual = online_median(stream)
        expected = [6, 5, 5, 4, 4, 3]
        self.assertListEqual(expected, actual, "decreasing_order")

    def test_empty_stream(self):
        stream = []
        actual = online_median(stream)
        expected = []
        self.assertListEqual(expected, actual, "empty_stream")
  
    def test_one_element(self):
        stream = [1]
        actual = online_median(stream)
        expected = [1]
        self.assertListEqual(expected, actual, "one_element")
    
    def test_two_elements(self):
        stream = [1, 5]
        actual = online_median(stream)
        expected = [1, 3]
        self.assertListEqual(expected, actual, "two_element")      

if __name__ == '__main__':
    unittest.main()