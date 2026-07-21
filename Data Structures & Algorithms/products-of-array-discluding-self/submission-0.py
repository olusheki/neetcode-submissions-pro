class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''I know this includes something to do with a running some that is tracking 
        the product up until a point, but I don't know exactly the 
        mechanics of making it naturally exclusive.
        
        If we have a running sum for i that is the product
        of everything to the left, and then a running some for i 
        that is the product of everything to the right,
        you can apply both of then in 2 o(n) for loops.
        '''
        output = [1] * len(nums)
        left = 1
        for i in range(len(nums)):
            output[i] *= left
            left *= nums[i]
        right = 1
        for i in range(len(nums) -1,-1,-1):
            output[i] *= right
            right *= nums[i]
        return output

