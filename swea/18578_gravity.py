T = int(input())
for tc in range(1, T+1):
    W = int(input())
    boxes = list(map(int, input().split()))

    max_fall = 0

    for i in range(W-1):
        high_num = 0
        for j in boxes[i+1 : ]:
            if j >= boxes[i]:
                high_num += 1

        cur_fall = W - high_num - i - 1
        max_fall = max(max_fall, cur_fall)

    print(f'#{tc} {max_fall}')