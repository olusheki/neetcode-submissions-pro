class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        maybe this is greedy?

        AAABABABBBB
             l
                  r
        so the idea is to have the freq of the window
        and make sure that the freq across all the chars don't
        differ by k. if it does, then advance the window
        else, grow the window until the condition fails again.
        we can update maxlen the whole way through

        p:
        make a dictionary
        make pointers l and r = 0
        while r < len(s)
            if s[r] in dict.keys()
                dict[r] += 1
            else:
                dict[r] = 1
            # now make the logic for making sure our condition works
            .values() will give us a list of ints. 
            We know it will be easier to keep the one of most value
            and change the other ones
            so if we get the max value, then take all the other ones and 
            sum them up, if they are over k, then the condition fails.

            else, we can continue. However, that makes it O(n^2) right?
        '''
        freq = {}
        l = r = maxfreq = maxlen = 0

        for r in range(len(s)):
            freq[s[r]] = 1 + freq.get(s[r], 0)
            maxfreq = max(maxfreq, freq[s[r]])

            while (r - l + 1) - maxfreq > k:
                freq[s[l]] -= 1
                l += 1
            maxlen = max(maxlen, r - l + 1)

        return maxlen

        # while r < len(s):
        #     if s[r] in freq.keys():
        #         freq[s[r]] += 1
        #     else:
        #         freq[s[r]] = 1
        #     maxfreq = max(maxfreq, freq[s[r]])
        #     # if the size of the window minus max freq is > k
        #     while ((r - l) - maxfreq) > k:
        #         freq[s[r]] -= 1
        #         l += 1
        #     r += 1
        #     maxlen = max(maxlen, r - l)
            
        # return maxlen

