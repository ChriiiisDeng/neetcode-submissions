# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedLists.append(self.mergeTwoLists(l1, l2))
            lists = mergedLists
        return lists[0]
    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        cur = dummy
        while list1 and list2:

            if list1.val <= list2.val:
                cur.next = ListNode(list1.val)
                list1 = list1.next
            else:
                cur.next = ListNode(list2.val)
                list2 = list2.next
            cur = cur.next

        while list1:
            cur.next = ListNode(list1.val)
            list1 = list1.next
            cur = cur.next
        while list2:
            cur.next = ListNode(list2.val)
            list2 = list2.next
            cur = cur.next

        return dummy.next
        