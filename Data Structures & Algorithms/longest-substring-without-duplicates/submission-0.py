class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        u: given a string s, find the len of the longest contiguous substring 
        without duplicates in the substring
        so for example, abcabcabc, the answer would be abc because it
        has completely unique chars and it's the longest.
        return the length, not the substring.

        m: we use a sliding window to keep track of the substring. we can
        use a set to keep track of the chars, and pointers to mark the 
        edges of the windows. 

        p: so basically, we initialize the l pointer = 0, and we use
        a for loop with r as the index. one pass through
        we use a set called seen.
        initialize maxlen
        we start the for loop 
            if s[r] in seen:
                we get 
                maxlen(maxlen, r-l)
                make l = r + 1
                seen.clear()
            else:
                add s[r] to set
        check maxlen again
        return maxlen
        '''
        
        nums = s
        seen = set()

        res  = 0 

        l = 0

        for r in range(len(nums)):
            while nums[r] in seen:
                seen.remove(nums[l])
            
                l+=1 
            seen.add(nums[r])
            res = max  (res ,  r - l + 1)
        
        return  res




        '''
        seen ()
        p w w k e w
              l
            r
        maxlen = 2

        seen (d)
        d v d f
        l
            r
        maxlen = 2
        '''

            