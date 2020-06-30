import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N, Q = map(int, input().split())
size = [0] * (N+1); parent = [0] * (N+1)


for i in range(1,N+1):
    size[i] = 1
    parent[i] = i


def find(d):
    if d != parent[d]:
        parent[d] = find(parent[d])
    return parent[d]


def merge(u,v):
    fu = find(u); fv = find(v)
    if fu == fv: return
    parent[fu] = fv
    size[fv] += size[fu]


for i in range(Q):
    Class = list(map(int, input().split()))

    K = Class[0]; temp = Class[1]

    for j in range(1,K+1,1):
        if Class[j] > temp:
            merge(Class[j], temp)
        else:
            merge(temp, Class[j])

for i in range(len(parent)):
    parent[i] = find(i)
   
ans = []
answer = parent[1]
for i in range(N+1):
    if parent[i] == answer: ans.append(i)
    
ans.sort()
print(len(ans))
print(' '.join(map(str, ans)))
