# BOJ 14499, 주사위 굴리기
import sys
input = sys.stdin.readline

# 방향에 따라 좌표를 이동하는 함수
def mv_dice(x, y, direct):
    if direct == 1: # 동쪽
        y += 1
    elif direct == 2: # 서쪽
        y -= 1
    elif direct == 3: # 북쪽
        x -= 1
    else: # 남쪽
        x += 1
    return (x, y)

# 방향에 따라 주사위를 굴리는 함수
def roll_dice(dice, direct):
    if direct == 1: # 동쪽
        dice = [0, dice[1], dice[6], dice[2], dice[3], dice[5], dice[4]]
    elif direct == 2: # 서쪽
        dice = [0, dice[1], dice[3], dice[4], dice[6], dice[5], dice[2]]
    elif direct == 3: # 북쪽
        dice = [0, dice[6], dice[2], dice[1], dice[4], dice[3], dice[5]]
    else: # 남쪽
        dice = [0, dice[3], dice[2], dice[5], dice[4], dice[6], dice[1]]
    return dice

n, m, x, y, k = map(int, input().rstrip().split())
map_arr = []
for _ in range(n):
    row_data = list(map(int, input().rstrip().split()))
    map_arr.append(row_data)

stmts = list(map(int, input().rstrip().split()))

# 주사위 초기 설정 -> 전개도 기준으로 상단부터 1 ~ 6번 인덱스를 사용
dice = [0] * 7

for stmt in stmts:
    # 1: 동 / 2: 서 / 3: 북 / 4: 남
    mv_x, mv_y = mv_dice(x,y,stmt)

    # 범위를 넘는다면 해당 명령은 무시
    if mv_x < 0 or mv_x >= n or mv_y < 0 or mv_y >= m:
        continue

    # x, y업데이트
    x, y = mv_x, mv_y

    # 주사위 굴리기
    dice = roll_dice(dice, stmt)

    # 해당면이 0일 경우
    if map_arr[x][y] == 0:
        # 주사위 바닥면의 수를 복사
        map_arr[x][y] = dice[6]
    # 0이 아닐 경우
    else:
        # 해당 면의 수가 바닥면에 복사, 해당면은 0이 됨
        dice[6] = map_arr[x][y]
        map_arr[x][y] = 0

    # 주사위의 상단면의 수를 출력
    print(dice[3])