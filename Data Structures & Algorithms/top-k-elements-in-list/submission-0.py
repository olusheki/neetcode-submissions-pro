from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        sort = sorted(count.items(), key=lambda x: x[1], reverse=True)
        res = [x[0] for x in sort[:k]]
        return res
        