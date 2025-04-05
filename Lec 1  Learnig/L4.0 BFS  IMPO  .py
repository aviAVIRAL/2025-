


# simplest representiopomn  

# undirestred graph ahi 

from collections import deque

def bfsOfGraph(n, start, edges):

    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    vis = [0] * n
    vis[start] = 1
    q = deque() # q = deque([start])
    q.append(start) # 
    bfs = []
       
    while q:
        node = q.popleft()
        bfs.append(node)
        for neighbor in adj[node]:
            if not vis[neighbor]:
                vis[neighbor] = 1
                q.append(neighbor)
    return bfs

if __name__ == "__main__":
    n = 5
    edges= [(0,1), (1,2), (1,3), (0,4)]

    start_node = 0 # Changed the starting node to 4 : therfrore op is [4,0,1,2,3]
    ans = bfsOfGraph(n, start_node, edges)
    print(ans)  
#     0
#    / \
#   1   4
#  / \
# 2   3

               
# edges= [(0,1), (1,2), (1,3), (0,4)]
# edges convert itno adj list 

# adj list  
# [[1, 4], [0, 2, 3], [1], [1], [0]]

# opp [0, 1, 4, 2, 3]


