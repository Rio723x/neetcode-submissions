class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        rows = len(heights)
        cols = len(heights[0])

        pacific = set()
        atlantic = set()

        def dfs(i, j, visited, prevHeight):

            # Base Cases
            if (
                i < 0 or j < 0 or
                i >= rows or j >= cols or
                (i, j) in visited or
                heights[i][j] < prevHeight
            ):
                return

            visited.add((i, j))

            dfs(i + 1, j, visited, heights[i][j])
            dfs(i - 1, j, visited, heights[i][j])
            dfs(i, j + 1, visited, heights[i][j])
            dfs(i, j - 1, visited, heights[i][j])

        # Pacific (Top Row)
        for c in range(cols):
            dfs(0, c, pacific, heights[0][c])

        # Pacific (Left Column)
        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])

        # Atlantic (Bottom Row)
        for c in range(cols):
            dfs(rows - 1, c, atlantic, heights[rows - 1][c])

        # Atlantic (Right Column)
        for r in range(rows):
            dfs(r, cols - 1, atlantic, heights[r][cols - 1])

        ans = []

        for i in range(rows):
            for j in range(cols):
                if (i, j) in pacific and (i, j) in atlantic:
                    ans.append([i, j])

        return ans
            
            

        