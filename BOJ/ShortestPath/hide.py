# BOJ 13549, 숨바꼭질
import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

start, end = map(int, input().rstrip().split())

distance = [INF] * 100001

graph = [[] for _ in range(100001)]

# 0의 경우에는 1 비용을 들여 1로 이동하는 것으로 초기화
graph[0].append((1, 1)) # (목적지 노드, 거리)

# 각 노드에서 갈 수 있는 곳 저장
for i in range(1, 100001):
    # 걸어서 갈 수 있는 곳
    graph[i].append(((i-1), 1))
    if i+1 <= 100000: # 범위를 넘지 않도록 설정
        graph[i].append(((i+1), 1))

    # 순간이동으로 갈 수 있는 곳
    tg = i * 2
    if tg <= 100000:
        graph[i].append((tg, 0))
        # graph[tg].append((i, 0)) -> 순간 이동은 앞의 방향으로만 가능

def dijkstra(start_node):
    queue = []
    heapq.heappush(queue, (0, start_node))
    distance[start_node] = 0

    while queue:
        tg_dist, tg_node = heapq.heappop(queue)

        if distance[tg_node] < tg_dist: # 이미 방문한 노드라면, 건너뜀
            continue

        for node, dist in graph[tg_node]:
            cost = tg_dist + dist
            if cost < distance[node]:
                distance[node] = cost
                heapq.heappush(queue, (cost, node))

dijkstra(start)
print(distance[end])