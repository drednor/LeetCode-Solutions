# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None and list2 == None:
            return None
        dummy = ListNode(0,None)
        head = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                head.next = list1
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next
            head = head.next
        if list1:
            head.next = list1
        else:
            head.next = list2
        return dummy.next
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #         dummy = result = ListNode(0)
#         while list1 and list2:
#             if list1.val == list2.val:
#                 result.next = list1
#                 list1 = list1.next
#             elif list1.val > list2.val:
#                 result.next = list2
#                 list2 = list2.next
#             else:
#                 result.next = list1
#                 list1 = list1.next
#             result = result.next
#         result.next = list1 or list2
#         return dummy.next
        
        
        
        
        #         dummy = result = ListNode(0)
#         while list1 and list2:
#             if list1.val == list2.val:
#                 result.next = list1
#                 list1 = list1.next
#             elif list1.val < list2.val:
#                 result.next = list1
#                 list1 = list1.next
#             else:
#                 result.next = list2
#                 list2 = list2.next
#             result = result.next
#         result.next = list1 or list2
#         return dummy.next
                