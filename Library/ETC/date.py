# 기준 날짜에 해당 '달'을 더하는 함수 (한 달은 모두 28일로 가정)
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


# 첫번째 인자와 두번째 인자를 비교하여 두번째가 더 크거나 같으면 True를 반환하는 함수
# 두 인자 모두 [연, 월, 일] 리스트 형태로 입력
def comp_day(first, second):
    # 년, 월, 일 순서대로 비교
    for i in range(3):
        if first[i] > second[i]:
            return False
        elif first[i] < second[i]:  # 유효기간이 더 크다면 보관 가능
            return True
        # 같은 상황이라면 한 번 더 반복

    # 여기까지 안 끝났으면 같다는 의미임으로 보관 가능 -> True
    return True