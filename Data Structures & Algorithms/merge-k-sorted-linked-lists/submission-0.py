# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        I think that this might require some sort of O(n^2) solution which
        would technically be O( n * k ) so...

        u: you're given a list of linked lists. I think that
        maybe at the elements it has the head of the linked list.
        we're supposed to merge every list in ascending order

        m: linked list

        p: I'm so lost... If we can only get the heads of the linkedlist we
        need to use the index and .next and stuff... idk.

        lists[0].next or something.

        first loop to get the head of each LL and compare, and point to everything possible?

            i
                 1
        0: [1    2 --> 4]
            |  / |
        1: [1    3 --> 5]
               /  2
        2: [3 --> 6]

        Can't think of anything to be honest never encountered something like this before.
        """
        if not lists:
            return None

        while len(lists) > 1:
            merged = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                merged.append(self.merge(l1, l2))
            lists = merged
        return lists[0]
    def merge(self, l1, l2):
        dummy = ListNode()
        tail = dummy
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        return dummy.next
