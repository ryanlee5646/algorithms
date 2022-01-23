from collections import deque
import sys

def BFS(x, y):
    queue.append([x, y])
    visit[x][y] = cnt
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if data[nx][ny] == data[x][y] and visit[nx][ny] == 0:
                    queue.append([nx, ny])
                    visit[nx][ny] = 1

N = int(input())
data = [list(map(str, sys.stdin.readline())) for _ in range(N)]
visit = [[0]*N for _ in range(N)]
queue = deque()
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


cnt = 0
for i in range(N):
    for j in range(N):
        if visit[i][j] == 0:
            BFS(i, j)
            cnt += 1
print(cnt, end=' ')

for i in range(N):
    for j in range(N):
        if data[i][j] == 'R':
            data[i][j] = 'G'
visit = [[0]*N for _ in range(N)]

cnt = 0
for i in range(N):
    for j in range(N):
        if visit[i][j] == 0:
            BFS(i, j)
            cnt += 1
print(cnt)