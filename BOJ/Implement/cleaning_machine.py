# BOJ 14503, 로봇 청소기
import sys
input = sys.stdin.readline

# 반시계 방향으로 방향을 변경하는 함수
def rotate_direction(direct):
    direct -= 1
    if direct < 0:
        direct = 3

    return direct

n, m = map(int, input().rstrip().split())
x, y, d = map(int, input().rstrip().split())
arr = []
for _ in range(n):
    row_data = list(map(int, input().rstrip().split()))
    arr.append(row_data)

clean_cnt = 0
while True:

    # 1. 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
    if arr[x][y] == 0:
        clean_cnt += 1
        arr[x][y] = 2 # 청소된 칸을 2로 설정

    steps = [
        (-1, 0), # 북 0
        (0, 1), # 동 1
        (1, 0),  # 남 2
        (0, -1), # 서 3
    ]

    is_not_cleanroom = False
    for step in steps:
        mv_x = x + step[0]
        mv_y = y + step[1]

        if mv_x < 0 or mv_x >= n or mv_y < 0 or mv_y >= m:
            continue

        # 청소되지 않은 빈 칸이 존재하는 경우
        if arr[mv_x][mv_y] == 0:
            is_not_cleanroom = True
            break

    if is_not_cleanroom:
        # 3. 청소되지 않은 빈 칸이 존재하는 경우

        # 반시계 방향 회전
        d = rotate_direction(d)

        mv_x = x + steps[d][0]
        mv_y = y + steps[d][1]

        # 두 변수 값이 맵을 초과하는지 아닌지 체크
        if mv_x < 0 or mv_x >= n or mv_y < 0 or mv_y >= m:
            continue

        # 앞 칸이 청소 안 되어 있으면 전진
        if arr[mv_x][mv_y] == 0:
            x = mv_x
            y = mv_y

    else:
        # 2. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우

        # 후진할 수 있는지 확인하기 위한 방향 설정
        back_ward = rotate_direction(rotate_direction(d))

        mv_x = x + steps[back_ward][0]
        mv_y = y + steps[back_ward][1]

        # 두 변수 값이 맵을 초과하는지 아닌지 체크
        if mv_x < 0 or mv_x >= n or mv_y < 0 or mv_y >= m:
            # 이 경우 맵을 초과한다는 것은 벽을 맞닥뜨리는 것이기 때문에, break
            break

        # 벽이 아니라면 후진 가능
        if arr[mv_x][mv_y] != 1:
            # 후진할 수 있다면 후진
            x = mv_x
            y = mv_y
        else:
            # 후진 불가능하다면, 동작을 멈춤
            break

print(clean_cnt)