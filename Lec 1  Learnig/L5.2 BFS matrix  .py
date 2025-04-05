




# Breadth First Search (BFS): Level Order Traversal

from collections import deque

def bfsOfGraph(n, adj):
    vis = [0] * n
    vis[0] = 1
    q = deque()
    q.append(0)
    bfs = []
    # =--------------------list -------------------
    # while q:
    #     node = q.popleft()
    #     bfs.append(node)
    #     for neighbor in adj[node]:
    #         if not vis[neighbor]:   # vis[neighbor] == 0:
    #             vis[neighbor] = 1
    #             q.append(neighbor)
    # return bfs
#----------------------------------------------------------------

#--------------------------Matrix----------------------
    while q:
        node = q.popleft()
        bfs.append(node)
        for neighbor in range(n):  # Iterate over possible nodes
            if adj[node][neighbor] == 1 and not vis[neighbor]:  # Check adjacency matrix
                vis[neighbor] = 1
                q.append(neighbor)
    return bfs
#-------------------#-------------------#-------------------#-------------------
def addEdge(adj, u, v): # matrix 
    adj[u][v] =1 
    adj[v][u] =1 

    
# def addEdge(adj, u, v): #  list 
#     adj[u].append(v)
#     adj[v].append(u)

if __name__ == "__main__":
    n = 5  # n nodes 
    # adj = [[0]*(n+1) for _ in range(n+1)]   1 based index node 
    adj = [[0]*n for _ in range(n)] # matrix make adj 
    # adj = [[] for _ in range(n)] #  list
#     0
#    / \
#   1   4
#  / \
# 2   3

    addEdge(adj, 0, 1)
    addEdge(adj, 1, 2)
    addEdge(adj, 1, 3)
    addEdge(adj, 0, 4)

    ans = bfsOfGraph(n, adj)
    print(*ans) # print(*ans)

# adj = [
#     [1, 4],  # Node 0 is connected to nodes 1 and 4
#     [0, 2, 3],  # Node 1 is connected to nodes 0, 2, and 3
#     [1],  # Node 2 is connected to node 1
#     [1],  # Node 3 is connected to node 1
#     [0]   # Node 4 is connected to node 0
# ]


# -------------- 
# ans = [1, 2, 3, 4 , 5] 
# for x in ans :
#     print(x, end = " ")

# print()
# print(">>>")
# print()
