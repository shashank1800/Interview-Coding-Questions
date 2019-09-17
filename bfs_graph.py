"""
5
1 1 0 0 0
0 1 0 0 1
1 0 0 1 1
0 0 0 0 0
1 0 1 0 1

8
0 1 1 1 1 0 0 0
1 0 0 0 0 1 0 0 
1 0 0 0 0 1 0 0
1 0 0 0 0 0 1 0
1 0 0 0 0 0 1 0
0 1 1 0 0 0 0 1
0 0 0 1 1 0 0 1
0 0 0 0 0 1 1 0

"""


N = int(input())

adj = []
for i in range(N):
    adj.append([int(x) for x in input().split()])

start = int(input())
que = [start]
visited = [start]

while que:
    node = que.pop(0)
    print(node,que)
    for i in range(N):
        if adj[node][i]==1 and i!=node and i not in visited:
            que.append(i)
            visited.append(i)
