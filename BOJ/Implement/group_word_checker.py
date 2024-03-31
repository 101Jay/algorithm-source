# BOJ 1316, 그룹 단어 체커
import sys
input = sys.stdin.readline

n = int(input().rstrip())
answer = 0
for _ in range(n):
    # 단어를 리스트로 변경하여 저장
    word = list(input().rstrip())

    before = word[0]
    before_lst = [before]
    for ch in word:
        # 이전 값과 다르다면, 기존에 나왔던 값인지 확인하고 그렇다면 그룹 단어가 아님으로 탈출
        if ch != before:
            if ch in before_lst:
                break
            # 기존에 나오지 않았던 문자라면, before의 값을 변경하고 before_lst에 추가
            before = ch
            before_lst.append(before)
    else: # for문이 모두 정상적으로 실행된 후 실행되는 else문
        # 그룹 단어인 경우 answer 1 증가
        answer += 1

print(answer)