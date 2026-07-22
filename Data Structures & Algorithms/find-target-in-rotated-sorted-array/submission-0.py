class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        the target can be anywhere in the array, left or right.
        we can determine if it is in the left one or the right one
        by seeing if l < target < r. If so, then it is there.


        [3,4,5,6,1,2] target = 4
        l    m.    r
        3 < 5 < 2, we know target is in between l and m
        r = m
        
        [1,2,3,4,5,6] target = 4
               l m r

        first check is nums[m] == target. if so, return m
        elif nums[l] < target < nums[m]:
            it is in the left side
            make r = m 
        elif nums[m] < target < nums[r]:
            it is in the right side

        should I check l and r to see if they are target too?
        '''
        # initialize the left and right pointers
        l, r = 0, len(nums) - 1

        # we use l <= to r because...
        while l <= r:
            # calculate the middle 
            m = (l + r) // 2

            # if the m pointer is equal to target
            if target == nums[m]:
                # return middle pointer
                return m
            
            # if the value at the left pointer is < middle val
            if nums[l] <= nums[m]:
                # we are in the left part

                # if the target isn't in the left side
                if target > nums[m] or target < nums[l]:
                    # move l to the right
                    l = m + 1
                else:
                    # if it is in the left side, move r to the left
                    r = m - 1
            # we are in the right part
            else:
                # if target is 
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
        return -1