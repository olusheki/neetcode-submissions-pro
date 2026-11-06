class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        constraints:
            O(1) space
            i1 < i2
            num[i] + num[i2] = target
            1-indexed array, not 0 indexed

        match: no arrs, no dict, no set, etc.
            original solution works with hashmap and consulting if we've seen a match before. 
            it is sorted, so we could probably just use two pointers
            and move each pointer until it converges to a sum while the left pointer is
            still less than right points. Cannot be equal.
        '''
        l, r = 0, len(numbers) - 1
        while l < r:
            # if sum of both is too big, shrink the right pointer
            if numbers[l] + numbers[r] > target:
                r -= 1
            # if sum of both is too small, increase the left pointer
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                return [l + 1, r + 1]