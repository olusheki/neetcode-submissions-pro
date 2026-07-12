# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        I don't like this problem one bit

        u: given the head of 2 sorted linked lists
        turn them into 1 sorted linked list

        m: update pointers. O(n + m)

        p:
        with the two pointers, we need to consider every case
        I just don't know how to handle when one is finished and 
        the other isn't. I think the condition should be
        while list1 and list2.

        we have two pointers l1 and l2:
            if one is null, then it wont run. 
            start with which ever is less
            if l1 is less:
                check where to put its pointer to
                we need to check if l1.next even exists:
                    if l1.next doesnt exist and 
                    l2 should exist since the while didn't break
                    then l1.next = l2.
                    break?
                if l1.next.val  is less than l2
                    then l1.next should point to the lesser, l1.next
                    no update, just l1 = l1.next
                elif l2.val is less than l1.next.val
                    l1.next should be l2
                    make a tmp variable for l1.next so that l1
                    can proceed.
            else
                check if l2.next.val is less than l1.val
                    then l2.next should just proceed
                elif ...
                    then tmp var, proceed
        if one is broken while the other isnt:
            [example
                           l1
            l1: 1     3    5  
                |  /  |  /  |
            l2: 2     4     6 --> 7 --> 8 --> 10 -->
                            l2

            loop breaks ?  no. must break it ourselves

            we need to return the head though, so make a dummy for
            both just in case. return the dummy that has the lower val.


            result: 1 -> 2 -> 3 -> 4 -> 5 
            
            ]
            edge cases:
                both are null, return null
                one is null, other isn't
                    return the one that isn't null

            too complicated, I'm doing too much.
        '''
        dummy = ListNode()
        # points to the last node in the merged list
        tail = dummy
        '''
        (d)
        

             l1
         2 -> 4

        (d) -> 1 -> 1 -> 2 -> ...
                         t
        
        -> 3 -> 5
           l2
        '''
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        tail.next = list1 or list2

        return dummy.next

                