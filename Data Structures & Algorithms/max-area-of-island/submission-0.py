from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        '''
        this can be solved with bfs, so 
        when we're adding things to visited, we can also count that
        as visiting it meaning we can increase a local counter
        and we can also have out bfs function return an integer.
        '''
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        def bfs(r, c):
            area = 1
            q = deque([(r, c)])
            while q:
                r, c = q.popleft()
                for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == 0 or (nr, nc) in visited:
                        continue
                    else:
                        # add to queue, increment area
                        q.append((nr, nc))
                        visited.add((nr, nc))
                        area += 1
            return area
        maxArea = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0 or (r, c) in visited:
                    continue
                else:
                    visited.add((r, c))
                    area = bfs(r, c)
                    maxArea = max(maxArea, area)
        return maxArea

