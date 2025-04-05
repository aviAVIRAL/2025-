


# dfs 

def dfs_check(node, adj, vis, path_vis , check):
    vis[node] = 1
    path_vis[node] = 1

    check[node] = 0 # 

    for neighbor in adj[node]:
        if not vis[neighbor]:
            if dfs_check(neighbor, adj, vis, path_vis,  check):
                check[node] = 0 # 
                return True

        elif path_vis[neighbor] == 1:
            check[node] = 0 # 
            return True

    check[node] = 1 #  
    path_vis[node] = 0  
    return False

def is_cyclic(V, adj):
    vis = [0] * V  
    path_vis = [0] * V  
    safenode = [ ]
    check = [0] * V #
    for i in range(V):  
        if not vis[i]:
            # if dfs_check(i, adj, vis, path_vis):
                # return True
            dfs_check(i, adj, vis, path_vis , check)

    for i in range( 0, V): 
        if check[i]== 1:
            safenode.append(i)
    return safenode
    # return False

# Example usage ------
V = 12
adj = [[1], [2], [3, 4], [4, 5], [6], [6], [7], [], [1, 9], [10], [8], [9]]

safe_nodes = is_cyclic(V, adj)
print(*safe_nodes)





