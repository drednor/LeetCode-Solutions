# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
        
        
        
        
#         if head is None:
#             return False
#         cur = head
#         if cur.next is None:
#             return False
#         if cur.next.next is None:
#             if cur.next == cur:
#                 return True
#             else:
#                 return False
            
#         i = head
#         j = cur.next
#         while j.next is not None:
#             if i == j:
#                 return True
#             i = i.next
#             if j.next.next is None:
#                 return False
#             j = j.next.next
            
#         return False