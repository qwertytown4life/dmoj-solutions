import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
N, Q = map(int, input().split())
parent = [0] * (N + 1)
ans = []

for i in range(1, N + 1):
    parent[i] = i


def find(d):
    if d != parent[d]:
        parent[d] = find(parent[d])
    return parent[d]


def merge(u, v):
    fu = find(u);
    fv = find(v)
    if fu == fv: return
    parent[fu] = fv


for i in range(Q):
    Class = list(input().split())

    K = Class[0]
    Class[1] = int(Class[1])
    Class[2] = int(Class[2])
    temp = Class[1]
    if K == 'A':
        if Class[2] >= temp:
            merge(Class[2], temp)
        else:
            merge(temp, Class[2])

    else:
        if find(Class[1]) == find(Class[2]):
            ans.append('Y')
        else:
            ans.append('N')

print('\n'.join(map(str, ans)))
