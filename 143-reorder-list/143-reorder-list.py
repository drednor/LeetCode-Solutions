# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow , fast = head, head.next
        first = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None
        prev = None
        while second:
            nextnode = second.next
            second.next = prev
            prev = second
            second = nextnode
        second = prev
        while second:
            temp = first.next 
            first.next = second
            tempback = second.next
            second.next = temp
            first = temp
            second = tempback