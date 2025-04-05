
# course I  

from collections import deque

def find_order(V, prerequisites):
    
    adj = [[] for _ in range(V)]
    for x in prerequisites:
        adj[x[0]].append(x[1])
    
    indegree = [0] * V
    for i in range(V):
        for it in adj[i]:
            indegree[it] += 1
           
    q = deque()
    for i in range(V):
        if indegree[i] == 0:
            q.append(i)
    
    topo = []
    while q:
        node = q.popleft()
        topo.append(node)
        
        for it in adj[node]:
            indegree[it] -= 1
            if indegree[it] == 0:
                q.append(it)
    
    # return topo if len(topo) == V else []
    if len(topo) == V :
        return True 
    else :
        return False


if __name__ == "__main__":
    N = 4
    prerequisites = [[0, 1], [1, 2], [2, 3]]
    
    ans = find_order(N, prerequisites)
    print(ans)





    