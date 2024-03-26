# Programmers 92334, 신고 결과 받기
def solution(id_list, report, k):
    answer = []

    # 1. {신고당한사람 : 신고한 사람들 list} 형태의 dictionary 생성
    report_dict = {}
    for elem in report:
        elem = elem.split()
        if elem[1] not in report_dict:
            report_dict[elem[1]] = []

        # 동일 인물이 또 신고했다면 스킵
        if elem[0] not in report_dict[elem[1]]:
            report_dict[elem[1]].append(elem[0])

    # 2. {신고한 사람 : 메일 발송 횟수} 형태로 dictionray 생성
    final_dict = {}
    for key, value in report_dict.items():
        # value(리스트)의 길이가 k이상인 경우만 고려
        if len(value) < k:
            continue

        # 신고한 사람들 리스트를 순회하며 final_dict 값 할당
        for p in value:
            if p not in final_dict:
                final_dict[p] = 0
            final_dict[p] += 1

    # 3. id_list를 순회하며 순서에 맞춰 메일 발송 횟수를 answer에 추가
    for id in id_list:
        # final_dict에 없다면 0을 할당
        if id not in final_dict:
            answer.append(0)
            continue

        answer.append(final_dict[id])

    return answer