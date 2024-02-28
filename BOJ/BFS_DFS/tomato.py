# BOJ 7576, 토마토
import sys
input = sys.stdin.readline

m, n = map(int, input().rstrip().split())
ripe_tomato = []
raw_tomato = []
visit = [[False] * m for _ in range(n)]

# 지도 정보 입력 받기
arr = []
for i in range(n):
    row_data = list(map(int, input().rstrip().split()))
    arr.append(row_data)
    # 익은 토마토, 안 익은 토마토 따로 저장 및 익은 토마토는 미리 방문 처리
    for j, elem in enumerate(row_data):
        if elem == 1:
            ripe_tomato.append((i, j))
            visit[i][j] = True
        elif elem == 0:
            raw_tomato.append((i, j))

# 안 익은 토마토가 없다면 0을 출력 (토마토는 반드시 하나 이상)
if not raw_tomato:
    print(0)
else:
    # 안 익은 토마토는 있지만, 익은 토마토가 없다면 -> 모두 익을 수 없는 상황
    if not ripe_tomato:
        print(-1)
    else:
        steps = [
            (0, -1),
            (1, 0),
            (0, 1),
            (-1, 0)
        ]

        # 매번 순회하며 다 익었는지를 확인하기 위해 초기의 안 익은 토마토 개수 저장
        raw_size = len(raw_tomato)

        raw_cnt = 0
        day_cnt = 0

        # 해당 레벨에서 추가로 안 익은 토마토가 탐색되지 않을 때까지 수행
        while ripe_tomato:
            day_cnt += 1
            temp_arr = []
            # 익은 토마토의 리스트(ripe_tomato)를 한 단계씩 순회
            for to in ripe_tomato:
                x, y = to

                # 갈 수 있는 모든 방향으로 순회
                for step in steps:
                    mv_x, mv_y = x + step[0], y + step[1]

                    if mv_x < 0 or mv_x >= n or mv_y < 0 or mv_y >= m:
                        continue

                    if not visit[mv_x][mv_y] and arr[mv_x][mv_y] == 0:
                        arr[mv_x][mv_y] = 1 # 익은 것으로 변경
                        visit[mv_x][mv_y] = True
                        raw_cnt += 1
                        temp_arr.append((mv_x, mv_y))

            # 익은 토마토의 개수 비교를 통해 토마토가 모두 익었는지 확인
            if raw_size == raw_cnt:
                break

            # ripe_tomato 업데이트
            ripe_tomato = temp_arr

        # 토마토가 모두 익지 않은 상황에서 탐색이 종료된 것이라면, 더이상 익을 수 없는 상황 -> -1 출력
        if raw_size != raw_cnt:
            print(-1)
        else:
            print(day_cnt)