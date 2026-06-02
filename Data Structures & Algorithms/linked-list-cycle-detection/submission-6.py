# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        
        tortoise = head
        hare = head.next

        while hare is not None and hare.next:
            if tortoise is hare:
                return True
            
            tortoise = tortoise.next
            hare = hare.next.next
        

        return False