class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(node: Optional[ListNode], prev: Optional[ListNode]):
            if node is None:
                return prev
            next, node.next = node.next, prev
            return reverse(next, node)

        return reverse(head, None)