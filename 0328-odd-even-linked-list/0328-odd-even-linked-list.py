class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd_root = odd_dummy = ListNode()
        even_root = even_dummy = ListNode()

        is_odd = True

        while head:
            if is_odd:
                odd_dummy.next = head
                odd_dummy = head
            else:
                even_dummy.next = head
                even_dummy = head

            head = head.next
            is_odd = not is_odd

        even_dummy.next = None

        odd_dummy.next = even_root.next
        return odd_root.next
