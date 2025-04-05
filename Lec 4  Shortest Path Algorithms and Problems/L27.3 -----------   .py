









# DAG 

# Shortest Path in 
# Directed Acyclic Graph 
# Topological Sort: G-27

# from collections import defaultdict

def topo_sort_DFS(node, adj, vis, stack):
    vis[node] = 1 # marked it 
    for v, _ in adj[node]: # v => ngbr
        if not vis[v]:
            topo_sort_DFS(v, adj, vis, stack)
    stack.append(node)

def shortest_path(N, M, edges):
   
    # -------- adj list Create ------------------------
    adj = [[] for _ in range(N)]
    for u, v, wt in edges:
        adj[u].append((v, wt))
    
    # ---------toposot dfs------------------------
    vis = [0] * N
    stack = []
    for i in range(N):
        if not vis[i]:
            topo_sort_DFS(i, adj, vis, stack)
    
    print()
    print(stack)
# op [3, 1, 0, 2, 4, 5, 6]
    print()
    # ------------distances thing s ---------------------
    dist = [float('inf')] * N
    dist[0] = 0 
    # starting node ko mark with 0 
    while stack:
        node = stack.pop()
        if dist[node] != float('inf'):
            for v, wt in adj[node]:
                if dist[node] + wt < dist[v]:
                    dist[v] = dist[node] + wt
    return  dist
# ---------  repre also acc to quetions
    return [d if d != float('inf') else -1 for d in dist]
# Replace infinity distances with -1 
# --------- 
    result = []
    for d in dist:
        if d != float('inf'):
            result.append(d)
        else: # GFG
            result.append(-1)
    return result
# ---------
N = 7
M = 7

# aslo rep as list of list 
# or tuple of list 

# strivr e exple
edges = [(6, 4, 2), (6, 5, 3), (4, 0, 3), (4, 2, 1), (0, 1, 2), (1, 3, 1), (2, 3, 3), (5, 4, 1)]

# alsr rep  
# edges = [[6, 4, 2], [6, 5, 3], [4, 0, 3], [4, 2, 1], [0, 1, 2], [1, 3, 1], [2, 3, 3], [5, 4, 1]]


result = shortest_path(N, M, edges)
print(result)


# op starting node => 0 

# [0, 2, inf, 3, inf, inf, inf]   


# op  starting node => 6 :  dist[6] = 0 


# [5, 7, 3, 6, 2, 3, 0]







