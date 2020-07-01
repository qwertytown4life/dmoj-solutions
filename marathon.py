import sys
input = sys.stdin.readline

ans = []
def query(psa, total, l, r):
    if l == 0:
        return total - psa[r]
    else:
        return total - (psa[r] - psa[l - 1])
N, Q = map(int, input().split())
PSA = [0] * N
movies = list(map(int, input().split()))
for i in range(N):
    if i == 0:
        PSA[i] = movies[i]
    else:
        PSA[i] = PSA[i - 1] + movies[i]
full = PSA[-1]
for i in range(Q):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    ans.append(query(PSA,full,a,b))

for i in ans:
    print(i)
