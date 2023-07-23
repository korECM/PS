from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        root = head = ListNode()
        while None in lists:
            lists.remove(None)
        while lists:
            index_min = min(range(len(lists)), key=lambda i: lists[i].val)
            head.next = lists[index_min]
            head = head.next
            lists[index_min] = lists[index_min].next
            if lists[index_min] is None:
                del lists[index_min]
        return root.next
