# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        
        tortoise = head
        hare = head.next

        while tortoise is not None and hare is not None:
            if tortoise == hare:
                return True
            
            tortoise = tortoise.next
            hare = hare.next
            if not hare:
                return False
            hare = hare.next
        

        return False