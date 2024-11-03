# coding:: utf-8
#
# Diameter Of A Binary Tree
#  
#
# Example 1:
#   Input: [[0], [1, 2], [3, 4]]
#   Output: 3
#   Explanation: max diameter is 3 <- 1 <- 0 -> 2
#
#
# Constraints:
#   -10^5 <= node.value <= 10^5

import unittest
from typing import List
from queue import Queue

class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def get_log(self):
        cur_q = Queue(0)
        next_q = Queue(0)

        tree_log = []

        cur_q.put(self)
        while not cur_q.empty():
            level_log = []
            while not cur_q.empty():
                node = cur_q.get()
                level_log.append(node.value if node is not None else None)
                if node is not None:
                    next_q.put(node.left)
                    next_q.put(node.right)
            tree_log.append(level_log)
            cur_q = next_q
            next_q = Queue(0)

        return tree_log

def construct_binary_tree(tree_data: List[List[int]]) -> BinaryTreeNode:
    if tree_data is None \
        or len(tree_data) == 0 \
        or len(tree_data[0]) != 1:
        return None

    p_q = Queue(0)
    c_q = Queue(0)

    root = BinaryTreeNode(tree_data[0][0])
    p_q.put(root)
    
    for l in tree_data[1:]:
        for n_i in range(0, len(l), 2):
            parent_node = p_q.get()
            if l[n_i] is not None:
                left_node = BinaryTreeNode(l[n_i])
                c_q.put(left_node)
                parent_node.left = left_node
            if l[n_i+1] is not None:
                right_node = BinaryTreeNode(l[n_i+1])
                c_q.put(right_node)
                parent_node.right = right_node
        p_q = c_q
        c_q = Queue(0)
    return root

def binary_tree_diameter(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     int32
    """
    # Write your code here.
    if root is None:
        return 0
    
    max_dia = 0
    def max_path(node: BinaryTreeNode) -> int:
        left_max = max_path(node.left) + 1 if node.left is not None else 0
        right_max = max_path(node.right) + 1 if node.right is not None else 0
        
        dia = left_max + right_max
        nonlocal max_dia
        if dia > max_dia:
            max_dia = dia
        
        return max(left_max, right_max)
        
    max_path(root)
    return max_dia

class Testcase(unittest.TestCase):
    def test_example1(self):
        root = construct_binary_tree([[0], [1, 2], [3, 4]])
        actual = binary_tree_diameter(root)
        expected = 3
        self.assertEqual(expected, actual, "Example1") 


if __name__ == '__main__':
    unittest.main()