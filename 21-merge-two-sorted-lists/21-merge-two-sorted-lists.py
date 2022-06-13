# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        dummy = result = ListNode(0)
        a = list1
        b =  list2
        while a and b:
            if a.val == b.val:
                result.next = a
                a = a.next
            elif a.val<b.val:
                result.next = a
                a = a.next
            else:
                result.next = b
                b = b.next
            result = result.next
        result.next = a or b
        
        return dummy.next