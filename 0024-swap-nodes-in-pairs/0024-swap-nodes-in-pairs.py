class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = root = ListNode()
        prev.next = head
        cur = head

        while cur and cur.next:
            # prev->cur->b->next
            b = cur.next
            cur.next = b.next
            # prev b cur->next
            b.next = cur
            # prev b->cur->next
            prev.next = b
            # prev->b->cur->next

            prev = prev.next.next
            cur = cur.next

        return root.next
