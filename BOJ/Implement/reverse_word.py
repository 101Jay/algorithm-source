# BOJ 17413, 단어 뒤집기
import sys
from collections import deque
input = sys.stdin.readline

data = deque(list(input().rstrip()))

result = ""
temp = ""
while data:
    ch = data.popleft()

    # 태그일 때
    if ch == "<":
        # ">" 나올 때까지 계속 저장
        result += ch
        while ch != ">":
            ch = data.popleft()
            result += ch

    # 단어일 때
    else:
        # 공백이나 다음 태그가 나오거나 data가 끝날 때까지 단어를 temp에 담고, 이를 뒤집어서 저장
        temp += ch
        while ch != " " and ch != "<" and data: # 문자열 끝에는 공백이 안나온다는 점을 고려하여 data가 끝나면 종료
            ch = data.popleft()

            # 새로운 태그가 시작했다면 그것은 더하지 않고 다시 넣어줌
            if ch == "<":
                data.appendleft(ch)
                continue

            temp += ch

        # temp에서 공백 제거 후 뒤집기
        temp = temp.strip() # string은 immutable임으로 다시 할당
        temp = temp[::-1]

        # 뒤에가 태그가 아닐 때만 공백을 더해줌
        if ch != "<":
            temp += " "

        # 뒤집어서 result에 저장
        result += temp

        # temp 초기화
        temp = ""

# 마지막에 공백이 더해질 수 있음으로 최종적으로 공백 제거
print(result.strip())