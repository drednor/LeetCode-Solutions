# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        result1 = []
        cur = head
        while cur is not None:
            result1.append(cur.val)
            cur = cur.next
        cur = head
        prev = None
        while cur is not None:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        head = prev
        result2=[]
        cur = head
        while cur is not None:
            result2.append(cur.val)
            cur = cur.next
        if result1 == result2:
            return True
        else:
            return False