# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = result = ListNode(0)
        while list1 and list2:
            if list1.val == list2.val:
                result.next = list1
                list1 = list1.next
            elif list1.val < list2.val:
                result.next = list1
                list1 = list1.next
            else:
                result.next = list2
                list2 = list2.next
            result = result.next
        result.next = list1 or list2
        return dummy.next
                
            
        
        
        
        
        
#         if list1 is None and list2 is None:
#             return None
#         if list1 is None:
#             return list2
#         if list2 is None:
#             return list1
#         dummy = result = ListNode(0)
#         a = list1
#         b =  list2
#         while a and b:
#             if a.val == b.val:
#                 result.next = a
#                 a = a.next
#             elif a.val<b.val:
#                 result.next = a
#                 a = a.next
#             else:
#                 result.next = b
#                 b = b.next
#             result = result.next
#         result.next = a or b
        
#         return dummy.next