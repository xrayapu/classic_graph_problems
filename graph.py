# bfs man ! bfs ! 


# from collections import defaultdict
# class Graph:
#     def __init__(self):
#         self.graph= defaultdict(list)

#     def addEdge(self,u,v):
#         self.graph[u].append(v)
#         # self.graph[v].append(u)

#     def bfs(self,s):
#         queue=[]
#         visited= [False]*(max(self.graph)+1)

#         queue.append(s)
#         visited[s]=True
#         ans=[]

#         while queue:
#             it= queue.pop(0)
#             ans.append(it)
#             print(it, end=" ")
#             for i in self.graph[it]:
#                 if not visited[i]:
#                     queue.append(i)
#                     visited[i]= True

#         return ans



# # Driver code
# if __name__ == '__main__':

#     # Create a graph given in
#     # the above diagram
#     g = Graph()
#     g.addEdge(0, 1)
#     g.addEdge(0, 2)
#     g.addEdge(1, 2)
#     g.addEdge(2, 0)
#     g.addEdge(2, 3)
#     g.addEdge(3, 3)

#     print("Following is Breadth First Traversal"
#         " (starting from vertex 2)")
#     print(g.bfs(2))

# recusive approch !!! 

# from collections import defaultdict, deque
# class Graph:
#     def __init__(self):
#         self.graph= defaultdict(list)

#     def add_edge(self,u,v):
#         self.graph[u].append(v)

#     def dfs(self, s):
#         visited=set()
#         ans=[]
#         self.helper(s, visited,ans)
#         return ans

#     def helper(self, s, visited,ans):
#         visited.add(s)
#         ans.append(s)
#         for i in self.graph[s]:
#             if  i not  in visited:
#                 self.helper(i,visited, ans)
#         # stack= deque()
#         # stack.append(s)
#         # visited[s]=True
#         # while stack:
#         #     it= stack.pop()
#         #     if not visited[it]:
#         #         visited[it]= True
#         #         ans.append(it)

#         #         for i in reversed(self.graph[it]):
#         #             if not visited[i]:
#         #                 stack.append(i)
#         # return ans


# g = Graph()
# g.add_edge(0, 1)
# g.add_edge(0, 2)
# g.add_edge(1, 2)
# g.add_edge(2, 0)
# g.add_edge(2, 3)
# g.add_edge(3, 3)

# result = g.dfs(2)  # Start DFS from node 2
# print("\nDFS traversal:", result)

# bfs:
# from collections import defaultdict

# class Graph:
#     def __init__(self):
#         self.graph= defaultdict(list)

#     def addEdge(self, u,v ):
#         self.graph[u].append(v)
#         self.graph[v].append(u)

#     def bfs(self, s):
#         ans=[]
#         queue=[]
#         # visited=[False]*(max(self.graph)+1)
#         visited=set()
#         queue.append(s)
#         # visited[s]=True
#         visited.add(s)

#         while queue:
#             it= queue.pop(0)
#             ans.append(it)
#             for i in self.graph[it]:
#                 if i not in visited:
#                     queue.append(i)
#                     # visited[i]= True
#                     visited.add(i)

#         return ans


# g=Graph()
# g.addEdge('a','b')
# g.addEdge('b','c')
# g.addEdge('c','a')
# g.addEdge('c','d')

# print(g.bfs('a'))


# most efficient way to code bfs 



# from collections import defaultdict,deque

# class Graph:
#     def __init__(self):
#         self.graph=defaultdict(list)

#     def addEdge(self,u,v):
#         self.graph[u].append(v)
#         self.graph[v].append(u)

#     def bfs(self, s):
#         ans=[]
#         visited=set()
#         queue= deque([s])

#         #queue.append(s)
#         visited.add(s)
#         while queue:
#             it=queue.popleft()
#             ans.append(it)
#             for i in self.graph[it]:
#                 if i not in visited:
#                     queue.append(i)
#                     visited.add(i)


#         return ans
    


# if __name__ == "__main__":
#     g = Graph()
#     g.addEdge('a', 'b')
#     g.addEdge('b', 'c')
#     g.addEdge('c', 'a')
#     g.addEdge('c', 'd')

#     print("BFS starting from 'a':")
#     result = g.bfs('a')
#     print("BFS traversal order:", result)



# dfs :


# from collections import defaultdict, deque

# class Graph:
#     def __init__(self):
#         self.graph= defaultdict(list)

#     def addEdge(self,u,v):
#         self.graph[u].append(v)
#         self.graph[v].append(u)

#     def dfs(self, s):
#         visited=set()
#         stack= deque([s])
#         
#         ans=[]
#         while stack:
            
#             it= stack.pop()
#             if it not in visited:
#                 visited.add(it)
#                 ans.append(it)
            

#             for i in reversed(self.graph[it]): # Reverse to match recursive DFS orde
#                 if i not in visited:
#                     stack.append(i)
                    


#         return ans
    
# if __name__ == "__main__":
#     g = Graph()
#     g.addEdge('a', 'b')
#     g.addEdge('b', 'c')
#     g.addEdge('c', 'a')
#     g.addEdge('c', 'd')

#     print("DFS starting from 'a':")
#     result = g.dfs('a')
#     print("DFS traversal order:", result)

# from collections import defaultdict, deque
# class Graph:
#     def __init__(self):
#         self.graph= defaultdict(list)

#     def addEdge(self, u,v):
#         self.graph[u].append(v)
#         self.graph[v].append(u)

#     def dfs(self,s):

#         ans=[]
#         visited=set()
#         self.helper(s,ans,visited)

#         return ans
    
#     def helper(self,s,ans,visited):
#         visited.add(s)
#         ans.append(s)
#         for i in (self.graph[s]):
#             if i not in visited:
#                 self.helper(i, ans, visited)


# if __name__ == "__main__":
#     g = Graph()
#     g.addEdge('a', 'b')
#     g.addEdge('b', 'c')
#     g.addEdge('c', 'a')
#     g.addEdge('c', 'd')

#     print("DFS starting from 'a':")
#     result = g.dfs('a')
#     print("DFS traversal order:", result)

from collections import defaultdict, deque
class Graph:
    def __init__(self):
        self.graph=defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def Bfs(self,s):
        ans=[]
        visited=set()
        s=deque([s])
        visited.add(s)
        while s:
            it=s.popleft()
            
            ans.append(it)
            
            for i in self.graph[it]:
                if i not in visited:
                    s.append(i)
                    visited.add(i)


        return ans

if __name__ == "__main__":
    g = Graph()
    g.addEdge('a', 'b')
    g.addEdge('b', 'c')
    g.addEdge('c', 'a')
    g.addEdge('c', 'd')

    print("BFS starting from 'a':")
    result = g.Bfs('a')
    print("BFS traversal order:", result)
