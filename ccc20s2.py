import sys
input = sys.stdin.readline

rows = int(input())
columns = int(input())
grid = [list(map(int, input().split())) for i in range(rows)]


def FACTORS_MAZE(val, rows, columns):
    visited = [0] * (10 ** 6 + 1)
    queue = [(0, 0)]
    visited[val[0][0]] = 1
    while queue:
        x, y = queue.pop()

        for i in range(1, int(val[x][y]**0.5) + 1, 1):
            if val[x][y] % i != 0:
                continue

            j = int(val[x][y] / i)

            if j <= rows and i <= columns:
                if visited[val[j - 1][i - 1]] == 0:
                    queue.append((j - 1,i - 1))
                    visited[val[j - 1][i - 1]] = 1

            if i <= rows and j <= columns:
                if visited[val[i - 1][j - 1]] == 0:
                    queue.append((i - 1, j - 1))
                    visited[val[i - 1][j - 1]] = 1

        if visited[rows*columns]:
            return 'yes'
    return 'no'

print FACTORS_MAZE(grid,rows,columns)
