# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        3 pointer solution
        '''
        prev = None
        curr = head
        
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        return prev
        '''
        testing
       nil <- 0  1 -> 2 -> 3
                 c
              p
                  t
        '''