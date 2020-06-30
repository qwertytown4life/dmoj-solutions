import sys
from queue import Queue
input = sys.stdin.readline

rows, columns = map(int, input().split())
maze = [list(map(int, input().split())) for i in range(rows)]

visited = []

for i in range(rows):
    inp = []
    for j in range(columns):
        inp.append(0)
    visited.append(inp)

def maze_solver(grid, visited, rows, columns):
    if rows == 0 and columns == 0:
        return 0

    queue = Queue()
    queue.put((0, 0, 0))
    visited[0][0] = 1

    while not queue.empty():
        x, y, dist = queue.get()
        cur_val = grid[x][y]

        ShiftUP = (x - cur_val) % (rows + 1)
        ShiftDOWN = (x + cur_val) % (rows + 1)

        ShiftLEFT = (y - cur_val) % (columns + 1)
        ShiftRight = (y + cur_val) % (columns + 1)

        if visited[ShiftUP][y] == 0:
            queue.put((ShiftUP, y, dist + 1))
            visited[ShiftUP][y] = 1

        if visited[ShiftDOWN][y] == 0:
            queue.put((ShiftDOWN, y, dist + 1))
            visited[ShiftDOWN][y] = 1

        if visited[x][ShiftRight] == 0:
            queue.put((x, ShiftRight, dist + 1))
            visited[x][ShiftRight] = 1

        if visited[x][ShiftLEFT] == 0:
            queue.put((x, ShiftLEFT, dist + 1))
            visited[x][ShiftLEFT] = 1

        if visited[rows][columns] == 1:
            return dist + 1

    return 'FOREVER'


print(maze_solver(maze, visited, rows - 1, columns - 1))
