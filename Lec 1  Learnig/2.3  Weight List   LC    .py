


# jab edges 
# given ho to firct convert itno
#  adjancey list 

# directed graph  Leet code   GFG 

from collections import defaultdict

edges = [[0,1,2], [0,4,1], [4,5,4], [4,2,2], [1,2,3], [2,3,6], [5,3,1]]
#edges= [(0,1,2), (0,4,1), (4,5,4), (4,2,2), (1,2,3), [2,3,6], [5,3,1]]

N = 6
# adj = defaultdict(list)
adj = [[] for _ in range(N)]

for u, v, w in edges:
    adj[u].append((v, w))  # Directed graph: Only add (v, w) for u

print(adj)


[      [(1, 2), (4, 1)], # o node 
       [(2, 3)],            # 1 node
       [(3, 6)],    # 2 node
       [],        # 3 node
       [(5, 4), (2, 2)],   # 4 node
       [(3, 1)]  ]     # 5  node

# ...............................