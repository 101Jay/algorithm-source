# Programmers 92342, 양궁대회
import copy
def solution(n, info):
    ryan = [0] * 11  # 0번째 인덱스가 10점 과녁을 의미
    answer = [[]]  # 내부로 한 번 더 들어가 참조 연산을 통해 함수에서 값을 변경하도록 설정
    max_lst = [0]
    backtrack(n, info, ryan, 0, answer, max_lst)

    if max_lst[0] == 0:
        return [-1]

    return answer[0]


def backtrack(n, apeach, ryan, idx, answer, max_lst):
    # n발 남았음을 의미
    if n == 0:  # 모든 화살을 다 쐈다면 둘 간의 차이를 확인하고 max 값보다 크다면 answer에 해당 ryan을 저장
        get_diff(apeach, ryan, answer, max_lst)

    # 10점부터 시작해 각 과녁의 점수를 ryan이 획득하는 조합 생성, 최댓값 갱신
    for i in range(idx, 11):
        cost = min(n, apeach[i] + 1)  # apeach를 이길 수 있다면 해당 발보다 1발 많이 쏴야 함
        ryan[i] = cost
        backtrack(n - cost, apeach, ryan, i + 1, answer, max_lst)
        ryan[i] = 0  # 원상복구


# 라이언이 이기는 최대의 경우의 수를 찾아내 answer에 저장
def get_diff(apeach, ryan, answer, max_lst):
    score = get_score(apeach, ryan)
    max_val = max_lst[0]

    if max_val < score:  # 기존의 max 값을 갱신, answer도 갱신
        answer[0] = copy.deepcopy(ryan)
        max_lst[0] = score
    elif max_val > 0 and max_val == score:  # 동일하다면 점수가 더 낮은 것을 많이 맞힌 경우를 찾음
        # max_val가 0일 경우 answer[0]이 빈 배열이라는 것임으로 런타임 에러를 방지하기 위한 조건 추가
        for i in range(10, -1, -1):  # 0점부터 10점까지
            # 거꾸로 가려면 step에 -1 줘야함
            if answer[0][i] < ryan[i]:  # ryan이 낮은 점수를 더 많이 맞힌 것
                answer[0] = copy.deepcopy(ryan)
                break
            elif answer[0][i] > ryan[i]:  # answer이 낮은 점수를 더 많이 맞혔다면 이 또한 탈출해줘야 함
                break


# 라이언을 기준으로 점수 구하기
def get_score(apeach, ryan):
    score = 0
    for i in range(11):
        if ryan[i] + apeach[i] > 0:  # 둘 중 하나라도 과녁을 쏜 경우에만 점수를 얻거나 잃음
            if ryan[i] > apeach[i]:
                score += 10 - i
            else:
                score -= 10 - i  # apeach가 이기는 경우

    return score