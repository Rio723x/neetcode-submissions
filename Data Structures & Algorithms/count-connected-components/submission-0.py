class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = { i : [] for i in range(n)}
        for u , v in edges :
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        def dfs(node):
            if node in visited:
                return 
            
            visited.add(node)

            for i in graph[node]:
                dfs(i)
        
        components = 0

        for node in range(n):
            if node not in visited:
                dfs(node)
                components+=1
        return components

        