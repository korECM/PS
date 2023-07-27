from collections import defaultdict
from typing import List, Dict


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        candidates = []
        itinerary_length = len(tickets) + 1
        ticket_map = self.build_map(tickets)
        visited = set()

        def dfs(fr: str, path: List[str]):
            if candidates:
                return
            to_list = ticket_map[fr]
            if len(path) == itinerary_length:
                candidates.append(path)
                return

            for to, index in to_list:
                if candidates:
                    return
                if index not in visited:
                    visited.add(index)
                    dfs(to, path + [to])
                    visited.remove(index)

        dfs("JFK", ["JFK"])

        return candidates[0]

    def build_map(self, tickets: List[List[str]]) -> Dict[str, List[tuple[str, int]]]:
        ticket_map: defaultdict[str, List[tuple[str, int]]] = defaultdict(list)
        for i, ticket in enumerate(sorted(tickets)):
            ticket_map[ticket[0]].append((ticket[1], i))
        return ticket_map
