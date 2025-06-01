
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

import heapq

def _build_adj_list(num_nodes, edges):
    adj_map = { i: [] for i in range(1, num_nodes+1)}
    for e in edges:
        adj_map[e[0]].append((e[2], e[1], e[0]))
        adj_map[e[1]].append((e[2], e[0], e[1]))
    return adj_map

def prims_mst(num_nodes, edges):
    # Prims Algorithm leverages a BFS like algorithm each time
    #   picking an edge from the captured nodes with minimum cost.
    #
    # We will mark the captured nodes and maintain the edges coming from captured 
    #   ones in a priority queue (or min heap) which makes the looking up 
    #   next edge with log(m) time complexity.
    #
    # TC: O(M Log M) where M is edges
    # SC: O(M)
    adj_map = _build_adj_list(num_nodes, edges)
    captured = [False]*(num_nodes+1)
    q = []

    captured[1] = True
    for e in adj_map[1]:
        heapq.heappush(q, e)

    mst_edges = []
    mst_cost = 0
    while len(q) > 0 and len(mst_edges) < num_nodes - 1:
        e = heapq.heappop(q)
        if captured[e[1]]:
            continue
        
        captured[e[1]] = True
        mst_cost += e[0]
        mst_edges.append([e[2], e[1], e[0]])

        for ne in adj_map[e[1]]:
            heapq.heappush(q, ne)
    
    if len(mst_edges) < num_nodes - 1:
        return [], -1
    
    return mst_edges, mst_cost


import unittest

class Testcase(unittest.TestCase):
    def test_example1(self):
        actual, _ = prims_mst(3, [[1, 2, 2], [1, 3, 10], [2, 3, 3]])
        expected = [[1, 2, 2], [2, 3, 3]]
        self.assertListEqual(expected, actual, "example1") 
    
    def test_strongly_connected(self):
        actual, _ = prims_mst(5, [[1, 2, 2], [1, 3, 10], [1, 4, 5], [1, 5, 3], [2, 3, 2], [2, 4, 5], [2, 5, 5], [3, 4, 2], [3, 5, 7], [4, 5, 2]])
        expected = [[1, 2, 2], [2, 3, 2], [3, 4, 2], [4, 5, 2]]
        self.assertListEqual(expected, actual, "strongly_connected") 
    
    def test_one_self(self):
        actual, _ = prims_mst(1, [[1, 1, 0]])
        expected = []
        self.assertListEqual(expected, actual, "one_self") 

    def test_one(self):
        actual, _ = prims_mst(1, [])
        expected = []
        self.assertListEqual(expected, actual, "one") 
    
    def test_disconnected(self):
        actual, _ = prims_mst(4, [ [1, 2, 1], [1, 4, 1], [2, 4, 0] ])
        expected = []
        self.assertListEqual(expected, actual, "disconnected") 
    

if __name__ == '__main__':
    unittest.main()