# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        carry = 0
        while l1 or l2:
            if l1 and l2:
                val = l1.val + l2.val + carry
                l1 = l1.next
                l2 = l2.next
            elif l1:
                val = l1.val + carry
                l1 = l1.next
            else:
                val = l2.val + carry
                l2 = l2.next

            carry = 1 if  val >= 10 else 0
            val = val - 10 if val >= 10 else val
            cur.next = ListNode(val)
            cur = cur.next
        
        if carry > 0:
            cur.next = ListNode(carry)
            

        return dummy.next
        