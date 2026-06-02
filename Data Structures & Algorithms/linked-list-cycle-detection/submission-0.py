# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = []
        head_pointer = head
        first_it = True

        while (head is not None and head.next is not None):
            if head in seen:
                return True
            if head == head_pointer:
                if first_it:
                   first_it = False
                else:
                    return False
            
            seen.append(head)
            head = head.next
        
        return False
        