class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        visited = set()

        def dfs(i, j):

            # Out of bounds
            if i < 0 or j < 0 or i >= rows or j >= cols:
                return 0

            # base case Water
            if grid[i][j] == 0:
                return 0

            # Already visited
            if (i, j) in visited:
                return 0

            # Mark current cell
            visited.add((i, j))

            # Visit all 4 directions
            return ( 1 + dfs(i + 1, j)+ dfs(i - 1, j) + dfs(i, j + 1) + dfs(i, j - 1) )
        
        max_area = 0
        for i in range(rows):
            for j in range(cols):

                if grid[i][j] == 1 and (i, j) not in visited:
                    max_area = max(max_area , dfs(i,j))

        return max_area 
        