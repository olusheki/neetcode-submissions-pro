class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        I think i've played these games before
        I think it's like original two sum, but there's an anchor
        understand:
        we need to return a list of lists and the elements of the list 
        must equal to 0. Not sorted in anyway. no duplicates. return the
        numbers, not the indicies.

        plan:
        We have an "anchor" that goes through each element of the array
        then we have our two moving pointers for the elements to the right
        of the anchor (so no repeats). The point is that I don't want a O(n^3)
        solution, so this is where the optimization happens.
        since we return the numbers and not the indicies, we can SORT! 
        nlogn. We just sort once, then we use the two pointers method.
        so, O(n^2) since n^2 is bigger degree than nlogn
        """
        # make res array
        res = set()
        # first sort nums
        nums.sort() 
        #initialize for loop n in nums
        for i, n in enumerate(nums):
            # instantiate target 0 - n
            target = (0 - n)
            l, r = i + 1, len(nums) - 1
            # initialize sub while loop starting at i to prevent dupes
            # specifically, j < r where j is i + 1 and r is len(nums)
            while l < r:
                # To figure out how to move the pointers:
                # we want it to sum to 0, so make the origin point for
                # l and r to be 0 - (n). So if n = -2, target is 2

                if nums[l] + nums[r] == target:

                    #append [n, nums[l], nums[r]]
                    res.add((n, nums[l], nums[r]))
                    l += 1
                    r -= 1
                # if l + r is too little,  
                elif nums[l] + nums[r] < target:
                    l += 1

                    # increase l by 1
                #if l + r is too big
                elif nums[l] + nums[r] > target:
                    r -= 1

                    # decrease r by 1
        return [list(triplet) for triplet in res]
