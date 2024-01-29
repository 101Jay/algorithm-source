# BOJ 11000, 강의실 배정
# 그리디

import sys
from queue import PriorityQueue
import heapq
input = sys.stdin.readline

size = int(input())
pq = PriorityQueue()

for _ in range(size):
    pq.put(tuple(map(int, input().split())))

# 우선순위 큐는 자동으로 튜플의 첫 번째 원소 기준으로 정렬
class_num = []
heapq.heappush(class_num, pq.get()[1])

for _ in range(size-1):

    cur_val = pq.get() # 현재 수업
    tg = class_num[0] # classroom에 있는 원소의 종료시간 중 가장 작은 것
    if(cur_val[0] >= tg):
        # 수업이 들어갔다면, 기존의 가장 작았던 종료시간을 pop하고 대신 현재 수업의 종료시간을 추가 (즉, 해당 강의실의 종료시간을 연장한 셈)
        heapq.heappop(class_num)
        heapq.heappush(class_num, cur_val[1])
    else:
        # 만약 들어가고자 하는 수업의 시작시간이 여러 classroom의 가장 작은 종료시간 보다 작다면, 무조건 새로운 강의실을 만들어야 함
        # pop하는 것 없이 새롭게 put (강의실 추가되는 셈)
        heapq.heappush(class_num, cur_val[1])

print(len(class_num))