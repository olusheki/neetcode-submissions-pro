class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        find the min in logn time. 
        so it's binary search. I don't know...
        maybe the fact that nums are unique is a hint, since it must be strictly
        increasing.

        I know that you can split the array into two ascending arrays,
        so you just need to find the part where the two split.

        How do you find this cutoff?
        l  m     r
        [5,1,2,3,4]
        [3,4,5,1,2]
        '''
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                # minimum element is in left part
                l = m + 1
            else:
                # minimum element is in the right part
                r = m
        return nums[l]
