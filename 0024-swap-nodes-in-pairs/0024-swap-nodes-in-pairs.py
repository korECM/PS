class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = root = ListNode()
        prev_node, current_node = None, head

        while current_node:
            if prev_node:
                # root prev_node current_node
                root.next = current_node
                current_node.next, prev_node.next = prev_node, current_node.next
                # root current_node prev_node
                root = prev_node
                # current_node prev_node/root
                current_node = prev_node.next
                prev_node = None
                # root current_node
            else:
                prev_node = current_node
                current_node = current_node.next

        if prev_node:
            root.next = prev_node

        return dummy.next
