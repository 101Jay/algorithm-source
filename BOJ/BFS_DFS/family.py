# BOJ 2644, 촌수계산
import sys
from collections import deque
input = sys.stdin.readline

def find_rel(t1, t2, t1_num, t2_num, rel_dict):
    # 이 함수에 들어오는 과정에서 이미 동일한 친척 관계임은 가정하고 들어감

    # 깊이가 서로 동일할 때
    if t1_num == t2_num:
        # 부모를 거슬러 올라가며, 동일한 부모가 나올 때까지 확인
        t1_p = rel_dict[t1]
        t2_p = rel_dict[t2]

        # cnt를 체크하여 얼마나 위로 올라가야 동일한 부모인지 확인
        cnt = 1
        while t1_p != t2_p:
            t1_p = rel_dict[t1_p]
            t2_p = rel_dict[t2_p]
            cnt += 1

        # 올라간 만큼 동일하게 내려와주면 해당 값이 촌수
        return 2 * cnt

    # 깊이가 서로 다를 때
    else:
        # 아래로 더 많이 내려간 노드를 위로 끌어 올리며 카운트
        cnt = 0
        if t1_num > t2_num:
            # min_num = t2_num
            while t1_num > t2_num:
                t1 = rel_dict[t1]
                t1_num -= 1
                cnt += 1
        else:
            # min_num = t1_num
            while t2_num > t1_num:
                t2 = rel_dict[t2]
                t2_num -= 1
                cnt += 1

        # 동일한 레벨로 맞춰 놓았는데, 만약 두 노드가 동일하다면 올라가는 와중에 부모가 있는 것임으로 올라간 횟수만 리턴해주면 됨
        if t1 == t2:
            return cnt

        # 동일한 레벨로 맞춰 놓은 상태에서, 얼마나 위로 올라가야 동일한 부모인지 확인
        up_cnt = 0
        while t1 != t2:
            t1 = rel_dict[t1]
            t2 = rel_dict[t2]
            up_cnt += 1

        # 올라간 횟수와 두 노드 중 레벨이 높았던 노드까지 간 거리를 더해줌
        return cnt + up_cnt * 2

def bfs(graph, visited, cur_node):

    # 현재 노드 방문 처리
    visited[cur_node] = 0

    # queue 생성
    queue = deque([cur_node])

    # 탐색해가며 visited 리스트에 탐색 횟수를 저장
    while queue:
        target = queue.popleft()

        # 자식 노드가 없다면 다음 순서로
        if target not in graph:
            continue

        node_lst = graph[target]
        for node in node_lst:
            visited[node] = visited[target] + 1
            queue.append(node)

n = int(input().rstrip())
t1, t2 = map(int, input().rstrip().split())
m = int(input().rstrip())

# 촌수 관계 정보를 dictionary에 저장
relationship = {}
rev_rel = {}
for _ in range(m):
    parent, son = map(int, input().rstrip().split())
    if parent not in relationship:
        relationship[parent] = []

    relationship[parent].append(son)
    rev_rel[son] = parent

answer = -1
visited = [-1] * (n+1)

for i in range(n):
    # 해당 탐색 과정에서 최상위 노드 찾기
    target = i + 1
    while target in rev_rel:
        target = rev_rel[target]

    # 이미 방문한 노드라면 건너뜀
    if visited[target] != -1:
        continue

    bfs(relationship, visited, target)

    # 둘 다 방문 되었다면
    if visited[t1] != -1 and visited[t2] != -1:
        answer = find_rel(t1, t2, visited[t1], visited[t2], rev_rel)
        break
    # 둘 중 하나만 방문 되었다면
    elif visited[t1] != -1 or visited[t2] != -1:
        # -1을 리턴하게 됨
        break

    # 위의 조건에 걸리지 않았다면, 위와 같은 탐색을 반복

print(answer)