import heapq
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        root = head = ListNode()
        heap: list[tuple[int, int, ListNode]] = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))
        while heap:
            (_, index, node) = heapq.heappop(heap)
            head.next = node
            head = head.next
            if node.next is not None:
                heapq.heappush(heap, (node.next.val, index, node.next))

        return root.next
