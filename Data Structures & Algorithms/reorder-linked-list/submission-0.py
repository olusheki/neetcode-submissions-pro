# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        '''
        1  2. 3. 4. 5. 6. 7. 8. 
        1  8  2  7. 3. 6  5. 4 ?

        I feel like I need to use an extra data struture, maybe a stack
        because I can get to half of the list, then go to the end pushing
        the nodes in a stack. Then I can start at the first node and the 
        top of the stack (the end element), and repeat until the stack

        well... I might need to use two stacks or something but I'm not sure...
        '''
        if not head:
            return
        fast = slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        
        mid = slow.next
        slow.next = None
        prev = None
        while mid:
            tmp = mid.next
            mid.next = prev
            prev = mid
            mid = tmp
        # now we inter twine
        # prev should be pointing at new node
        curr = head
        while curr and prev:
            tmp = curr.next
            curr.next = prev
            tmp2 = prev.next
            prev.next = tmp
            curr = tmp
            prev = tmp2
        return