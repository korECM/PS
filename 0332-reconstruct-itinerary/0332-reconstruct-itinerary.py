from collections import defaultdict
from typing import List, Dict


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        candidates = ["Z"]
        itinerary_length = len(tickets) + 1
        ticket_map = self.build_map(tickets)
        visited = set()

        def dfs(fr: str, path: str, path_length: int):
            if candidates[0] != "Z":
                return
            to_list = ticket_map[fr]
            if path_length == itinerary_length:
                candidates[0] = path

            for to, index in to_list:
                if index not in visited:
                    visited.add(index)
                    dfs(to, path + to, path_length + 1)
                    visited.remove(index)

        dfs("JFK", "JFK", 1)

        chunks, chunks_size = len(candidates[0]), 3
        return [candidates[0][i:i + chunks_size] for i in range(0, chunks, chunks_size)]

    def build_map(self, tickets: List[List[str]]) -> Dict[str, List[tuple[str, int]]]:
        ticket_map: defaultdict[str, List[tuple[str, int]]] = defaultdict(list)
        for i, ticket in enumerate(tickets):
            ticket_map[ticket[0]].append((ticket[1], i))
        for key in ticket_map:
            ticket_map[key].sort()
        return ticket_map