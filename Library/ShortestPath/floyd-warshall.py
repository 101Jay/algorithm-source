# 모든 노드에서 모든 노드로 가는 최단 경로를 구하기 위한 Floyd-Warshall 알고리즘
import sys
input = sys.stdin.readline 
INF = int(1e9)

# 노드 및 간선의 개수
n, m = map(int, input().rstrip().split())

# 2차원 리스트 생성 및 무한으로 초기화
graph = [[INF] * (n+1) for _ in range(n+1)] # (n+1) * (n+1) 이차원 리스트 생성

# 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

# 간선 정보 입력
for _ in range(m):
    # a -> b로 가는 비용 c
    a, b, c = map(int, input().rstrip().split())
    graph[a][b] = c

# Floyd-Warshall algorithm
for k in range(1, n+1):
    # k : n개의 노드 선택
    # k를 제외한 나머지 n-1개의 노드에서 2개의 노드를 선택하는 것이 맞지만,
    # 아래와 같이 반복문을 돌려도 k를 포함한다거나 동일한 노드끼리 선택되는 경우에는
    # 점화식이 아무런 영향을 미치지 못함으로 아래와 같이 간단하게 수행
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 결과 출력
for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print("INFINITY", end=" ")
        else:
            print(graph[a][b], end=" ")
    print() # 한 칸 띔

'''
입력 예시
4 7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2
---
출력 예시
0 4 8 6 
3 0 7 9 
5 9 0 4 
7 11 2 0 
'''