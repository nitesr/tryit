class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

from typing import List
from collections import deque

def deser_tree(values: List[int]) -> Node:
    if not values or len(values) == 0:
        return None
    
    root = Node(values[0])
    q = deque()
    q.appendleft(root)

    for i in range(1, len(values), 2):
        left_node = Node(values[i]) if values[i] is not None else None
        right_node = Node(values[i + 1]) if i < len(values) - 1 and values[i + 1] is not None else None

        parent_node = q.pop()
        parent_node.left = left_node
        parent_node.right = right_node
        
        if left_node:
            q.appendleft(left_node)

        if right_node:
            q.appendleft(right_node)

    return root

def ser_tree(root: Node) -> List[int]:
    if not root:
        return []


    values = []

    q = deque()
    q.appendleft(root)
    values.append(root.value)
    while len(q) > 0:
        node = q.pop()

        values.append(node.left and node.left.value)
        values.append(node.right and node.right.value)

        if node.left:
            q.appendleft(node.left)
        if node.right:
            q.appendleft(node.right)
    
    last_non_none = len(values) - 1

    # atleast one non-none will be there
    while values[last_non_none] is None:
        last_non_none -= 1
    
    return values[:last_non_none + 1]
    


