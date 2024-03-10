# BOJ 1966, 프린터 큐
import sys
from collections import deque
input = sys.stdin.readline

answers = []
tc = int(input().rstrip())
for _ in range(tc):
    n, t_pos = map(int, input().rstrip().split())
    arr = deque(list(map(int, input().rstrip().split())))

    # 타겟의 중요도 저장
    tg = arr[t_pos]

    cnt = 0
    while arr:
        max_node = max(arr)
        cur_node = arr.popleft()

        # max_node라면, cnt 증가
        if cur_node == max_node:
            cnt += 1
        # max_node가 아니라면 다시 넣어중
        else:
            arr.append(cur_node)

        # 타겟 노드가 max_node이고, 그것이 현재 노드였다면 break
        if max_node == tg and t_pos == 0:
            break

        # target의 위치 재조정
        t_pos -= 1
        if t_pos < 0:
            t_pos = len(arr) - 1

    # 정답 저장
    answers.append(cnt)

for answer in answers:
    print(answer)