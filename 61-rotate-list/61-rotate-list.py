# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None
        last = head
        length = 1
        while last.next:
            length += 1
            last = last.next
        if k % length == 0:
            return head
        cur = head
        for i in range(length - (k%length)-1):
            cur = cur.next
        next_node = cur.next
        new_head = next_node
        last.next = head
        cur.next = None
        return new_head
            
            