# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a , b= headA, headB
        while a!=b:
            a = headB if not a else a.next
            b = headA if not b else b.next
        return a
    
        # lenA , lenB = 0 , 0
        # while a:
        #     lenA +=1
        #     a = a.next
        # while b:
        #     lenB +=1
        #     b = b.next
        # a , b = headA , headB
        # for i in range(abs(lenA-lenB)):
        #     if lenA >= lenB:
        #         a = a.next
        #     else:
        #         b = b.next
        # while a != b:
        #     a = a.next
        #     b = b.next
        # return a