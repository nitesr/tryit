"""
Given a Weighted Directed Acyclic Graph (DAG) and a source vertex s in it, 
    find the longest distances from s to all other vertices in the given graph.

Example1:
    Input:
        n = 5 (numbered 0 to 4) vertices
        edges: [
            [0, 1, 5],
            [0, 2, 3],
            [1, 3, 6],
            [1, 2, 2],
            [2, 4, 4],
            [2, 5, 2],
            [2, 3, 7],
            [3, 5, 1],
            [3, 4, -1],
            [4, 5, 2]
        ]
        source_vertex = 1
    output:
        [-INF, 0, 2, 9, 8 , 10]
"""

from typing import List, Dict
def longest_path_weighted_dag(n: int, edges: List[List[int]], source_vertex: int) -> List[int]:
    """
    Solution:
        get the topological sort, 
            and for each node find the max distance from the incoming edges
            int the order of toplogical sort.

        in the example:
            topological sort: 0 1 2 3 4 5

            for destination 0:
                inital vertex with 0 in-degree
                so max_dist = -inf

            for destination 1:
                its the source vertex so max_dist = 0

            for destination 2:
                incoming edges = [1, 2, 3], [0, 2, 3]
                so max_dist = max(max_dist[1] + 3, max_dist[0] + 3)
                            = max(3, -inf)
                            = 3
            and so on
        
        TC: O(V + E)
        SC: O(V + E)
    """
    adj_list = [[] for _ in range(n)]
    inv_adj_list = [[] for _ in range(n)]
    for s, d, w in edges:
        adj_list[s].append((d, w))
        inv_adj_list[d].append((s, w))
    
    def topological_sort():
        topo_order = []

        visited = [False] * n
        def dfs(v):
            visited[v] = True
            for n_v, _ in adj_list[v]:
                if not visited[n_v]:
                    dfs(n_v)
            
            topo_order.append(v)

        for v in range(n):
            if not visited[v]:
                dfs(v)
        
        topo_order.reverse()
        return topo_order


    topo_order = topological_sort()
    max_dist = [float('-inf')] * n

    i = 0
    while topo_order[i] != source_vertex:
        i += 1
    
    max_dist[i] = 0
    while i < len(topo_order):
        v = topo_order[i]
        for d, w in inv_adj_list[v]:
            max_dist[v] = max(max_dist[v], max_dist[d]+w)
        i += 1

    
    return max_dist

if __name__ == '__main__':
    n = 6
    edges = [
        [0, 1, 5],
        [0, 2, 3],
        [1, 3, 6],
        [1, 2, 2],
        [2, 4, 4],
        [2, 5, 2],
        [2, 3, 7],
        [3, 5, 1],
        [3, 4, -1],
        [4, 5, 2]
    ]
    max_dist = longest_path_weighted_dag(n, edges, 1)
    print(max_dist)




