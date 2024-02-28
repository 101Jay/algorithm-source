# BOJ 21608, 상어 초등학교
import sys
N_INF = int(1e9) * -1
input = sys.stdin.readline

n = int(input().rstrip())
students = []
favorites = {}
for _ in range(n ** 2):
    tg, t1, t2, t3, t4 = map(int, input().rstrip().split())
    students.append(tg)
    favorites[tg] = [t1, t2, t3, t4]

# 각 자리에 앉을 사람의 번호를 저장할 n x n의 이차원 배열, -1로 초기화
room = [[-1] * n for _ in range(n)]

# 이미 앉은 사람들을 저장할 리스트 (사람, x, y) 형태로 저장
sitted = []

# 인접 거리는 상,하,좌,우 임으로 갈 수 있는 스텝을 미리 선언
steps = [
    (0, -1),
    (1, 0),
    (0, 1),
    (-1, 0)
]

# 자리에 앉을 순서대로 학생들을 순회
for student in students:
    # 좋아하는 학생 목록 구함
    fav = favorites[student]

    # 좋아하는 학생 중 이미 자리에 앉은 목록을 구함
    fav_sit = [] # (사람, x, y) 형태
    for s in sitted:
        if s[0] in fav:
            fav_sit.append(s)

    # 카운팅용 맵 선언
    temp_map = [[0] * n for _ in range(n)]

    # 효율적인 탐색을 위해, 한 번 이상 카운팅 된 위치를 저장하는 리스트 (x, y) 형태
    temp_max = []

    # 좋아하는 학생들 중 자리에 앉은 학생들이 있을 때만 수행
    if fav_sit:
        # 좋아하는 학생들 위치를 순회하며, 해당 위치와 인접한 위치의 temp_map 값을 1씩 더해줌
        for fv in fav_sit:
            name, x, y = fv

            # 모든 갈 수 있는 방향 탐색
            for step in steps:
                mv_x, mv_y = x + step[0], y + step[1]

                # 범위를 넘지 않는지 탐색
                if mv_x < 0 or mv_x >= n or mv_y < 0 or mv_y >= n:
                    continue

                # 해당 위치가 비어있지 않으면 앉을 수 없음으로 배제
                if room[mv_x][mv_y] != -1:
                    continue

                # count 1 증가
                temp_map[mv_x][mv_y] += 1

                # 한 번 이상 증가된 위치 저장
                temp_max.append((mv_x, mv_y))

        # 한 번이라도 선택 받은 위치들을 대상으로, 인접거리에 좋아하는 학생의 수가 가장 많은 값을 구함
        max_val = N_INF
        for tup in temp_max:
            value = temp_map[tup[0]][tup[1]]
            if value > max_val:
                max_val = value

        fav_sit = [] # (x, y)
        # 다시 순회하며, max_val를 가진 위치를 fav_sit에 저장 (max_val 0이라는 것은 해당하는 자리가 없다는 뜻임으로 빈 배열로 나감)
        if max_val != 0:
            for tup in temp_max:
                if temp_map[tup[0]][tup[1]] == max_val:
                    fav_sit.append((tup[0], tup[1]))

    final_sit = [] # (x, y)
    # fav_sit이 비어있다면 -> 즉, 좋아하는 학생이 인접한 칸이 없다는 것
    # 따라서 모든 위치 중 인접거리에 빈칸의 개수가 가장 많은 곳을 구함
    if not fav_sit:
        temp_arr = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                # 배치 가능한 위치에 대해서만 구함
                if room[i][j] != -1:
                    continue

                # 모든 가능한 이동거리에 대해서 인접거리를 구함
                for step in steps:
                    mv_i, mv_j = i+step[0], j+step[1]

                    # 이동할 수 없는 범위는 무시
                    if mv_i < 0 or mv_i >= n or mv_j < 0 or mv_j >= n:
                        continue

                    # 해당 위치로부터 인접거리의 칸이 비어있다면 해당 위치의 카운트 값 1 증가
                    if room[mv_i][mv_j] == -1:
                        temp_arr[i][j] += 1

        # 모든 배치 가능한 위치에 대해 temp_arr에서 가장 큰 카운트 값을 구함
        max_val = N_INF
        for row in temp_arr:
            val = max(row)
            if val > max_val:
                max_val = val

        # max_val가 0이라면, 모든 위치에 대해 인접거리 안에 빈칸이 없다는 의미임으로, 그냥 빈칸을 찾아 final_sit에 저장
        if max_val == 0:
            for i in range(n):
                for j in range(n):
                    if room[i][j] == -1:
                        final_sit.append((i,j))
        # 그렇지 않다면, 가장 큰 카운트 값을 가지고 있는 위치를 final_sit에 저장
        else:
            for i in range(n):
                for j in range(n):
                    if temp_arr[i][j] == max_val:
                        final_sit.append((i, j))

    # fav_sit에 하나만 있다면, 그대로 final_sit으로 저장
    elif len(fav_sit) == 1:
        final_sit = fav_sit

    # 인접거리에 좋아하는 학생이 가장 많은 자리들이 여러개라면, 그 자리들만을 대상으로 인접거리의 빈칸의 개수가 가장 많은 자리들을 구함
    else:
        temp_arr = [[0] * n for _ in range(n)]
        for tup in fav_sit:
            i, j = tup
            # 모든 가능한 이동거리에 대해서 인접거리를 구함
            for step in steps:
                mv_i, mv_j = i + step[0], j + step[1]

                # 이동할 수 없는 범위는 무시
                if mv_i < 0 or mv_i >= n or mv_j < 0 or mv_j >= n:
                    continue

                # 인접거리의 칸이 비어있다면 원래의 위치에 카운트를 증가
                if room[mv_i][mv_j] == -1:
                    temp_arr[i][j] += 1

        # 모든 배치 가능한 위치에 대해 temp_arr에서 가장 큰 카운트 값을 구함
        max_val = N_INF
        for row in temp_arr:
            val = max(row)
            if val > max_val:
                max_val = val

        # 가장 큰 카운트 값을 가지고 있는 위치를 final_sit에 저장
        for tup in fav_sit:
            i, j = tup
            if temp_arr[i][j] == max_val:
                final_sit.append((i, j))

    # final_sit을 행, 열 순으로 정렬
    final_sit.sort(key=lambda x : (x[0], x[1]))

    # 저장
    final_x, final_y = final_sit[0]
    room[final_x][final_y] = student
    sitted.append((student, final_x, final_y))

# 만족도의 총합 구하기
point = 0
for i in range(n):
    for j in range(n):
        tg = room[i][j] # 해당 번호 구하기
        tg_lst = favorites[tg] # 좋아하는 번호 리스트 구하기

        satisfied = 0
        # 옮길 수 있는 모든 이동 위치를 순회
        for step in steps:
            mv_i, mv_j = i+step[0], j+step[1]

            if mv_i < 0 or mv_i >= n or mv_j < 0 or mv_j >= n:
                continue

            # 인접 위치가 좋아하는 사람이라면 카운트 값 증가
            if room[mv_i][mv_j] in tg_lst:
                satisfied += 1

        # 좋아하는 사람의 수에 따라 다르게 점수 측정
        if satisfied == 1:
            point += 1
        elif satisfied == 2:
            point += 10
        elif satisfied == 3:
            point += 100
        elif satisfied == 4:
            point += 1000

print(point)