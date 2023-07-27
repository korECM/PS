from collections import defaultdict
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        route = []
        graph = defaultdict(list)
        for f, t in sorted(tickets, reverse=True):
            graph[f].append(t)

        def dfs(f):
            while graph[f]:
                dfs(graph[f].pop())
            route.append(f)

        dfs("JFK")
        return route[::-1]
