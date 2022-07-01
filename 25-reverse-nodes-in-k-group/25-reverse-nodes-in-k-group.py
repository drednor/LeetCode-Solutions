# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        groupPrev = dummy
        cur = head
        while True:
            kth = self.getkth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next
            prev , cur = kth.next,groupPrev.next
            while cur != groupNext:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp
            
        return dummy.next
            
            
    def getkth(self, cur, k):
        while cur and k>0:
            cur = cur.next
            k-=1
        return cur
            
        