


#  too sort basic algo 

    # indegree = [0] * V  # Initialize in-degree array
    # for i in range(V):
    #     for neighbor in adj[i]:
    #         indegree[neighbor] += 1

# ---------------------------------

# Find Eventual Safe States 
# - BFS - Topological Sort: G-25



from collections import deque

def eventual_safe_nodes(V, adj):
    adj_rev = [[] for _ in range(V)]
    indegree = [0] * V

# ----I M P O ----------------------------- 
               # Reverse kiya  first   graph  
    for i in range(V):
        for ngbr in adj[i]:  
            adj_rev[ngbr].append(i)

    for i in range(V):  # reverse gp ki indergree find kiya 
        for ngbr in adj_rev[i]:     # adj  replace by adj_rev 
            indegree[ngbr] += 1 #  

# --------------------------------- 
    q = deque()
    safe_nodes = []
    
    for i in range(V):
        if indegree[i] == 0:
            q.append(i)

    while q:
        node = q.popleft()
        safe_nodes.append(node)
        for it in adj_rev[node]:
            indegree[it] -= 1
            if indegree[it] == 0:
                q.append(it)
    
    return sorted(safe_nodes)

# Example usage
adj = [[1], [2], [3, 4], [4, 5], [6], [6], [7], [], [1, 9], [10], [8], [9]]
V = 12
safe_nodes = eventual_safe_nodes(V, adj)
print(*safe_nodes)





# # .................-----------------------------------------
# #        0    1     2        3     4    5    6    7    8      9     10   11
# adj  = [[1], [2], [3, 4], [4, 5], [6], [6], [7], [], [1, 9], [10], [8], [9]]

# #        0    1       2   3     4      5      6     7    8      9      10   11
# adjrev=[[], [0, 8], [1], [2], [2, 3], [3], [4, 5], [6], [10], [8, 11], [9], []]  
  


# indegree = [1, 1, 2, 2, 1, 1, 1, 0, 2, 1, 1, 1] 


# # op       0 1 2 3 4 5 6 7  


