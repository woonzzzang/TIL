from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

M, N = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]

# 1 : 익은 토마토
# 0 : 익지 않은 토마토
# -1 : 토마토가 없음 

queue = deque()
box = []

for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            queue.append([i, j])
    box.append(tomato[i])

while len(queue) > 0:
    x, y = queue.popleft()
    day = box[x][y]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M and box[nx][ny] == 0:
            box[nx][ny] = day + 1
            queue.append([nx, ny])

def get_day():
    max_day = 0
    for b in box:
        max_day = max(max_day, max(b))
    return max_day - 1 

def is_all_riped():
    for b in box:
        for tmt in b:
            if tmt == 0:
                return False
    return True

if not is_all_riped():
    print(-1)

else:
    print(get_day())