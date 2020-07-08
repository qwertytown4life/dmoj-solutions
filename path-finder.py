import sys
input = sys.stdin.readline
from queue import Queue
rows, columns, K = map(int, input().split())

vis = {}
walls = {}
for i in range(K):
    x, y = map(int, input().split())
    walls[x - 1,y - 1] = 1
    vis[x - 1, y - 1] = 0


def isValid(rows,cols,r,c,visArr):
    if 0 <= r < rows and 0 <= c < cols:
        if visArr[r,c] == 0:
            return True
    return False


def BFS(graph, visited, ROWS, COLS):
    q = Queue()
    for i in graph:
        if i[0] == 0 or i[1] == COLS - 1:
            q.put(i)
            visited[i] = 1

    while not q.empty():
        r, c = q.get()
        if r == ROWS - 1 or c == 0:
            return False

        RMoves = [0,0,-1,1,1,1,-1,-1]
        CMoves = [1,-1,0,0,1,-1,1,-1]

        for j in range(8):
            rMov = RMoves[j] + r
            cMov = CMoves[j] + c
            if (rMov,cMov) in graph:
                if isValid(ROWS,COLS,rMov,cMov, visited):
                    q.put((rMov,cMov))
                    visited[rMov,cMov] = 1

    return True


if BFS(walls,vis,rows,columns):
    print('YES')
    sys.exit()

print('NO')
