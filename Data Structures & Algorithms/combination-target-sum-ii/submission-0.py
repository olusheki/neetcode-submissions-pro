class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        for something like this I feel like you should start by sorting
        u:
            we need to find a combination of ints from the candidates list
            that when added up will sum up to target. However they can't be repeated. double however there can be duplicate ints, but each can be used only once in the sum.
            no duplicates allowed
        
        m: 
            the last one was backtracking, this seems like backtracking again, like it's recursive. 
        
        p:
            we should sort the list so that there's no issues with weird duplicates
            then from there we should keep track of the index, the path, and the current total of the combination sum
            There can be a stop if the total is bigger than target
            We're going to not move backwards too and we'll use a for loop to go through candidates
        '''
        candidates.sort()
        res = []
        def backtrack(index, path, total):
            if total == target:
                res.append(list(path))
                return
            if total > target:
                return
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                path.append(candidates[i])
                backtrack(i + 1, path, total + candidates[i])
                path.pop()
        backtrack(0, [], 0)
        return res