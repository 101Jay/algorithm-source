# Programmers 118668, 코딩 테스트 공부
from collections import deque
INF = int(1e9)

def solution(alp, cop, problems):
    # 1. 목표치 설정
    t_alp, t_cop = 0, 0
    for problem in problems:
        al, co = problem[0], problem[1]
        if t_alp < al:
            t_alp = al

        if t_cop < co:
            t_cop = co

    # visit의 각 값은 해당 위치로 가는 최소 시간을 의미
    visited = [[INF] * (t_cop + 1) for _ in range(t_alp + 1)]

    # al,co가 처음부터 t_alp와 t_cop보다 크다면 최대값으로 줄임(인덱스 에러 방지)
    if alp > t_alp:
        alp = t_alp

    if cop > t_cop:
        cop = t_cop

    # 2. bfs 탐색
    bfs(problems, (alp, cop), visited, t_alp, t_cop)

    # 3. 목표 위치의 최솟값 출력
    answer = visited[t_alp][t_cop]

    return answer

def bfs(graph, cur_node, visit, t_alp, t_cop):
    # 시작 노드는 0으로 업데이트 업데이트
    al, co = cur_node
    visit[al][co] = 0

    queue = deque([cur_node])

    while queue:
        tg_a, tg_c = queue.popleft()

        # 문제를 풀어서 실력을 늘리는 방식
        for node in graph:
            a_req, c_req, a_rw, c_rw, cost = node
            # 해당 문제를 풀 수 있는 것이라면
            if tg_a >= a_req and tg_c >= c_req:
                # 움직일 위치 업데이트
                mv_a, mv_c = tg_a + a_rw, tg_c + c_rw

                # 만약 mv_a나 mv_c가 범위를 벗어난다면 범위 최대값으로 맞춰줌
                # 범위가 벗어나는 것도 목표 달성임으로 '목표 위치'로 값을 갱신
                if mv_a > t_alp:
                    mv_a = t_alp

                if mv_c > t_cop:
                    mv_c = t_cop

                # 갈 수 있는 위치의 기존 cost 값보다 줄일 수 있다면 방문
                if visit[mv_a][mv_c] > visit[tg_a][tg_c] + cost:
                    visit[mv_a][mv_c] = visit[tg_a][tg_c] + cost
                    # queue에 옮길 위치를 넣어줌
                    queue.append((mv_a, mv_c))

        # 공부해서 실력을 늘리는 방식
        # 1) 알고리즘 공부
        mv_a, mv_c = tg_a + 1, tg_c
        if mv_a > t_alp:  # 범위 벗어나지 않게 조정
            mv_a = t_alp

        if visit[mv_a][mv_c] > visit[tg_a][tg_c] + 1:
            visit[mv_a][mv_c] = visit[tg_a][tg_c] + 1
            # queue에 옮길 위치를 넣어줌
            queue.append((mv_a, mv_c))

        # 2) 코딩 공부
        mv_a, mv_c = tg_a, tg_c + 1
        if mv_c > t_cop:  # 범위 벗어나지 않게 조정
            mv_c = t_cop

        if visit[mv_a][mv_c] > visit[tg_a][tg_c] + 1:
            visit[mv_a][mv_c] = visit[tg_a][tg_c] + 1
            # queue에 옮길 위치를 넣어줌
            queue.append((mv_a, mv_c))