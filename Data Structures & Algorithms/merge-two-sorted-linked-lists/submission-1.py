# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        if list1 and not list2:
            return list1

        if list2 and not list1:
            return list2

        if list1.val <= list2.val:
            head = list1
        else:
            head = list2
        curr1 = list1
        curr2 = list2
        prev = None
        while curr1 and curr2:
            if curr1.val <= curr2.val:
                if prev:
                    prev.next = curr1

                prev = curr1
                curr1 = curr1.next
            else:
                if prev:
                    prev.next = curr2
                prev = curr2
                curr2 = curr2.next

        if curr1:
            prev.next = curr1

        if curr2:
            prev.next = curr2

        return head
        
        