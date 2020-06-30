from queue import Queue
import sys
input = sys.stdin.readline
def BFS(graph, p,q, num):

    v = []
    for i in range(num):
        v.append(False)
    v[p] = True

    que = Queue()
    que.put((p,graph[p],0))

    while not que.empty():
        cur, options,dist = que.get()
        if cur == q:
            return dist
        for i in options:
            if not v[i]:
                v[i] = True
                que.put((i,graph[i],dist+ 1))
    return 'Should not get here'
N, p,q,M = map(int, input().split())

graph = []
for i in range(N):
    graph.append([])

for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)

p -= 1
q -= 1

print(BFS(graph,p,q,N))
