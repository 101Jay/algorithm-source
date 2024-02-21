# BOJ 13458, 시험 감독
import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))
b, c = map(int, input().rstrip().split())

total_num = 0
for a in arr:
    cnt = 0

    # 총감독관 한 명 우선 배치
    a -= b
    cnt += 1

    # a가 음수가 아니라면 더 줄이는 과정 수행
    if a > 0:
        # 이제부턴 부감독관(c)만 배치
        share = a // c
        a -= share * c
        cnt += share

        # 아직 남은 것이 있다면 부감독관을 한 명 더 충원해서 모두 감독할 수 있도록 함
        if a > 0:
            cnt += 1

    # 전체 인원 수에 업데이트
    total_num += cnt
print(total_num)