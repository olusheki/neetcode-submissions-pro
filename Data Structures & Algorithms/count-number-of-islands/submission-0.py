from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        this is breadth first search

        I can make a helper function bfs() that takes in
        the row and column. then from there, it ventures out until
        its queue is empty then terminates

        I'll make a visited set as well

        Once the helper is initialized, I will make a for loop
        where I iterate through cells. First checking if it is
        a 0 or 1. if it's 1, check if it is in visited
        if not, then that is the start of a new island, and find
        all of its connecting pieces. and add them to visted

        return the amount of unique ones. reminds me of number of
        provences.
        '''
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()

        def bfs(r, c):
            q = deque([(r, c)])
            while q:
                # we need to filter for:
                    # if the node that we're going for is in visited 
                    # (so there's no inf loop)
                    # if it has a 1 and not a 0
                    # if it is out of bounds
                r, c = q.popleft()
                visited.add((r, c))
                for dr, dc in [(1, 0), (0, 1), (-1, 0),( 0, -1)]:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == '0' or (nr, nc) in visited:
                        continue
                    else:
                        # we add it to the queue
                        q.append((nr, nc))
        num_islands = set()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '0' or (r, c) in visited:
                    continue
                num_islands.add((r, c))
                bfs(r, c)
        return len(num_islands)
                
