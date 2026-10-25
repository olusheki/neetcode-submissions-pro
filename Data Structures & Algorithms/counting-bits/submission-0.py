class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for v in range(0, (n + 1)):
            count = 0
            while v > 0:
                if v & 1 == 1:
                    count += 1
                v = v >> 1
            res.append(count)
        return res