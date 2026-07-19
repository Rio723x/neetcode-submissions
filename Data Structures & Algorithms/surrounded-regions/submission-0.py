class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        visited = set()

        def dfs( i , j ):

            #boundary conditions
            if i < 0 or j < 0 or i >= rows or j >= cols:
                return
            
            #checking if X or O
            if board[i][j] == 'X':
                return
            
            #if already visited
            if ( i,j ) in visited:
                return 
            visited.add((i,j))
            

            #traversing in all 4 directions
            dfs( i + 1 , j )
            dfs( i , j + 1)
            dfs( i - 1 , j)
            dfs( i , j - 1)

        for i in range(rows):
            if board[i][0] == 'O':
                dfs(i, 0)
            if board[i][cols - 1] == 'O':
                dfs(i, cols - 1)

        # DFS from first and last row
        for j in range(cols):
            if board[0][j] == 'O':
                dfs(0, j)
            if board[rows - 1][j] == 'O':
                dfs(rows - 1, j)
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O' and (i,j) not in visited:
                    board[i][j] = 'X'
            

        