class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        rows = len(board)
        cols = len(board[0])

        visited = set()

        def dfs(i, j, ptr):

            # Base Case 1
            # Entire word matched
            if  ptr == len(word):
                return True

            # Base Case 2
            # Out of bounds
            if i < 0 or j < 0 or i >= rows or j >= cols:
                return False

            # Base Case 3
            # Already visited
            if (i,j) in visited:
                return False

            # Base Case 4
            # Character doesn't match
            if board[i][j] != word[ptr]:
                return False
            # Mark visited
            visited.add((i, j))
            # Explore
            down = dfs(i + 1, j, ptr + 1)
            up = dfs(i - 1, j, ptr + 1)
            right = dfs(i, j + 1, ptr + 1)
            left = dfs(i, j - 1, ptr + 1)

            # Backtrack
            # Remove from visited
            visited.remove((i, j))
            return down or up or right or left

        for i in range(rows):
            for j in range(cols):

                if dfs(i, j, 0):
                    return True

        return False
        