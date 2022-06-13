#DOUBLE LINK LIST

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
    
class MyLinkedList:
    def __init__(self):
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.size = 0
        
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def addAtHead(self,value):
        
        pred = self.head
        succ = self.head.next
        
        self.size += 1
        
        
        new_node = ListNode(value)
        
        new_node.next = succ
        new_node.prev = pred
        pred.next = new_node
        succ.prev = new_node
        
    
    def addAtTail(self, value):
        
        succ = self.tail
        pred = self.tail.prev
        self.size += 1
        
        new_node= ListNode(value)
        new_node.next = succ
        new_node.prev = pred
        succ.prev = new_node
        pred.next = new_node
        
        pass
    
    def addAtIndex(self, index, value):
        if index>self.size:
            return 
        
        if index < self.size - index:
            pred = self.head
            
            for _ in range(index):
                pred = pred.next
            succ = pred.next
            
        else:
            succ = self.tail
            
            for _ in range(self.size - index):
                succ = succ.prev
            pred = succ.prev
        
        new_node = ListNode(value)
        self.size += 1
        new_node.next = succ
        new_node.prev = pred
        pred.next = new_node
        succ.prev = new_node
    
    def get(self, index):
        if index <0 or index>= self.size:
            return -1
        
        if index+1 < self.size - index:
            cur = self.head
            
            for _ in range(index+1):
                cur = cur.next
        else:
            cur = self.tail
            for _ in range(self.size - index):
                cur = cur.prev
        return cur.val
        
        
        
    
    def deleteAtIndex(self, index):
        
        if index<0 or index>=self.size:
            return
        
        if index <self.size - index:
            pred = self.head
            for _ in range(index):
                pred = pred.next
            succ = pred.next.next
        else:
            succ = self.tail
            for _ in range(self.size - index -1):
                succ = succ.prev
            pred = succ.prev.prev
        self.size -= 1
        pred.next = succ
        succ.prev = pred


# SINGLE LINK LIST
# class ListNode:
#     def __init__(self, value):
#         self.data = value
#         self.next = None
        
        
# class MyLinkedList:
#     def __init__(self):
#         self.head = None
#         self.size = 0
        
#     def addAtHead(self, value):
#         if self.head is None:
#             self.head = ListNode(value)
#             self.size+=1
#         else:
#             next_node = self.head
#             cur_node = ListNode(value)
#             self.size+=1
#             cur_node.next = next_node
#             self.head = cur_node
        
#     def addAtTail(self, value):
#         if self.head is None:
#             self.head = ListNode(value)
#             self.size+=1
#             return None
            
#         cur_node = self.head
#         while cur_node.next is not None:
#             cur_node = cur_node.next
#         cur_node.next = ListNode(value)
#         self.size+=1
        
#     def addAtIndex(self, index, value):
#         if self.head is None and index == 0:
#             self.head = ListNode(value)
#         i = 0
#         cur_node = self.head
#         while cur_node is not None:
#             if index == 0:
#                     next_node = cur_node
#                     cur_node = ListNode(value)
#                     self.size+=1
#                     cur_node.next =next_node
#                     self.head = cur_node
#                     return None
#             elif index-1 == i:
#                 prev_node = cur_node
#                 next_node = cur_node.next
#                 cur_node = ListNode(value)
#                 self.size+=1
#                 cur_node.next = next_node
#                 prev_node.next = cur_node
#                 return None
#             else:
#                 i+=1
#                 cur_node = cur_node.next
#         return None
    
#     def get(self, index):
#         if self.head is None:
#             return -1
#         i = 0
#         cur_node = self.head
#         while cur_node is not None:
#             if i == index:
#                 return cur_node.data
#             i+=1
#             cur_node = cur_node.next
#         return -1
    
#     def deleteAtIndex(self, index):
#         if self.head is None:
#             return None
        
#         i = 0
#         cur_node = self.head
#         if index == 0 and cur_node.next is None:
#             self.head = None
#             self.size-=1
#             return -1
#         while cur_node.next is not None:
#             if index == 0:
#                 self.head = cur_node.next
#                 self.size-=1
#                 return None
#             elif index-1 == i:
#                 del_node = cur_node.next
#                 cur_node.next = del_node.next
#                 self.size-=1
#                 return-1
#             else:
#                 i+=1
#                 cur_node = cur_node.next
#         return -1
                
#     def show_elements(self):
#         if self.head is None:
#             print("No Elements")
#         else:
#             current_node = self.head
#             while current_node is not None:
#                 print(current_node.data)
#                 current_node = current_node.next
                

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)