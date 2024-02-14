import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

# 노드 및 간선의 개수
n, m = map(int, input().rstrip().split())

# 시작 노드
init_node = int(input().rstrip())

# 각 노드에 연결된 다른 노드들을 리스트 형태로 저장
graph = [[] for _ in range(n+1)]

# 최단 거리 테이블 초기화
distance = [INF] * (n+1)

# 간선 정보 입력 받기
for _ in range(m):
    # a -> b로 가는 비용 c
    a, b, c = map(int, input().rstrip().split())
    graph[a].append((b, c))

# dijkstra 알고리즘
def dijkstra(start):
    queue = []

    # 시작 노드로의 최단 경로는 0으로 설정, 큐에 삽입
    # queue에는 (거리, 노드)의 튜플 형태로 저장
    heapq.heappush(queue, (0, start))

    # 시작 노드의 최단 거리는 0으로 설정
    distance[start] = 0

    # queue가 빌 때까지 반복
    while queue:
        # 거리가 가장 짧은 노드 꺼내기
        tg_dist, tg_node = heapq.heappop(queue)

        # distance 속 tg_node의 최단 거리와 비교하여, 최단 거리보다 더 크다면 이미 방문한 노드임으로 건너뜀
        if distance[tg_node] < tg_dist:
            continue

        # tg_node와 연결된 다른 인접 노드들을 확인
        for node, dist in graph[tg_node]:
            # tup은 (노드, 거리) 형태로 되어 있음
            cost = tg_dist + dist

            # 현재 노드를 거쳐서 다른 노드로 가는 것이 더 짧은 경우만 업데이트
            if cost < distance[node]:
                distance[node] = cost
                # 최단 거리로 업데이트 된 정보는 heapq에 다시 넣기
                heapq.heappush(queue, (cost, node))

# 다익스트라 알고리즘 수행
dijkstra(init_node)

# 모든 노드로 가는 최단 거리 출력
for i in range(1, n+1):
    # 도달 가능하지 않은 경우 INFINITY라고 출력
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])
