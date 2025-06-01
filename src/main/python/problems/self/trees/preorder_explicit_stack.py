"""
Given a tree do an inorder traversal with explicit stack
"""

from typing import List
from .tree_builder import Node

def preorder_traversal(node: Node) -> List[int]:
    if not node:
        return []
    
    stack = [node]
    last_seen = node

    results = [node.value]
    while stack:
        if stack[-1].left is None and stack[-1].right is None:
            last_seen = stack.pop()
            continue

        if stack[-1].right == last_seen:
            last_seen = stack.pop()
        elif stack[-1].left is None or stack[-1].left == last_seen:
            if stack[-1].right is not None:
                last_seen = stack[-1].right
                results.append(last_seen.value)
                stack.append(last_seen)
            else:
                last_seen = stack.pop()
        else:
            last_seen = stack[-1].left
            results.append(last_seen.value)
            stack.append(last_seen)
            
    
    return results

import unittest
from .tree_builder import ser_tree, deser_tree

class Testcase(unittest.TestCase):
    TEST_CASES = [
        # Basic cases
        {"tree": [1, 2, 6, 3, 5, 7, 8, None, 4, None, None, None, None, 9], "expected": [1, 2, 3, 4, 5, 6, 7, 8, 9], "description": "a tree"}
        
        # Edge cases
        ,{"tree": [], "expected": [], "description": "empty tree"}
        ,{"tree": [1], "expected": [1], "description": "one node tree"}
        ,{"tree": [1, 2, None, 3, None, 4], "expected": [1, 2, 3, 4], "description": "left only tree"}
        ,{"tree": [1, None, 2, None, 3, None, 4], "expected": [1, 2, 3, 4], "description": "right only tree"}

        # Boundary cases
        ,{"tree": [1, 2, 6, 3, 4, 5, 8], "expected": [1, 2, 3, 4, 6, 5, 8], "description": "a complete tree"}
    ]

    def test_testcases(self):
        for test_case in self.TEST_CASES:
            try:
                tree = deser_tree(test_case['tree'])
                actual = preorder_traversal(tree)
                self.assertEqual(test_case['expected'], actual, f"{test_case['description']}")
            except ValueError as e:
                print(test_case['description'], e)
                raise e

if __name__ == '__main__':
    unittest.main()