class Solution:

    def encode(self, strs: List[str]) -> str:
        '''
        Take a list of strings and encode them to have the same information,
        but put into a single string. This is open ended and I could do a dumb or lazy
        solution, where I just put a different character to represent a break.
        Is there a more interesting solution? prolly
        '''
        st = ""
        for i, s in enumerate(strs):
            st += str(len(s)) + "#" + s
        return st
        
    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            j = s.find("#", i)
            length = int(s[i:j])
            res.append(s[j+1 : j+1+length])
            i = j + 1 + length
        return res