# BOJ 2161, 카드1
import sys
from collections import deque
input = sys.stdin.readline

n = int(input().rstrip())

queue = deque([x for x in range(1, n+1)])

result = []
while len(queue) > 1:
    # 버릴 카드 뽑기
    tg1 = queue.popleft()
    result.append(tg1)

    # 남은 카드가 1장이면 종료
    if len(queue) == 1:
        result.append(queue.popleft())
        break

    # 아래로 넣을 카드를 뽑은 뒤 아래에 넣기
    tg2 = queue.popleft()
    queue.append(tg2)

if not result:
    # result가 비어있다면, n은 1임으로 1추가
    result.append(1)

# 출력 형식에 맞게 출력
result_size = len(result) - 1
for i, elem in enumerate(result):
    if i == result_size:
        print(elem, end="")
    else:
        print(elem, end=" ")