# Given a weighted graph and a source vertex in the graph, 
#   find the shortest paths from the source to all the other vertices in the given graph.
#
# Example 1:
#   Input: 
#       edges: [ [1, 2, 4], [1, 8, 8], [2, 3, 8], [2, 8, 11], [3, 4, 7], [3, 6, 4], [3, 9, 2], [4, 5, 9], [4, 6, 14], [5, 6, 10], [6, 7, 2], [7, 8, 1], [7, 9, 6], [8, 8, 7] ] 
#       source_node: 1
#       num_nodes: 9
#   Output:
#       distance: [0, 4, 12, 19, 21, 11, 9, 8, 14 ]

import heapq

def dijstra_shortest_path(edges, source_node, num_nodes):
    # Dijskra's algorithm works like a BFS but each time we pick with next
    #   edge/node we pick the one with minimum weight.
    # As we traverse the graph, we may encounter shorter path for the already
    #   captured node, which we will update.
    # We will matain the captured nodes with their shortest path from source node.
    #   a priority queue (min heap), where we will pick the edge with min weight.
    def _build_adj_map(edges, num_nodes):
        adj_list = {i:[] for i in range(1, num_nodes+1)}
        for e in edges:
            adj_list[e[0]].append((e[1], e[2]))
            adj_list[e[1]].append((e[0], e[2]))
        return adj_list
    
    adj_list = _build_adj_map(edges, num_nodes)
    captured = [False]*(num_nodes+1)
    shortest_paths = [float('+inf')]*(num_nodes+1)
    shortest_paths[source_node] = 0

    q = []
    for (nb_node, wt) in adj_list[source_node]:
        heapq.heappush(q, (wt, nb_node))
    captured[source_node] = True
    
    while len(q) > 0:
        wt, node = heapq.heappop(q)
        shortest_paths[node] = min(wt, shortest_paths[node])

        if not captured[node]:
            captured[node] = True
            for nb_node, nb_wt in adj_list[node]:
                heapq.heappush(q, (wt+nb_wt, nb_node))
        
    return shortest_paths[1:]

import unittest
class Testcase(unittest.TestCase):
    def test_example1(self):
        edges = [ [1, 2, 4], [1, 8, 8], [2, 3, 8], [2, 8, 11], [3, 4, 7], [3, 6, 4], [3, 9, 2], [4, 5, 9], [4, 6, 14], [5, 6, 10], [6, 7, 2], [7, 8, 1], [7, 9, 6], [8, 9, 7] ]
        actual = dijstra_shortest_path(edges, 1, 9)
        expected = [ 0, 4, 12, 19, 21, 11, 9, 8, 14 ]
        self.assertListEqual(expected, actual, "example1")
    
    def test_one(self):
        actual = dijstra_shortest_path([], 1, 1)
        expected = [ 0 ]
        self.assertListEqual(expected, actual, "one")

    def test_strongly_connected_3(self):
        actual = dijstra_shortest_path([[1, 2, 4], [1, 3, 3], [2, 3, 10]], 3, 3)
        expected = [3, 7, 0 ]
        self.assertListEqual(expected, actual, "strongly_connected_3")  

if __name__ == '__main__':
    unittest.main()