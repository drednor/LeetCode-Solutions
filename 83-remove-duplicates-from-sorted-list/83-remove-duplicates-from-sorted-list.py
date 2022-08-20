# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = set()
        cur = head
        prev = None
        while cur:
            if cur.val in res:
                prev.next = cur.next
                cur = cur.next 
                continue
            else:
                res.add(cur.val)
            prev = cur
            cur = cur.next
        return head
        