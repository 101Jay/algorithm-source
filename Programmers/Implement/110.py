# Programmers 77886, 110 옮기기
from collections import deque
def solution(s):
    answer = []

    for target in s:
        if len(target) <= 3:
            # 행동을 할 수 없음으로 그대로 담기
            answer.append(target)
            continue

        cnt = 0
        # 110을 몇 번 뺄 수 있는지 구하기
        temp_target = deque(list(target))

        rest = []
        comp_lst = deque([])
        comp_lst.append(temp_target.popleft())
        comp_lst.append(temp_target.popleft())

        correct_queue = deque(['1', '1', '0'])

        while temp_target:
            if len(comp_lst) == 3:
                rest.append(comp_lst.popleft())
            comp_lst.append(temp_target.popleft())

            if comp_lst == correct_queue:
                cnt += 1

                # 남은 문자열로 다시 비교하기 위해 세팅
                comp_lst = deque([])
                for _ in range(2):
                    if rest:
                        comp_lst.appendleft(rest.pop())  # rest에서 가져온 건 앞으로 추가

                # comp_lst가 얼마나 차있는지에 따라서 처리
                if len(comp_lst) == 0:
                    for _ in range(2):
                        if temp_target:  # temp_target에거 가져온 건 뒤로 추가
                            comp_lst.append(temp_target.popleft())
                elif len(comp_lst) == 1:
                    if temp_target:
                        comp_lst.append(temp_target.popleft())

                # 그런데도 comp_lst가 2가되지 않았다면 더이상 비교 불가
                if len(comp_lst) != 2:
                    break

        # 110이 없는 문자열이라면 해당 내역을 저장하고 탈출
        if cnt == 0:
            answer.append(target)
            continue

        # 110을 모두 제거한 문자열에서 가장 마지막 0 뒤에 넣어주는 방식
        tg = rest + list(comp_lst) + list(temp_target)

        if tg:
            is_append = False
            for i in range(len(tg) - 1, -1, -1):
                if tg[i] == '0':
                    ans = "".join(tg[:i + 1]) + ('110' * cnt) + "".join(tg[i + 1:])
                    is_append = True
                    break

            if not is_append:
                # 0이 없는 경우 -> 맨 앞에 넣어줌
                ans = '110' * cnt + "".join(tg)
        else:
            # 만약 tg가 비어있다면
            ans = '110' * cnt

        answer.append(ans)

    return answer