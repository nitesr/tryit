# coding:: utf-8
#
# A spanning tree is defined as a tree-like subgraph of a connected, 
#   undirected graph that includes all the vertices of the graph.
#   and a minimum spanning tree (MST) is defined as a spanning tree 
#   that has the minimum weight among all the possible spanning trees.
#
#  
# Example 1:
#   Input: edges = [[1, 2, 2], [1, 3, 10], [2, 3, 3]]
#   Output: edges = [[1, 2, 2], [2, 3, 3]] 
#   Explanation: In the three node (1, 2, 3) graph the mst can
#       be formed by edges 1-2 & 2-3 covering all nodes and min cost of 5
#
#

def krushkal_union_find(n, edges):
    # initalize (parent, num_children) for each vertex
    parent = [(i, 1) for i in range(n+1)]
    num_mst_edges = 0

    def _find_root(node):
       if parent[node][0] == node:
           return parent[node]
       
       # replace the root node for faster find next time
       root_node = _find_root(parent[node][0])
       parent[node] = (root_node[0], -1)
       return root_node

    mst_edges = []
    total_cost = 0
    for n1, n2, wt in sorted(edges, key=lambda e: ( e[2], e[0], e[1] )):
        r1 = _find_root(n1)
        r2 = _find_root(n2)
        # merge two rooted sets into to one if they differ
        if r1[0] != r2[0]:
            p_root, c_root = (r1, r2) if r1[1] > r2[1] else (r2, r1)
            parent[c_root[0]] = (p_root[0], -1)
            parent[p_root[0]] = (p_root[0], p_root[1]+c_root[1])
            total_cost += wt
            num_mst_edges += 1
            mst_edges.append([n1, n2, wt])
    
    # if number of edges are lesser than (n-1), the graph is disconnected
    #   it can't be greater
    if num_mst_edges != n-1:
        return [], -1
    
    mst_edges.sort(key=lambda e: (e[0], e[1]))
    return mst_edges, total_cost

def find_mst(n, edges):
    mst_edges, mst_cost = krushkal_union_find(n, edges)
    
    return mst_edges


import unittest

class Testcase(unittest.TestCase):
    def test_example1(self):
        actual = find_mst(3, [[1, 2, 2], [1, 3, 10], [2, 3, 3]])
        expected = [[1, 2, 2], [2, 3, 3]]
        self.assertListEqual(expected, actual, "example1") 
    
    def test_strongly_connected(self):
        actual = find_mst(5, [[1, 2, 2], [1, 3, 10], [1, 4, 5], [1, 5, 3], [2, 3, 2], [2, 4, 5], [2, 5, 5], [3, 4, 2], [3, 5, 7], [4, 5, 2]])
        expected = [[1, 2, 2], [2, 3, 2], [3, 4, 2], [4, 5, 2]]
        self.assertListEqual(expected, actual, "strongly_connected") 
    
    def test_one_self(self):
        actual = find_mst(1, [[1, 1, 0]])
        expected = []
        self.assertListEqual(expected, actual, "one_self") 

    def test_one(self):
        actual = find_mst(1, [])
        expected = []
        self.assertListEqual(expected, actual, "one") 
    
    def test_disconnected(self):
        actual = find_mst(4, [ [1, 2, 1], [1, 4, 1], [2, 4, 0] ])
        expected = []
        self.assertListEqual(expected, actual, "disconnected") 
    


if __name__ == '__main__':
    unittest.main()