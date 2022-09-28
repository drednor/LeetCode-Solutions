# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None and n == 1:
            return None
        cur = head
        total = 0
        while cur:
            total += 1
            cur = cur.next
        cur = head
        print(total)
        if total == n:
            return head.next
        n = total - n
        i = 0
        while i < n-1:
            cur = cur.next
            i+=1
        cur.next = cur.next.next
        return head
        