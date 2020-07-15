import sys
from collections import deque
raw_input = sys.stdin.readline
N, M, T = map(int, raw_input().split())
graph = []
for i in range(N): graph.append([])

for i in range(M):
    a, b = map(int, raw_input().split())
    a -= 1; b -= 1
    graph[a].append((b,1))

def dij(source):
    q = deque()
    q.append(source)
    dist = [float('inf')] * N
    dist[source] = 0

    while q:
        cur = q.popleft()
        for i in graph[cur]:
            newDist = dist[cur] + i[1]
            if newDist < dist[i[0]]:
                dist[i[0]] = newDist
                q.append(i[0])

    return dist

ans = []
for i in range(N):
    temp = []
    for j in range(N):
        temp.append(-1)
    ans.append(temp)
for i in range(N):
    temp = dij(i)
    for j in range(len(temp)):
        if temp[j] == float('inf'):
            ans[i][j] = "Not enough hallways!"
        else:
            ans[i][j] = temp[j] * T
Q = int(raw_input())
for i in range(Q):
    a, b = map(int, raw_input().split())
    a -= 1; b -= 1
    print(ans[a][b])
