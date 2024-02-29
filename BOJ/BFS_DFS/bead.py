# BOJ 13460, 구슬 탈출 2
import sys, copy
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
arr = []
for i in range(n):
    row_data = list(input().rstrip())
    arr.append(row_data)

    # 빨간 구슬과 파란 구슬 위치 저장
    for j, elem in enumerate(row_data):
        if elem == 'R':
            red = (i, j)
        if elem == 'B':
            blue = (i, j)

steps = [(0, -1), (1, 0), (0, 1), (-1, 0)]

# 맵 템플릿(구슬을 제거한 맵)
map_template = [['.'] * m for _ in range(n)] # 템플릿에서 R과 B가 이동하는 위치는 빈칸이 되어야 함으로 '.'으로 초기화
for i in range(n):
    for j in range(m):
        if arr[i][j] != 'R' and arr[i][j] != 'B':
            map_template[i][j] = arr[i][j]


# 탐색을 위한 리스트 초기화 (red_x, red_y, blue_x, blue_y_)
search_lst = [(red[0], red[1], blue[0], blue[1])]
search_cnt = 0
is_break = False # 탈출해야 할 때 True로 변경하는 flag 변수
while search_lst:
    temp_lst = []

    # 한 레벨의 탐색에 대해 cnt를 1 증가
    search_cnt += 1

    # 10보다 커졌다면 -1을 저장 후 탈출
    if search_cnt > 10:
        search_cnt = -1
        break

    # 빨간 공이 해당 레벨에서 이동한 모든 위치를 순회
    for pos in search_lst:
        x, y, bx, by = pos

        # 이 위치에서 이동할 수 있는 모든 방향 탐색
        for step in steps:
            # 맵 템플릿을 활용해 맵 세팅
            temp_map = copy.deepcopy(map_template)
            temp_map[x][y] = 'R'
            temp_map[bx][by] = 'B'

            ##### 파란 공 이동
            blue_break = False
            temp_map[bx][by] = '.'
            mvb_x, mvb_y = bx + step[0], by + step[1]
            while True:
                # 막다른 길이라면 직전 위치에 구슬을 저장
                if temp_map[mvb_x][mvb_y] == '#' or temp_map[mvb_x][mvb_y] == 'R':
                    mvb_x, mvb_y = mvb_x - step[0], mvb_y - step[1]
                    temp_map[mvb_x][mvb_y] = 'B'
                    break
                # 파란 구슬이 구멍을 만나면 해당 탐색은 실패
                elif temp_map[mvb_x][mvb_y] == 'O':
                    blue_break = True
                    break
                # 갈 수 있는 길이라면, 한 칸 더 감
                else:
                    mvb_x, mvb_y = mvb_x + step[0], mvb_y + step[1]

            if blue_break: # 파란 구슬이 탈출했다면 해당 이동은 무시
                continue

            ##### 빨간 공 이동
            temp_map[x][y] = '.'
            mv_x, mv_y = x + step[0], y + step[1]

            while True:
                # 막다른 길이라면 직전 위치에 구슬을 저장
                if temp_map[mv_x][mv_y] == '#' or temp_map[mv_x][mv_y] == 'B':
                    mv_x, mv_y = mv_x - step[0], mv_y - step[1]
                    temp_map[mv_x][mv_y] = 'R'
                    break
                # 빨간 구슬이 구멍을 만나면 탈출 플래그를 True로 변경한 뒤 탈출
                elif temp_map[mv_x][mv_y] == 'O':
                    is_break = True
                    break
                # 갈 수 있는 길이라면, 한 칸 더 감
                else:
                    mv_x, mv_y = mv_x + step[0], mv_y + step[1]

            ##### 파란 공 이동 (빨간 공 이동 후 추가로 이동 가능할 경우 고려)
            temp_map[mvb_x][mvb_y] = '.'
            mvb_x, mvb_y = mvb_x + step[0], mvb_y + step[1]
            while True:
                # 막다른 길이라면 직전 위치에 구슬을 저장
                if temp_map[mvb_x][mvb_y] == '#' or temp_map[mvb_x][mvb_y] == 'R':
                    mvb_x, mvb_y = mvb_x - step[0], mvb_y - step[1]
                    temp_map[mvb_x][mvb_y] = 'B'
                    break
                # 파란 구슬이 구멍을 만나면 해당 탐색은 실패
                elif temp_map[mvb_x][mvb_y] == 'O':
                    blue_break = True
                    break
                # 갈 수 있는 길이라면, 한 칸 더 감
                else:
                    mvb_x, mvb_y = mvb_x + step[0], mvb_y + step[1]

            ##### 탈출 플래그 확인
            if blue_break:
                is_break = False # 파란공이 탈출했다면 무용지물
                continue

            # 탈출 플래그가 True면 탈출
            if is_break:
                break

            # x, y, bx, by 중 하나라도 움직였다면(기존 위치가 아니라면) 큐에 저장하여 추가 탐색
            if mv_x != x or mv_y != y or mvb_x != bx or mvb_y != by:
                temp_lst.append((mv_x, mv_y, mvb_x, mvb_y))

        # 탈출 플래그가 True면 탈출
        if is_break:
            break

    # 탈출 플래그가 True면 탈출
    if is_break:
        break

    # search_lst를 업데이트
    search_lst = temp_lst

    # search_lst가 비었다면, 구슬이 탈출할 수 있는 추가적인 탐색이 불가능함으로, -1을 출력
    if not search_lst:
        search_cnt = -1
        break

print(search_cnt)