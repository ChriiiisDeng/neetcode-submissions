# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur_node = head
        dummy = ListNode()

        while cur_node:
            next = cur_node.next
            cur_node.next = dummy.next
            dummy.next = cur_node
            cur_node = next

        return dummy.next
    

    def reorderList(self, head: Optional[ListNode]) -> None:
        slow,fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        l1 = head
        l2 = slow.next
        slow.next = None
        l2 = self.reverseList(l2)

        dummy = ListNode()
        cur = dummy
        while l1 or l2:
            if l1:
                cur.next = l1
                l1 = l1.next
                cur = cur.next
            if l2:
                cur.next = l2
                l2 = l2.next
                cur = cur.next

        head = dummy.next
        