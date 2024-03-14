# Programmers 150370, 개인정보 수집 유효기간 (2023 카카오 공채)
def solution(today, terms, privacies):
    answer = []

    # [Year, Month, Day]로 변경
    today = list(map(int, today.split(".")))

    for i, priv in enumerate(privacies):
        # 기준 날짜
        fix_day = priv[:-2]

        # 약관 종류
        type = priv[-1]

        # 유효기간 가져오기
        for term in terms:
            if term[0] == type:
                month = int(term[2:])

        # 날짜 더하기
        after_day = plus_month(fix_day, month)

        # 보관 불가능한 날짜를 저장
        if not comp_day(today, after_day):
            answer.append(i + 1)  # 파기해야 함으로 해당 약관의 번호를 저장

    return answer


def plus_month(cur_day, target):
    year, month, day = map(int, cur_day.split("."))

    # 일자 하나 빼기
    day -= 1
    if day == 0:
        day = 28
        month -= 1

        if month <= 0:
            month = 12 - (month * -1)
            year -= 1

    # 달 더하기
    month += target

    # 달이 12가 넘었을 때
    if month > 12:
        if month % 12 == 0:  # edge 케이스가 발생함으로, 별도 처리
            share = month // 12 - 1
            month = 12
        else:
            share = month // 12
            month = month - share * 12

        year += share

    return [year, month, day]


# 보관 가능하다면 True, 불가능하다면 False를 출력하는 함수
def comp_day(today, t_day):
    # 년, 월, 일 순서대로 비교
    for i in range(3):
        if today[i] > t_day[i]:
            return False
        elif today[i] < t_day[i]:  # 유효기간이 더 크다면 보관 가능
            return True
        # 같은 상황이라면 한 번 더 반복

    # 여기까지 안 끝났으면 같다는 의미임으로 보관 가능 -> True
    return True