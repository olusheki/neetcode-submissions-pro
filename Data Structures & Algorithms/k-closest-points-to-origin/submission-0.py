import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        '''
        understand:
            we are given a list of (basically tuples) where there is an x val and a y val for each given point. using
            the distance formula provided, figure out the k closest point to the origin.

        plan:
            I would try to make some sort of lamba equation so that we could sort our heap by that and to just pop it out like that but I have no clue how to do the syntax for that. I would look it up but I dont know if coding interviers let you look up syntax mid interview. 
            So for each point I can calculate its euclidian distance from (0,0), then I can try to use lamba or something to make our heapify sort like that and biuld it which is also O(n), then I can pop our k values until I have the K closest.
            So O(2n + k) which is O(n) time and O(n) space due to the heap.
            x1 = 0
            x2 = item[0]
            y1 = 0
            y2 = item[1]
        '''
        n_points = [ [(((0-item[0])**2)+((0-item[1])**2))**(1/2), item] for item in points ]
        heapq.heapify(n_points)
        res = []
        for i in range(k):
            res.append(heapq.heappop(n_points)[1])
        return res