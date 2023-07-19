class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = root = ListNode()
        cur = head

        while cur and cur.next:
            # dummy cur cur.next
            dummy.next = cur.next
            cur.next = cur.next.next
            dummy.next.next = cur
            # dummy cur.next cur
            dummy = cur
            # cur.next cur/dummy
            cur = cur.next
            # cur.next dummy cur

        if cur:
            dummy.next = cur

        return root.next
