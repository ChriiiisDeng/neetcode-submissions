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
        