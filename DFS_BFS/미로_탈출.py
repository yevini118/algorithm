from collections import deque

n, m = map(int, input().split())
maze = []
for i in range(n):
    maze.append(list(map(int, input())))

def bfs(x, y):

    queue = deque()
    queue.append((x,y))
    direction = [[0,1],[0,-1],[1,0],[-1,0]]

    while(queue):
        x, y = queue.popleft()
        for d in direction:
            next_x = x + d[0]
            next_y = y + d[1]

            if next_x<0 or next_x>=n or next_y<0 or next_y>=m:
                continue

            if maze[next_x][next_y] == 1:
                maze[next_x][next_y] = maze[x][y]+1
                queue.append((next_x, next_y))

    return maze[n-1][m-1]
    
print(bfs(0,0))