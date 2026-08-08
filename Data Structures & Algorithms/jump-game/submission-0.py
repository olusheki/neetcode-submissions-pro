class Solution:
    def canJump(self, nums: List[int]) -> bool:
        '''
        work backwards and find a new goal
        until you reach the start again.

        maybe I will have the index of the current goal
        and I will have the index of what i'm searching for
        and the use nums[i] to calculate if I can reach the curgoal from curjump
        and repeat until we get to curjump = 0 or maybe even less
        should be one pass through easy O(n) solution

        edgecase:
        [1] = true or false? true
        [0] = true?

        how do I detect? when l wants to end see 
        if you can get the the curgoal from the beginning.
        '''
        curgoal = len(nums) - 1
        for l in range(len(nums) - 1, -1, -1):
            if nums[l] >= curgoal - l:
                curgoal = l
        return nums[0] >= curgoal
