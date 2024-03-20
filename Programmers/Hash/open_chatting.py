# Programmers 42888, 오픈채팅방(2019 카카오 블라인드 채용)
def solution(record):
    answer = []

    # 1. record를 순회하며 dictionary 생성
    rec_dict = {}
    for sen in record:
        sen = sen.split()

        # Leave는 dict를 변경하지 않음으로 스킵
        if sen[0] == 'Leave':
            continue

        # uid에 해당하는 닉네임 업데이트
        rec_dict[sen[1]] = sen[2]

    # 2. record를 순회하며 출력문 생성
    for sen in record:
        sen = sen.split()

        # 조건에 따라 출력문 생성
        word = ""
        if sen[0] == 'Enter':
            word = "님이 들어왔습니다."
        elif sen[0] == 'Leave':
            word = "님이 나갔습니다."
        else:
            continue  # Change라면 출력문 생성하지 않음

        answer.append(rec_dict[sen[1]] + word)

    return answer