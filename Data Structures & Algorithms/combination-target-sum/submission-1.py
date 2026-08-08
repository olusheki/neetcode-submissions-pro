class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        '''
        this needs to be recursive
        '''
        res = []
        def backtrack(curnum, path, total):
            # curnum is supposed to be the number you're adding
            # like the index in nums
            # path is the array so that I can push it to a bigger list 
            # I just don't know how to avoid duplicates in subsets
            # total will be to see if the amount of path is equal to target
            
            if total == target:
                res.append(list(path))
            if total > target:
                return
            for i in range(curnum, len(nums)): 
                path.append(nums[i])
                backtrack(i, path, total + nums[i])
                path.pop()
            
        #for i in range(len(nums)):
        backtrack(0, [], 0)
        return res