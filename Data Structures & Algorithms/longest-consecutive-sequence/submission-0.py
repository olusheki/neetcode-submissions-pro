class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        I forgot that .sort() is O(nlogn), so my solution wasn't valid and I need to resubmit

        """
        if not nums:
            return 0
        s = set(nums)
        maxc = 0
        sc = 0
        seen = set()
        for n in nums:
            if n-1 not in s and n not in seen:
                curr = n
                while (curr + 1) in s:
                    sc += 1
                    curr += 1
                maxc = max(maxc, sc)
                sc = 0
                seen.add(n)
        maxc = max(maxc, sc)
        return maxc + 1
