class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = head = ListNode()
        if not head:
            return None
        print(f'head : {head.val}')
        while list1 and list2:
            if list1.val <= list2.val:
                head.next = list1
                head = list1
                list1 = list1.next
            else:
                head.next = list2
                head = list2
                list2 = list2.next

        if list1 or list2:
            head.next = list1 if list1 else list2

        return dummy.next