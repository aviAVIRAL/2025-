# Cycle Detection in unirected Graph (bfs)

from collections import deque

def detect(src, adj, vis):
    vis[src] = 1  # src : starting node # short cut represnt
    q = deque([(src, -1)])  
       
    while q:
        node, parent = q.popleft()  
#     neighbor :   ngr   :   # short cut represnt 
        for neighbor in adj[node]:
            if not vis[neighbor]:
                q.append((neighbor, node))  
                vis[neighbor] = 1  
            elif parent != neighbor: # impo 
                return True  
    return False  

#    component   graph  ke code 
def isCycle(V, adj): 
    vis = [0] * V  
    for i in range(V):     # impo
        if not vis[i]:  
            if detect(i, adj, vis):
                return True  
    return False  

# Example usage
V = 4 # o based indx : node hai  1, 2, 3 only 
# adj = {0: [], 1: [2], 2: [1, 3], 3: [2]}  

# asloe   rep 
adj = [[], [2], [1, 3], [2]] 


#    1 ---- 2 ---- 3
#       no cyle exist 

ans = isCycle(V, adj)
print(1 if ans else 0)
# ------------------
# Define adjacency list
# adj = [
#     [],        # 0 (Not used, since 1-based indexing)
#     [2],       # 1 -> 2
#     [1, 3],    # 2 -> 1, 3
#     [2, 1]     # 3 -> 2, 1
# ]

#    1-----2
#    \    /
#     \  /
#      3
