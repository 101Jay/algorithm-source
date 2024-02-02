# BOJ 3190, 뱀
import sys, heapq
input = sys.stdin.readline

def change_dir(cur, stmt):
    # 오른쪽으로 이동일 경우
    if stmt == 'D':
        cur += 1
    # 왼쪽으로 이동일 경우
    else:
        cur -= 1

    # 넘치는 것을 대비
    if cur == 0:
        cur = 4
    elif cur == 5:
        cur = 1

    return cur

n = int(input().rstrip())

apple_num = int(input().rstrip())
apples = [tuple(map(int, input().rstrip().split())) for _ in range(apple_num)]

turn_num = int(input().rstrip())
turns = []
for _ in range(turn_num):
    turn = input().rstrip().split()
    turns.append((int(turn[0]), turn[1]))

heapq.heapify(turns)

direction = 2 # Up = 1 Right = 2 Down = 3 Left = 4
second = 0
pos = (0, 0)
body = [(0,0)]

while True:

    # 조건에 맞춰 방향 변경
    if turns and turns[0][0] == second:
        cur_dir = heapq.heappop(turns)
        direction = change_dir(direction, cur_dir[1])

    # direction에 맞춰서 이동
    if direction == 1:
        pos = (pos[0] - 1, pos[1])
    elif direction == 2:
        pos = (pos[0], pos[1] + 1)
    elif direction == 3:
        pos = (pos[0] + 1, pos[1])
    else:
        pos = (pos[0], pos[1] - 1)

    # 시간 증가
    second += 1

    # 사과가 있다면 먹음
    eat_apple = False
    for a_pos in apples:
        if a_pos[0] - 1 == pos[0] and a_pos[1] - 1 == pos[1]:
            eat_apple = True
            apples.remove(a_pos)
            break

    ##### 탈출 조건
    # 막다른 곳이라면 탈출
    if pos[0] < 0 or pos[0] >= n or pos[1] < 0 or pos[1] >= n:
        break

    # 몸에 닿으면 탈출
    touch = False
    for b in body:
        if b[0] == pos[0] and b[1] == pos[1]:
            touch = True
            break
    if touch:
        break # 전체 루프 탈출
    #####

    # 몸 길이 수정
    # 사과를 먹지 않았다면 기존 위치를 지워줌 지금의 위치 추가는 공통적
    if not eat_apple:
        del body[0]
    body.append(pos)

print(second)