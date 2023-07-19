class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = head = ListNode()
        extra_num = 0

        while l1 or l2 or extra_num:
            sum = extra_num
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            extra_num, sum = divmod(sum, 10)
            head.next = ListNode(val=sum)
            head = head.next
            
        return dummy.next