class Solution:
    def canFinish(self, numCourses: int, edges: List[List[int]]) -> bool:
        
        #build graph 
        graph = { i : [] for i in range(numCourses)}
        for u , v in edges:
            graph[v].append(u)
        if len(edges) == 0:
            return True
        #visited set and path set
        visited = set()
        path = set()

        def dfs(u):
            if u in visited:
                return True
            
            if u in path:
                return False
            
            path.add(u)

            for nei in graph[u]:
                if not dfs(nei):
                    return False
            
            visited.add(u)
            path.remove(u)
            return True
        
        for u in range(numCourses):
            if not dfs(u):
                return False
        return True

        
        

        