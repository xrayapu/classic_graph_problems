#graph traversal
#graph traversal
from collections import defaultdict, deque 
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph= defaultdict(list) # init() -> er kaj!
        for u,v in edges: #addEdge er kaj ! 
            graph[u].append(v)
            graph[v].append(u)
        return self.helper(destination,source,graph)

        

    def helper(self, tar ,s, graph): # bfs
        
        visited=set()
        node= deque([s])
        visited.add(s)
        while node:
            it= node.popleft()
            if it == tar: # if traverse, then the node will be in pop list ! 
                return True
            for i in graph[it]:
                if i not in visited:
                    node.append(i)
                    visited.add(i)


        return False

        
