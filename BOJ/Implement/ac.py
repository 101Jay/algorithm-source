# BOJ 5430, AC
import sys, re
from collections import deque
input = sys.stdin.readline

test_num = int(input().rstrip())

result = []
for _ in range(test_num):
    stmt = deque(list(input().rstrip()))
    lst_size = int(input().rstrip())
    lst_str = input().rstrip()

    # '[1,2,3,4]'로 구성된 문자열에서 숫자만을 파싱
    lst = re.findall(r'\d+', lst_str)
    lst = deque([int(x) for x in lst])

    # 가장 앞 원소를 제거하는 방향으로 초기화
    que_dir = True

    while stmt:
        tg = stmt.popleft()

        # Reverse일 때
        if tg == "R":
            # 삭제하는 방향 변경
            que_dir = not que_dir

        # Delete일 때
        else:
            # 비어있을 때 해당 문자열이 수행되면 error
            if not lst:
                lst = 'error'
                break
            else:
                if que_dir:
                    # 가장 앞 문자 제거
                    lst.popleft()
                else:
                    # 가장 뒷 문자 제거
                    lst.pop()

    # deque를 list로 변경하여 저장
    if lst != 'error':
        # 반대 방향으로 되어있다면, 리스트를 반대 방향으로 바꿔줌
        if not que_dir:
            answer = list(lst)[::-1]
        else:
            answer = list(lst)

        # 최종 리스트를 출력 형식에 맞게 공백 없는 리스트 문자열로 변환
        answer_str = "["
        for i, elem in enumerate(answer):
            if i != 0:
                answer_str += ','
            answer_str += str(elem)

        answer_str += "]"

        result.append(answer_str)
    else:
        result.append(lst)

# 결과를 모두 확인한 뒤 출력
for elem in result:
    print(elem)