# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        i = 0
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            i+=1
        if i == 0:
            return None
        cur = head
        temp = 0
        while temp != i-1:
            cur = cur.next
            temp += 1
        cur.next = cur.next.next
        return head