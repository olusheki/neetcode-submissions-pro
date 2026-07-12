from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        u: return a substring (that is contiguous) of s that has every character
        and its frequency in t. If a substring with that property doesn't
        exist, return an empty string

        m: state tracker + dynamic window + two pointer since we need
        to actually return the string

        p: I need to return the actual string, then I can return a subset
        of s with a slice (s[l:r]). what's the best method for tracking the 
        state of the window, and being able to check if t's elements are all
        there?

        and also being able to query the state in > O(n)?
        What we can't do:
            a dict where we check if all letters in t have the same freq
            a set since t can have duplicates
        idea:
            what if we just started with the freq of t. we can adjust what we've
            seen in the subwindow by updating the freq table. then 
            at each iteration, check if that table is none. If it is, that means that
            all of the elements in t are inbetween l and r? 
            However, I would need to del freq[elem] when 0. 

        idea to use a int that tracks how many unique chars have been satisfied
        when one is no longer satisfied the increment the int again

        i:
        l start at 0
        import counter and get counter of t O(n)
        start for loop with r as index to end of s:
            if s[r] in t.keys(): O(n), so isn't this already O(n^2)?
        
        '''
        if not t:
            return ''
        freq = Counter(t)
        window = {}

        satisfied = 0
        need = len(freq)

        res = ""
        res_len = float("inf")

        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1

            if c in freq and window[c] == freq[c]:
                satisfied += 1

            while satisfied == need:
                if (r - l + 1) < res_len:
                    res = s[l:r+1]
                    res_len = r - l + 1

                left_char = s[l]
                window[left_char] -= 1
                if left_char in freq and window[left_char] < freq[left_char]:
                    satisfied -= 1
                l += 1

        return res

        # track = {}
        # #for the condition to break, satisfied should equal the len of keys in freq
        # satisfied = 0 
        # # use a while loop so indexes are persistent
        # l = 0
        # r = 0
        # # while
        # while satisfied < len(freq.keys()):
        #     if s[r] in track:
        #         track[s[r]] += 1
        #     else:
        #         track[s[r]] = 1
        #     if track[s[r]] == freq[s[r]]:
        #         satisfied += 1
        
        # while l < len(s):
        #     if l not in freq:
        #         l += 1
        #     # how could l not be in track?
        #     elif track[l] > freq[l]:
        #         l += 1
        #     else:
        #         return s[l:r]


            
