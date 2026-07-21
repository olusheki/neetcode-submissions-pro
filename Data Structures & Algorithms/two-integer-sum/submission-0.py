class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for index, num in enumerate(nums):
            complement = target - num

            # Check if the required partner number was already seen
            if complement in seen:
                return [seen[complement], index]

            # Store the index of the current number
            seen[num] = index
        return []
