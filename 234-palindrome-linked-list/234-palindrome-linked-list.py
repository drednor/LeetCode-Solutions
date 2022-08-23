# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
        rev = prev
        start = head
        # print(rev.val)
        # print(start.val)
        # print(start, rev)
        while start != rev and start and rev:
            if start.val != rev.val:
                return False
            start = start.next
            rev = rev.next
        return True