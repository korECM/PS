class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = head = ListNode()
        extra_num = 0

        while l1 and l2:
            extra_num, sum = divmod(l1.val + l2.val + extra_num, 10)
            head.next = ListNode(val=sum)
            head, l1, l2 = head.next, l1.next, l2.next

        remain_list = l1 if l1 else l2

        while remain_list:
            extra_num, sum = divmod(remain_list.val + extra_num, 10)
            head.next = ListNode(val=sum)
            head, remain_list = head.next, remain_list.next

        if extra_num > 0:
            head.next = ListNode(val=extra_num)

        return dummy.next