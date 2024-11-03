# coding: utf-8
#
# Kth Largest In A Stream
#   Given an initial list along with another list of numbers to be appended with the initial list and an integer k, 
#       return an array consisting of the k-th largest element after adding each element 
#       from the first list to the second list.
#   The stream can contain duplicates.
#
# Example 1:
#   Input: 
#       k=2, initial_stream = [4, 6], append_stream = [5, 2, 20]
#   Output: [5, 5, 6]
#   Explanation:
#       append 5 -> [4, 6, 5] -> sort -> [4, 5, 6] -> 5 (2nd largest)
#       append 2 -> [4, 6, 5, 2] -> sort -> [2, 4, 5, 6] -> 5 (2nd largest)
#       append 20 -> [4, 6, 5, 2, 20] -> sort -> [2, 4, 5, 6, 20] -> 6 (2nd largest)
#
#
# Constraints:
#   1 <= length of both lists <= 10^5
#   1 <= k <= length of initial list + 1
#   0 <= any value in the list <= 10^9

import unittest
import random
from typing import List



def kth_largest(k, initial_stream, append_stream):
    """
    Args:
     k(int32)
     initial_stream(list_int32)
     append_stream(list_int32)
    Returns:
     list_int32
    """
    # Solution:
    #    we can use a min heap of size k and keep adding to the heap if the array in stream is greater then 
    #       min in heap. The min in heap is always the kth largest.
    #   Time Complexity: O((m+n)logk)
    #   Space Complexity: O(k)
    #
    # Edge cases:
    if k < 1:
        return []
    
    import heapq
    top_k = min(k, len(initial_stream))

    min_heap = initial_stream[:top_k]
    heapq.heapify(min_heap)
    for ele in initial_stream[top_k:]:
        if ele > min_heap[0]:
            heapq.heappushpop(min_heap, ele)
    
    sol = []
    for ele in append_stream:
        if len(min_heap) < k:
            heapq.heappush(min_heap, ele)
        elif ele > min_heap[0]:
            heapq.heappushpop(min_heap, ele)
        
        if len(min_heap) >= k:
            sol.append(min_heap[0])
    return sol


class Testcase(unittest.TestCase):
    def test_example1(self):
        k = 2
        initial_stream = [4, 6]
        append_stream = [5, 2, 20]
        actual = kth_largest(k, initial_stream, append_stream)
        expected = [5, 5, 6]
        self.assertListEqual(expected, actual, "Example1")
    
    def test_example1_higher_k(self):
        k = 4
        initial_stream = [4, 6]
        append_stream = [5, 2, 20]
        actual = kth_largest(k, initial_stream, append_stream)
        expected = [2, 4]
        self.assertListEqual(expected, actual, "example1_higher_k")

    
    def test_empty_initial(self):
        k = 1
        initial_stream = []
        append_stream = [5, 2, 20]
        actual = kth_largest(k, initial_stream, append_stream)
        expected = [5, 5, 20]
        self.assertListEqual(expected, actual, "empty_initial")

    
    def test_all_same(self):
        k = 3
        initial_stream = [2, 2, 2]
        append_stream = [2, 2, 2]
        actual = kth_largest(k, initial_stream, append_stream)
        expected = [2, 2, 2]
        self.assertListEqual(expected, actual, "all_same")

    
    def test_increasing_numbers(self):
        k = 3
        initial_stream = [1, 2, 3]
        append_stream = [4, 5, 6]
        actual = kth_largest(k, initial_stream, append_stream)
        expected = [2, 3, 4]
        self.assertListEqual(expected, actual, "increasing_numbers")

    
    def test_decreasing_numbers(self):
        k = 3
        initial_stream = [6, 5, 4]
        append_stream = [3, 2, 1]
        actual = kth_largest(k, initial_stream, append_stream)
        expected = [4, 4, 4]
        self.assertListEqual(expected, actual, "decreasing_numbers")

if __name__ == '__main__':
    unittest.main()