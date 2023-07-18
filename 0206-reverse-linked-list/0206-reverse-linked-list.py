class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        self.solve(head, dummy)
        return dummy.next if dummy.next else None

    def solve(self, head: Optional[ListNode], dummy: ListNode):
        if head is None:
            return head
        if head.next is None:
            dummy.next = head
            return head
        result = self.solve(head.next, dummy)
        result.next, head.next = head, None
        return head
