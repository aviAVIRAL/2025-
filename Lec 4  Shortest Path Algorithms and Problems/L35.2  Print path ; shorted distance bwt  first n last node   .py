



# ...................................
# Print karna hai shortest path in 
# weighted undirected graph 

# ----------------------------------

# ----------------------------------


# Find the shortest path between 
# the vertex 1 and the vertex n, 

# ....................................







# ...................................
# Print karna hai shortest path in 
# weighted undirected graph 

# ----------------------------------

# ----------------------------------


# Find the shortest path between 
# the vertex 1 and the vertex n, 

# ....................................
import heapq

def shortest_path(n, m, edges):
    # Create an adjacency list
      # 1 based  indx grarph 
    adj = [[] for _ in range(n + 1)]
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))

    # disToance and parent arrays
    disTo = [float('inf')] * (n + 1)
    parent = [i for i in range(n + 1)]

    # Priority queue for Dijkstra's algorithm
    pq = [(0, 1)]  # (disToance, node)
    disTo[1] = 0

    while pq:
        dis, node = heapq.heappop(pq)
        for ngbr, W in adj[node]:
            if dis + W < disTo[ngbr]:
                disTo[ngbr] = dis + W
                parent[ngbr] = node # imp
                heapq.heappush(pq, (disTo[ngbr], ngbr))

    if disTo[n] == float('inf'):
        return [-1]

    print()
    print(parent)
    print(disTo)
    print()


    # Bactrack: DP :  the path
    arr = []  # path
    node = n
    while parent[node] != node:
        arr.append(node)
        node = parent[node]
    
    arr.append(1) # sourse add by ur'self
    arr.reverse()

    # return arr[::-1]
    return arr[::-1]

# Driver code
if __name__ == "__main__":
    V, E = 5, 6
    edges = [
        [1, 2, 2],
        [2, 5, 5],
        [2, 3, 4],
        [1, 4, 1],
        [4, 3, 3],
        [3, 5, 1]
    ]
    result = shortest_path(V, E, edges)
    print(*result)


# op  path  print 
# 1 4 3 5
# ---------------------------------
# parent : [0,  1, 1, 4, 1, 3]
#  DIsTo :[inf, 0, 2, 4, 1, 5]




