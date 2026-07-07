class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False

        #build graph
        graph = {i : [] for i in range(n)}
        for u , v in edges:
            graph[u].append(v)
            graph[v].append(u)

        #dfs traversal and visited array
        visited = set()
        def dfs( node , parent):
            
            if node in visited :
                return False

            visited.add(node)

        #checking for cycles or neighbor == parent
            for nei in graph[node]:
                if nei == parent:
                    continue
                if not dfs( nei , node ):
                    return False
            return True

        #check connectivity
         
        return dfs( 0 , -1) and len(visited)==n 

