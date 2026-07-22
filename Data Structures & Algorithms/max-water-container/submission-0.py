class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
        understand:
        you're supposed to get the maximum amount of "water" that can be made
        depends on the min height and distance between the two
        it's a two pointer problem, the hard part is deciding how
        and when to move the pointers.
        I think you should move the smaller of the two pointers.
        '''
        l, r = 0, len(heights) - 1
        max_area = (min(heights[l], heights[r]) * r - l)
        print(max_area)
        while l < r:
            if heights[l] <= heights[r]:
                l += 1
            else:    
                r -= 1
            max_area = max(max_area, (min(heights[l], heights[r]) * (r - l)))
            #it was the order of operations
        return max_area