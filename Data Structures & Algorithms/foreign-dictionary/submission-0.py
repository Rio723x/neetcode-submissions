class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        #build graph logic
        graph = { i : [] for word in words for i in word }
        for i in range(len(words) - 1) :
            w1 = words[i]
            w2 = words[i+1]

            if ( len(w1) > len(w2) and w1.startswith(w2)):
                return ""
            for j in range( min(len(w1), len(w2))):
                if w1[j] != w2[j]:
                    graph[w1[j]].append(w2[j])
                    break


        #dfs
        visited = set()
        path = set()
        topo = []

        def dfs(node):

            path.add(node)
            visited.add(node)
            ans = True
            for nei in graph[node]:                    
                if nei in path:
                    return False

                if nei not in visited:
                    ans = ans and dfs(nei)

            path.remove(node)
            topo.append(node)

            return ans


        for node in graph:
            if node not in visited:
                if not dfs(node):
                    return ""

        topo.reverse()
        return "".join(topo)

        