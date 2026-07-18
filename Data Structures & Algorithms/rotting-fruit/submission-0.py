from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        rows = len(grid)
        cols = len(grid[0])
        fresh = 0
        time = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r,c))
        
        while q and fresh > 0:
            for k in range(len(q)):
                r,c = q.popleft()

                #up
                if (r - 1) >= 0 and grid[r-1][c] == 1:
                    fresh -=1
                    grid[r-1][c] = 2
                    q.append((r-1,c))

                #down
                if (r + 1) < rows and grid[r+1][c] == 1:
                    fresh -=1
                    grid[r+1][c] = 2
                    q.append((r+1,c))
                #left
                if (c-1) >= 0 and grid[r][c-1] == 1:
                    fresh -=1
                    grid[r][c-1] = 2
                    q.append((r,c-1))
                #right
                if (c+1) < cols  and grid[r][c+1] == 1:
                    fresh -=1
                    grid[r][c+1] = 2
                    q.append((r,c+1))

            time +=1
        if fresh == 0:
            return time
        else:
            return -1
