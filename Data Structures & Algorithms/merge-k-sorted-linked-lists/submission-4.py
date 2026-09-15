# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class NodeWrapper:
    def __init__(self, node):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None


        min_heap = []
        cur = dummy = ListNode(0)
        for lst in lists:
            if lst is not None:
                heapq.heappush(min_heap, NodeWrapper(lst))


        while min_heap:
            node_wrapper = heapq.heappop(min_heap)
            cur.next = ListNode(node_wrapper.node.val)
            cur = cur.next
            if node_wrapper.node.next:
                heapq.heappush(min_heap, NodeWrapper(node_wrapper.node.next))

        return dummy.next
    
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
        