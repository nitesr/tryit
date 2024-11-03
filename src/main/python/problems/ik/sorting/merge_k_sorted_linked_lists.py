# coding:: utf-8
#
# Merge K Sorted Linked Lists
#   Given k linked lists where each one is sorted in the ascending order, merge all of them into a single sorted linked list.
#
# Example 1:
#   Input: 
#       lists = [ [1, 3, 5], [3, 4], [7] ]
#   Output: [1, 3, 3, 4, 5, 7]
#
# Constraints:
#   0 <= k <= 10^4
#   0 <= length of any given linked list <= 10^3
#   -10^9 <= node values <= 10^9
#   Sum of the lengths of all given lists won't exceed 10^5.

import unittest
from heapq import heappush, heappop, heapify 
from typing import List

"""
For your reference:
"""
class LinkedListNode:
    def __init__(self, value, next_node = None):
        self.value = value
        self.next = next_node

def build_linked_list(list_values: List[int]) -> LinkedListNode:
    if len(list_values) == 0:
        return None
    
    node = LinkedListNode(list_values[-1], None)
    for i in range(len(list_values)-2, -1, -1):
        node = LinkedListNode(list_values[i], node)
    
    return node

def read_linked_list(node: LinkedListNode) -> List[int]:
    cur_node = node

    vals = []
    while cur_node is not None:
        vals.append(cur_node.value)
        cur_node = cur_node.next
    return vals

def merge_k_lists(lists):
    """
    Args:
     lists(list_LinkedListNode_int32)
    Returns:
     LinkedListNode_int32
    """
    # Solution:
    #   We can use a min heap to keep track of min of k values from k sorted list
    #   Each time we pop min, we advance the index of corresponding sorted list
    #   We continue till all the elments are read
    #   Time Complexity: O(klogk + nklogk) = O(nklogk)
    #   Space Complexity: O(k) for heap and O(kn) for output
    
    k_min_heap = []
    for li in range(len(lists)):
        if lists[li] is not None:
            k_min_heap.append((lists[li].value, li))
    heapify(k_min_heap)

    sol_head = LinkedListNode(-1) # dummy head node

    cur_node = sol_head
    while len(k_min_heap) > 0:
        k_min = heappop(k_min_heap)
        cur_node.next = LinkedListNode(k_min[0])
        cur_node = cur_node.next

        lists[k_min[1]] = lists[k_min[1]].next
        if lists[k_min[1]] is not None:
            heappush(k_min_heap, (lists[k_min[1]].value, k_min[1]))

    return sol_head.next

class Testcase(unittest.TestCase):
    def test_example1(self):
        lists = [ build_linked_list([1, 3, 5]), build_linked_list([3, 4]), build_linked_list([7]) ]
        actual = read_linked_list(merge_k_lists(lists))
        expected = [1, 3, 3, 4, 5, 7]
        self.assertListEqual(expected, actual, "Example1") 

    def test_one_empty(self):
        lists = [ build_linked_list([1, 3, 5]), build_linked_list([]), build_linked_list([7]) ]
        actual = read_linked_list(merge_k_lists(lists))
        expected = [1, 3, 5, 7]
        self.assertListEqual(expected, actual, "one_empty") 

    def test_all_duplicates(self):
        lists = [ build_linked_list([2, 2]), build_linked_list([2, 2]), build_linked_list([2, 2]) ]
        actual = read_linked_list(merge_k_lists(lists))
        expected = [2, 2, 2, 2, 2, 2]
        self.assertListEqual(expected, actual, "all_duplicates") 

    def test_all_empty(self):
        lists = [ build_linked_list([]), build_linked_list([]), build_linked_list([]) ]
        actual = read_linked_list(merge_k_lists(lists))
        expected = []
        self.assertListEqual(expected, actual, "all_empty") 

    def test_one_list(self):
        lists = [ build_linked_list([1, 4, 7, 9, 10]) ]
        actual = read_linked_list(merge_k_lists(lists))
        expected = [1, 4, 7, 9, 10]
        self.assertListEqual(expected, actual, "one_list") 

    def test_one_each(self):
        lists = [ build_linked_list([1]), build_linked_list([2]), build_linked_list([3]) ]
        actual = read_linked_list(merge_k_lists(lists))
        expected = [1, 2, 3]
        self.assertListEqual(expected, actual, "one_each") 

if __name__ == '__main__':
    unittest.main()