from collections import defaultdict
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        graph: dict[int, list[int]] = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        leaves = []
        for i in range(n):
            if len(graph[i]) == 1:
                leaves.append(i)
            
        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for i in leaves:
                neighbor = graph[i].pop()
                del graph[i]
                graph[neighbor].remove(i)
                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)
            leaves = new_leaves

        return graph.keys()
