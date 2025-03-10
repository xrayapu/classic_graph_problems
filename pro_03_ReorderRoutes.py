#   1 --> 2 <-- 3
#   ^
#   |
#   0 <-- 4 --> 5     # start from 0 and try to return from all the node to 0, how many change should do to make it minimum ! 


import collections
def sol(n, edges):
    g=collections.defaultdict(list) # make adj list ! 
    visit=set()
    for u,v in edges: # set the orginal(directed) as true and ( make whole graph as undirected and extra edges -> mark as false )
        g[u].append((v, True)) 
        g[v].append((u, False))
    q= deque([0])
    visit.add(0)
    ans=0
    while q:
        it= q.popleft()
        for node, is_dir in g[it]: # in bfs-> parents to child 
            if node not in visit:
                visit.add(node)
                q.append(node)
                if is_dir : # we have to return from child to parent, so this ! 
                    ans+=1

    return ans


# code is ok ! time: O(n), space: O(n) 
