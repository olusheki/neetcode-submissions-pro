class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        arrSum = sum(nums)
        curSum = 0
        for i, n in enumerate(nums):
            if curSum == arrSum - curSum - nums[i]:
                return i
            curSum += n    
        return -1