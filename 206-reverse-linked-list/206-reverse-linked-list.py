# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # TWO POINTERS 
        if head is None:
            return head
        cur = head;
        prev = None
        while cur is not None:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        head = prev
        return head

#         # RECURSIVE 
#         if head is None or head.next is None:
#             return head
        
#         newhead = self.reverseList(head.next)
#         head.next.next = head
#         head.next = None
#         return newhead
        
        
        