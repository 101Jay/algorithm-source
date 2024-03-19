# Programmers 118667, 두 큐 합 같게 만들기
from collections import deque
def solution(queue1, queue2):
    answer = -1

    # 1. 두 큐의 합을 구한 뒤 각 큐의 목표 값을 구함
    sum_val = sum(queue1) + sum(queue2)
    # 만약 2로 나누어 떨어지지 않는다면 목표 달성 불가 -> -1 반환
    if sum_val % 2 != 0:
        return answer

    target_val = sum_val // 2

    # 2. 각 큐의 합이 같아질 때까지 반복
    repeat_limit = len(queue1) * 2 + 1 # 같게 만들 수 있는 경우 중 최대 반복 횟수로 가정

    q1 = deque(queue1)
    q2 = deque(queue2)

    answer += 1  # 0으로 만들어 줌
    q1_sum = sum(q1)
    q2_sum = sum(q2)
    while q1_sum != target_val and answer <= repeat_limit:

        if q1_sum > q2_sum:  # q1이나 q2가 비어있는 경우는 여기서 걸러짐
            # q1에서 하나 빼서 q2로 넣기
            q1_out = q1.popleft()
            q2.append(q1_out)

            # q1_sum, q2_sum 업데이트
            q1_sum -= q1_out
            q2_sum += q1_out
        else:
            # q2에서 하나 빼서 q1으로 넣기
            q2_out = q2.popleft()
            q1.append(q2_out)

            # q1_sum, q2_sum 업데이트
            q1_sum += q2_out
            q2_sum -= q2_out

        answer += 1

    # 3. 둘이 같아져서 끝난 것이 아니라면 answer = -1로 바꿔줌
    if q1_sum != target_val:
        answer = -1

    return answer