# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZgSFmP6tCjHBIN_&contestProbId=AZh9w1wa0ITHBINp&probBoxId=AZh8t9T6uvPHBINp&type=USER&problemBoxTitle=250806+List&problemBoxCnt=6#none

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)

    num_sum = -5001

    for i in range(1, N-1):
        for j in range(1, N-1):
            cur_sum = arr[i][j]
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < N and 0 <= ny < N:
                    cur_sum += arr[nx][ny]
                else:
                    break
            num_sum = max(num_sum, cur_sum)
    print(f'#{tc} {num_sum}')

