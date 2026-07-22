class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        understand: We need to return the max possible profit that 
        we could've gotten. for example, if price was stricly decreasing,
        then the output would be 0. Don't invest.
        We need to look for the opportunity that has the highest increase from the beginning
        or end

        match: this sound like a sliding window problem, since we're looking
        for the best subarray for the given array. Do I start with the ends
        moving in the same direction, or opposite ends? I feel like moving
        in the same direction. Maybe I can do one pass through:

        plan:
        l moves if r is lower than it. r moves regardless, and profit is 
        calculated at each step. keep the max profit in a variable. max().
        """

        l = 0
        maxprofit = 0
        for r in range(len(prices)):
            if prices[r] < prices[l]:
                l = r
            profit = prices[r] - prices[l]
            maxprofit = max(maxprofit, profit)
        return maxprofit
            #calculate profit at the beginning or end? I choose end.