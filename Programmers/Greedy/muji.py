# 프로그래머스 42891, 무지의 먹방 라이브
import heapq, copy

def solution(food_times, k):
    length = len(food_times)
    arr = copy.deepcopy(food_times)
    heapq.heapify(arr)

    pop_cnt = 0
    share_acc = 0
    remainder = -1

    while k >= 0:

        # 음식 종류 개수 (food_type) 업데이트
        food_type = length - pop_cnt

        # k가 1보다 큰 상태에서 먹을 음식이 남지 않았다면 탈출
        if food_type <= 0:
            break

        # 최솟값 업데이트
        elem = heapq.heappop(arr)
        pop_cnt += 1

        success_cnt = 1
        if arr and elem == arr[0]:
            # elem이 다음 원소와 동일하다면 계속 pop
            while arr and elem == arr[0]:
                elem = heapq.heappop(arr)
                pop_cnt += 1
                success_cnt += 1

        # k를 남은 음식의 종류 수로 나눈 몫과 elem 중 작은 값을 선택
        share = min(k // food_type, elem - share_acc)
        if share < (elem - share_acc):
            # 다시 해당 원소를 다시 넣어줘야 함
            # 연속해서 빼줬다면 그만큼 다시 채워 넣어야 함
            while success_cnt > 0:
                heapq.heappush(arr, elem)
                pop_cnt -= 1
                success_cnt -= 1

        share_acc += share

        if share >= 1:
            # 먹은만큼 k의 값 줄이기
            k -= share * (food_type)

        else:
            # 더 이상 순회 불가 -> remainder 설정 후 탈출
            remainder = k
            break

    # 먹을 음식이 다 떨어진 상황
    if remainder == -1:
        return -1

        # elem 보다 작은 것들은 고려하지 않고, 큰 것들을 remainder 만큼 돌면서 먹을 위치 파악
    for i in range(length):
        if food_times[i] < elem:
            continue

        if remainder == 0:
            return i + 1

        remainder -= 1