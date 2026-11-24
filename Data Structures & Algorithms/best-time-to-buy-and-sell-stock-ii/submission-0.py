class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        understand:
            classic buy and sell stock, but this time you're given the ability to buy and sell several times but you can only hold one
            share at a time. You can buy in the same day and cell in the same day

            example:
                buy 1, sell on 5, buy on 3, sell on 6. total profit = 7
            
            kind of looking at it, it seems like it is a greedy algortim that will take at the first lowest price, and hold until you       reach a peak.

            plan:
                definitely is a greedy algorithm where it buys the first dip, sells at the first peak before a dip again. 
                sounds like we could use two pointers for a problem like this, where they are going to same direction. 
                We can use two while loops and two variable sto hold things like values to decide whether we sell out current stock or not.

                things to track:
                    whether we are in a buy or sell state (can we buy right now? can we sell?)
                    If there is an unsettled sum at the end, dont buy
                    record all of the small profits.
                    keep track of where your pointers are and dont get into any exceptions. 
                
            implement:

                outer whileloop:
                     we are traversing with l
                     How do we get the behavior to trigger the buy state
                        ideal buy state: when the next stock is increasing. 
                        if prices[l + 1] > prices[l] then start looking for profits
                        record the initial price
                        trigger inner exploring while loop:
                            inner loop: r
                            we will trigger the sell when [prices]r + 1 < prices[r] or 
                            when it is index out of bounds. 
                            record final profits, add it to total profits
                        
                    we want l to jump to r.
                    however, if prices[l+1] < prices[l] then we should just increase l+1
                    this behavior should be O(n) and with O(1) space as well.

                to be fair, we don't need the nested while loop, we could probably just do it by comparing previous values, storing states, maybe using constants to define things, etc. Like... Okay, it is it increasing then we will just add it to the total. If the net change is decreasing dont add anything actually. 

        '''
        total = 0
        if len(prices) == 1:
            return 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                total += prices[i] - prices[i -1]
        return total


