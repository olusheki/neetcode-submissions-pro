import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        '''
        understand:
            we have a list of stones and their weights. we want to simulate this algorthm
                we take the two heaviest stones, and smash them together. if x == y, they are both destroyed.
                however, if one is larger than the other, the smaller is destroyed and the larger has a new weight larger-smaller
                continue until there is 1 or less stone
                if 1 stone, return weight
                if no stone, return 0.
            
        plan:
            we use heap to quickly get out the max values that we actually want, then we pop the new values if any back into the heap.
            we can check if the length of the heap becomes 1 or less. 
            
        '''
        n_stones = [-s for s in stones]
        heapq.heapify(n_stones)
        while len(n_stones) >= 2:
            rock1 = heapq.heappop(n_stones)
            rock2 = heapq.heappop(n_stones)
            if rock1 == rock2:
                continue
            if rock1 > rock2:
                heapq.heappush(n_stones, rock2-rock1)
            else:
                heapq.heappush(n_stones, rock1-rock2)

        if len(n_stones) == 0:
            return 0
        else:
            return -heapq.heappop(n_stones)