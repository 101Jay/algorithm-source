# p259, 미래 도시
'''
연결된 도시는 양방향 이동이 가능
1번 -> K번 -> X번 회사로 이동
만약 X번 회사에 도달할 수 없다면 -1을 출력
두 도시 간의 거리는 항상 1로 고정

# 점화식 : Aab = min(Aab, Aak + Akb)

노드의 개수가 최대 100임으로 플루이드-워셜 알고리즘으로 해결 가능
'''
import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드, 간선 개수 입력
n, m = map(int, input().rstrip().split())

# 두 노드 간의 연결 관계를 표현하는 이차원 그래프, 무한으로 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자신으로 가는 거리는 0으로 설정
for a in range(n+1):
    for b in range(n+1):
        if a==b:
            graph[a][b] = 0

# 간선들을 입력 받으면서 거리 1을 할당
for _ in range(m):
    a, b = map(int, input().rstrip().split())
    # 양방향이기 때문에 양쪽 모두에 1씩 할당
    graph[a][b] = 1
    graph[b][a] = 1

# X도시와 K도시 입력
dest, visit = map(int, input().rstrip().split())

# 플루이드-워셜 알고리즘 수행
for k in range(n+1):
    for a in range(n+1):
        for b in range(n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

answer = graph[1][visit] + graph[visit][dest]

if answer >= INF:
    print(-1)
else:
    print(answer)

'''
입력 예시 1
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5
---
출력 : 3

입력 예시 2
4 2
1 3
2 4
3 4
---
출력 : -1
'''