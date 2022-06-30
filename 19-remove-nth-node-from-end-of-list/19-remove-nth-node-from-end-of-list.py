# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
                 4          
        1->2->3->4->5->6->7
              s---->
        f           f      f 
        '''         
        slow = fast = head
        for i in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return head
              
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        
        
        # fast = slow = head
        # for _ in range(n):
        #     fast = fast.next
        # if not fast:
        #     return head.next
        # while fast.next:
        #     fast = fast.next
        #     slow = slow.next
        # slow.next = slow.next.next
        # return head
        
        # a = head
        # lenA = 0
        # while a:
        #     lenA += 1
        #     a = a.next
        # x = lenA-n
        # a = head
        # if x==0 and head.next:
        #     head = head.next
        #     return head
        # elif x==0 and head.next is None:
        #     head = None
        #     return head
        # else:
        #     for i in range(x-1):
        #         a = a.next
        #     a.next = a.next.next
        # return head
            
        