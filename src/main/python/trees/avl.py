from typing import List
from collections import deque
import math, random

class AVLTreeNode:
    def __init__(self, key) -> None:
        self.key = key
        self.left = None
        self.right = None
        self.height = 1
    

class AVLTree:
    def __init__(self) -> None:
        self.root = None
        self.debug = True
    
    def _log(self, message) -> None:
        if self.debug:
            print(message)
    
    def _height_node(self, node) -> int:
        if node is None:
            return 0
        return node.height
    
    def _calc_balance(self, node) -> int:
        if node is None:
            return 0
        
        left_height = 0 if node.left is None else node.left.height
        right_height = 0 if node.right is None else node.right.height
        return left_height - right_height


    def _balance_node(self, node) -> AVLTreeNode:
        balance = self._calc_balance(node)
        left_balance = self._calc_balance(node.left)
        right_balance = self._calc_balance(node.right)
        self._log(f"balancing: {node.key}({balance}), ({left_balance}, {right_balance})")
        
        new_node = node
        if balance > 1 and left_balance >= 0:
            new_node = self._right_rotate(node)
        
        if balance > 1 and left_balance < 0:
            node.left = self._left_rotate(node.left)
            new_node = self._right_rotate(node)
        
        if balance < -1 and right_balance <= 0:
            new_node = self._left_rotate(node)
        
        if balance < -1 and right_balance > 0:
            node.right = self._right_rotate(node.right)
            new_node = self._left_rotate(node)
        
        self._log(f"balanced: {node.key}({balance}) -> {new_node.key}({self._calc_balance(new_node)} = {self._height_node(new_node.left)}-{self._height_node(new_node.right)})")
        return new_node

    def _right_rotate(self, y) -> AVLTreeNode:
        x = y.left
        r_x = x.right

        x.right = y
        y.left = r_x

        y.height = max(self._height_node(y.left), self._height_node(y.right))+1
        x.height = max(self._height_node(x.left), self._height_node(x.right))+1
        
        return x
    
    def _left_rotate(self, y) -> AVLTreeNode:
        x = y.right
        l_x = x.left

        x.left = y
        y.right = l_x

        y.height = max(self._height_node(y.left), self._height_node(y.right))+1
        x.height = max(self._height_node(x.left), self._height_node(x.right))+1

        return x


    def _insert_node(self, node, key) -> AVLTreeNode:
        if node is None:
            self._log(f"{key} node created")
            return AVLTreeNode(key)
        
        if key > node.key:
            node.right = self._insert_node(node.right, key)
            self._log(f"{node.key} <-R- {node.right.key}")
        elif key < node.key:
            node.left = self._insert_node(node.left, key)
            self._log(f"{node.key} <-L- {node.left.key}")
        else:
            return node
        
        left_height = 0 if node.left is None else node.left.height
        right_height = 0 if node.right is None else node.right.height
        node.height = max(left_height, right_height)+1
         
        return self._balance_node(node)

    
    def _find_min(self, node) -> AVLTreeNode:
        while node.left is not None:
            node = node.left

        return node
    
    def _find_max(self, node) -> AVLTreeNode:
        while node.right is not None:
            node = node.right

        return node

    
    def _delete_node(self, node, key) -> AVLTreeNode:
        if node is None:
            return None
        
        if key > node.key:
            node.right = self._delete_node(node.right, key)
        elif key < node.key:
            node.left = self._delete_node(node.left, key)
        else:
            if node.right is None or node.left is None:
                temp = node.left if node.left else node.right
                if temp is None:
                    return None
                else:
                    node = temp
            else:
                temp = self._find_min(node.right)
                node.key = temp.key
                node.right = self._delete_node(node.right, temp.key)
        
        left_height = 0 if node.left is None else node.left.height
        right_height = 0 if node.right is None else node.right.height
        node.height = max(left_height, right_height)+1

        return self._balance_node(node)

    def insert(self, key) -> None:
        if self.root is None:
            self.root = AVLTreeNode(key)
            return
        
        self.root = self._insert_node(self.root, key)

    def find_successor(self, key) -> int: 
        last_node_left = None
        parent_node = None
        node = self.root
        while node is not None and node.key != key:
            parent_node = node
            node = node.right if key > node.key else node.left
            if node is not None and node == parent_node.left:
                last_node_left = parent_node
        
        # left sub-tree and no right
        if key < parent_node.key and (node is None or node.right is None):
            return parent_node
        
        # right sub-tree and no right
        if key > parent_node.key and (node is None or node.right is None):
            # backtrace to first right (or last left from top)
            return last_node_left

        successor_node = self._find_min(node.right)
        return successor_node.key if successor_node is not None else None

    def find_predecessor(self, key):
        last_node_right = None
        parent_node = None
        node = self.root
        while node is not None and node.key != key:
            parent_node = node
            node = node.right if key > node.key else node.left
            if node is not None and parent_node.right == node:
                last_node_right = parent_node
        
        # right sub-tree and no left
        if key > parent_node.key and (node is None or node.left is None):
            return parent_node
        
        # left sub-tree and no left
        if key < parent_node.key and (node is None or node.left is None):
            return last_node_right
        
        predecessor_node = self._find_max(node.left)
        return predecessor_node.key if predecessor_node is not None else None
    
    def delete(self, key) -> None:
        if self.root is None:
            return
        
        self.root = self._delete_node(self.root, key)

    
    def has_key(self, key) -> bool:
        node = self.root
        while node is not None and node.key != key:
            node = node.right if key > node.key else node.left
        
        return node is not None
    
    def traverse_level(self) -> List[List[int]]:
        tree = []
        if self.root is None:
            return tree
        
        cur_level = deque()
        cur_level.append(self.root)

        next_level = deque()
        log = []
        while len(cur_level) > 0:
            while len(cur_level) > 0:
                node = cur_level.popleft()
                
                if node is not None:
                    next_level.append(node.left)
                    next_level.append(node.right)
                    log.append(node.key)
                else:
                    log.append(None)
            if len(next_level) > 0:
                tree.append(log)
            cur_level = next_level
            next_level = deque()
            log = []
        return tree

    def traverse_inorder(self) -> List[int]:
        tree = []
        if self.root is None:
            return tree
        
        def inorder(node):
            if node is None:
                return
            
            inorder(node.left)
            tree.append(node.key)
            inorder(node.right)

        inorder(self.root)
        return tree

import unittest

def construct_avl_tree(tree_data: List[int]) -> AVLTree:    
    tree = AVLTree()
    tree.debug = True
    if tree_data is None \
        or len(tree_data) == 0:
        return tree

    for key in tree_data:
        tree.insert(key)
    
    return tree

class Testcase(unittest.TestCase):
    def test_ascend(self):
        keys = [0, 1, 2, 3, 4]
        tree = construct_avl_tree(keys)

        level = tree.traverse_level()
        inorder = tree.traverse_inorder()

        print("test_ascend", level)
        
        self.assertEqual(len(keys), len(inorder), "ascend: size match")
        self.assertEqual(int(math.log2(len(keys)))+1, len(level), "ascend: height")

    def test_decend(self):
        keys = list(reversed([0, 1, 2, 3, 4]))
        tree = construct_avl_tree(keys)

        level = tree.traverse_level()
        inorder = tree.traverse_inorder()

        print("test_decend", level)
        
        self.assertEqual(len(keys), len(inorder), "test_decend: size match")
        self.assertEqual(int(math.log2(len(keys)))+1, len(level), "test_decend: height")

    def test_random(self):
        keys = [0, 1, 2, 3, 4]
        random.shuffle(keys)
        tree = construct_avl_tree(keys)

        level = tree.traverse_level()
        inorder = tree.traverse_inorder()

        print("test_random", level)
        
        self.assertEqual(len(keys), len(inorder), "test_random: size match")
        self.assertEqual(int(math.log2(len(keys)))+1, len(level), "test_random: height")


    def test_delete(self):
        keys = [0, 1, 2, 3, 4]
        random.shuffle(keys)
        tree = construct_avl_tree(keys)
        tree.delete(3)

        level = tree.traverse_level()
        inorder = tree.traverse_inorder()

        print("test_delete", level)
        
        self.assertEqual(len(keys)-1, len(inorder), "test_delete: size match")
        self.assertEqual(False, 3 in inorder, "test_delete: key shouldn't exist")


    def test_delete_none(self):
        keys = [0, 1, 2, 3, 4]
        random.shuffle(keys)
        tree = construct_avl_tree(keys)
        tree.delete(10)

        level = tree.traverse_level()
        inorder = tree.traverse_inorder()

        print("test_delete_none", level)
        
        self.assertEqual(len(keys), len(inorder), "test_delete_none: size match")
        self.assertEqual(False, 10 in inorder, "test_delete_none: key shouldn't exist")

    def test_insert(self):
        keys = [0, 1, 3, 4, 8, 9]
        random.shuffle(keys)
        tree = construct_avl_tree(keys)
        tree.insert(2)

        level = tree.traverse_level()
        inorder = tree.traverse_inorder()

        print("test_insert", level)
        
        self.assertEqual(len(keys)+1, len(inorder), "test_insert: size match")
        self.assertEqual(True, 2 in inorder, "test_insert: key should exist")

    def test_insert_same(self):
        keys = [0, 1, 3, 4, 8, 9]
        random.shuffle(keys)
        tree = construct_avl_tree(keys)
        tree.insert(3)

        level = tree.traverse_level()
        inorder = tree.traverse_inorder()

        print("test_insert_same", level)
        
        self.assertEqual(len(keys), len(inorder), "test_insert_same: size match")
        self.assertEqual(True, 3 in inorder, "test_insert_same: key should exist")


    def test_lot_of_keys(self):
        keys = [i for i in range(30)]
        random.shuffle(keys)
        tree = construct_avl_tree(keys)

        level = tree.traverse_level()
        inorder = tree.traverse_inorder()

        print("test_lot_of_keys", level)
        expected_height = int(math.log2(len(keys)))+1
        height_diff = expected_height - len(level)
        print(f"height_diff = {height_diff} = {expected_height} - {len(level)}")
        
        self.assertEqual(len(keys), len(inorder), "test_lot_of_keys: size match")
        self.assertTrue(height_diff in range(-1, 1), "test_lot_of_keys: height")

if __name__ == '__main__':
    unittest.main()