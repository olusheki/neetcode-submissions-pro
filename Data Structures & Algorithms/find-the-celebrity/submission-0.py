# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        '''
        there are 0 - n-1 nodes, where there may be a celebrity
        def of celebrity:
            everyone knows the celebrity, celebrity doesn't know anyone.
               0 1 2
             0   X. 
             1 
             2 X.X

        We want to find who the celebrity is, if there is one at all. We can only read to see who knows who,
        and you want to ask as few people as possible.

        output: label, if no celebrety then -1
        matrix isn't directly accessible, it is read only

        plan:
            a strategy to minimize the amount of calls we are making to find the celebrity.
            likely need to store info in case it could come in handy later.

            brute force:
                checking every person against every other person. eg:
                    does 0 know 1? yes
                    does 0 know 2? no
                    does 1 know 0? no
                    etc..

            When can we decide that we know who the celebrity is?
            When we have someone who has n -1 people knowing who they are (freq table) and they don't know anyone else.
            To check if someone doesn't know anyone else in the party, should that be after we confirm everyone else in the party knows them?
            Should there be a tuple associated with each list, where idx 0 is freq and idx 1 is outgoing connections?
            This also kind of sounds like an adjacancy matrix, but I think that we can store it in the form of a hash map
            where we are counting the rows and the cols and how full they are. Once table[col1] = full (n-1) except for @ val 1 and table[row1] is 0 still, then we found it and those are two simple integer checks. 

            Involved first building the hashmap, which may as well be O(n) because we're storing slots filled in 

            This doesn't get to core of how to make as little calls as possible. 

            We know that something is NOT the celebrity if they know someone! So when we ask someone if they know another person and they say yes, they are ruled out. But who they know aren't ruled out. If person A says they don't know person B, then person B is ruled out too, since everyone else should know them.

            lets keep a set of people we are eliminating and make sure not to ask them further questions.

            Is there an optimal starting point? Not sure. 
        '''
        candidate = 0
        for i in range(1, n):
            if knows(candidate, i):
                # cant be current candidate
                candidate = i
        for i in range(n):
            if i == candidate:
                continue
            if knows(candidate, i):
                return -1
            if not knows(i, candidate):
                return -1
        
        # we might still need to confirm that 
        return candidate

