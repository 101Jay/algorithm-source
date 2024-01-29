# p119, 게임 개발

import sys
input = sys.stdin.readline

map_size = list(map(int, input().split()))
input_data = list(map(int, input().split()))
pos = [input_data[0], input_data[1]]
direction = input_data[2]

map_data = []
for i in range(map_size[0]):
    imap = list(map(int, input().split()))
    map_data.append(imap)

map_data[pos[0]][pos[1]] = -1 # 처음 시작 지점 또한 가본 곳으로 마킹

steps = [
    (-1, 0), (0, 1), (1, 0), (0, -1)
]

cnt = 0
visit_cnt = 1

while(True):
    # 왼쪽으로 방향 전환
    direction = direction - 1
    if direction < 0:
        direction = 3

    cnt += 1 # 방향 전환 카운트

    # 1, 2번째 조건
    move_pos = [pos[0] + steps[direction][0], pos[1] + steps[direction][1]]

    # 게임판 밖으로 나가지 않는지 점검
    if move_pos[0] < 0 or move_pos[0] >= map_size[0] or move_pos[1] < 0 or move_pos[1] >= map_size[1]:
        continue

    if map_data[move_pos[0]][move_pos[1]] == 0:
        pos = move_pos
        map_data[pos[0]][pos[1]] = -1 # 가본 곳으로 마킹
        cnt = 0 # 방향 전환 카운트 초기화
        visit_cnt += 1


    # 3번째 조건
    if cnt == 4:
        # 방향은 유지해야 함으로 temp_direction을 씀
        temp_direction = direction + 2
        if temp_direction > 3:
            temp_direction -= 4 # 3보다 커질 경우 다시 0, 1로 돌려 놓음

        move_pos = [pos[0] + steps[temp_direction][0], pos[1] + steps[temp_direction][1]]

        # 게임판 밖으로 나간 경우
        if move_pos[0] < 0 or move_pos[0] >= map_size[0] or move_pos[1] < 0 or move_pos[1] >= map_size[1]:
            break

        # 뒤로 간 곳이 바다인 경우
        if map_data[move_pos[0]][move_pos[1]] == 1:
            break

        # 그렇지 않을 경우, 뒤로 한 칸 이동한 걸 pos에 업데이트 해줌
        pos = move_pos

        cnt = 0

print(visit_cnt)