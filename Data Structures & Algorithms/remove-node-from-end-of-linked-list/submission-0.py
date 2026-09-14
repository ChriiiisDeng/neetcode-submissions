# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        prev = dummy = ListNode()
        dummy.next = head
        tail = dummy
        for i in range(n):
            tail = tail.next

        while tail.next:
            tail = tail.next
            prev = prev.next

        prev.next = prev.next.next

        return dummy.next
        