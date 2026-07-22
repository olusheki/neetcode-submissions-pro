class Solution:
    def isValid(self, s: str) -> bool:
        '''
        is it is a open bracket push
        elif the top of stack isn't complementary then return fase
        elif there's nothing there, return false
        elif it is complementary, pop the top, continue
        once done with the loop, return not stack
        '''
        stack = []
        compliment = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        for c in s:
            if c in compliment.values():
                stack.append(c)
            else:
                if not stack:
                    return False
                elif stack[-1] != compliment[c]:
                    return False
                else:
                    stack.pop(-1)
        return not stack
                    
