
# 5 6
# 1 2 10
# 1 3 20
# 2 4 30
# 3 4 40
# 3 5 50
# 4 5 60

 #  jab u v w govrn ho 


#  Un-Directed graph 

n, m = map(int, input().split())

adj = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v, w = map(int, input().split())  # u --(w)--> v
    adj[u].append((v, w))
    adj[v].append((u, w))  
      #  Un-Directed graph 


print(adj)
# op 
# [ [], 
#   [(2, 10), (3, 20)], 
#   [(1, 10), (4, 30)], 
#   [(1, 20), (4, 40), (5, 50)], 
#   [(2, 30), (3, 40), (5, 60)], 
#    [(3, 50), (4, 60)]   ]

# ----------------

# Printing adjacency list
# for i in range(1, n + 1):
#     print(f"Node {i}: {adj[i]}")

# op  
# Node 1: [(2, 10), (3, 20)]
# Node 2: [(1, 10), (4, 30)]
# Node 3: [(1, 20), (4, 40), (5, 50)]
# Node 4: [(2, 30), (3, 40), (5, 60)]
# Node 5: [(3, 50), (4, 60)]
