# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if not head:
            return head
        headstart = head
        dummy = ListNode()
        dummy.next = head
        while n > 0 and headstart:
            headstart = headstart.next
            n -= 1
        #
        slow = head
        while headstart and headstart.next:
            slow = slow.next
            headstart = headstart.next

        if headstart == None:
            if dummy.next:
                return dummy.next.next
            else:
                return None

        if slow.next:
            slow.next = slow.next.next
        return head
