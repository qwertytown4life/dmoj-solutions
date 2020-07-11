import sys
from collections import deque

raw_input = sys.stdin.readline 
rows, columns, K = map(int, raw_input().split())

vis = {}
walls = {}
for i in range(K):
    x, y = map(int, raw_input().split())
    walls[x - 1,y - 1] = 1
    vis[x - 1, y - 1] = 0


def isValid(rows,cols,r,c,visArr):
    if 0 <= r < rows and 0 <= c < cols:
        if visArr[r,c] == 0:
            return True
    return False


def BFS(graph, visited, ROWS, COLS):
    q = deque()
    for i in graph:
        if i[0] == 0 or i[1] == COLS - 1:
            q.append(i)
            visited[i] = 1

    while q:
        r, c = q.popleft()
        if r == ROWS - 1 or c == 0:
            return 'NO'

        RMoves = [0,0,-1,1,1,1,-1,-1]
        CMoves = [1,-1,0,0,1,-1,1,-1]

        for j in range(8):
            rMov = RMoves[j] + r
            cMov = CMoves[j] + c
            if (rMov,cMov) in graph:
                if isValid(ROWS,COLS,rMov,cMov, visited):
                    q.append((rMov,cMov))
                    visited[rMov,cMov] = 1

    return 'YES'

print BFS(walls,vis,rows,columns)
