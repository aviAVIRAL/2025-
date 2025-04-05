


# 5 6
# 1 2 10
# 1 3 20
# 2 4 30
# 3 4 40
# 3 5 50
# 4 5 60

#
#     Directed graph   Code foreces 
 
 #  jab u v w govrn ho 


n, m = map(int, input().split())

adj = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v, w = map(int, input().split())  # u --(w)--> v
    adj[u].append((v, w))
    # adj[v].append((u, w))   

# #     Directed graph ke liye 

print(adj)

# ----------------

#  output 
# [ [], 
#   [(2, 10), (3, 20)],
#   [(4, 30)], 
#   [(4, 40), (5, 50)], 
#   [(5, 60)], 
#   []  ]   

