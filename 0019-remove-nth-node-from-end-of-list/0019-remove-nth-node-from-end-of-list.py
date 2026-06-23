# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p = ListNode(0)
        p.next = head
        temp = p
        count = 0
        while temp.next:
            count += 1
            temp = temp.next
        
        x = count - n
        temp = p
        
        while x>0:
            temp = temp.next
            x -= 1
        temp.next = temp.next.next
        return p.next
        
        