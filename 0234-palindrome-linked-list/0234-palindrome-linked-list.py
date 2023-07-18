class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        data = []
        while head is not None:
            data.append(head.val)
            head = head.next
        return data == data[::-1]
