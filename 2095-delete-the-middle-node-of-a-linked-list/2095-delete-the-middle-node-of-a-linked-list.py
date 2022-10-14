# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        if not head.next:
            return None
        while True:
            fast = fast.next.next
            if not (fast and fast.next):
                slow.next = slow.next.next
                break
            slow = slow.next
        return head
            
        