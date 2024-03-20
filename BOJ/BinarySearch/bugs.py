# BOJ 3020, 개똥벌레
import sys
from bisect import bisect_left
INF = int(1e9)
input = sys.stdin.readline

n, h = map(int, input().rstrip().split())
suksuns = []
jongyus = []
for i in range(1, n+1):
    data = int(input().rstrip())
    if i % 2 == 0: # 종유석인 경우
        jongyus.append(h-data)
    else: # 석순인 경우
        suksuns.append(data)

# 정렬 및 사이즈 저장
suksuns.sort()
jongyus.sort()
suksun_size = len(suksuns)
jongyu_size = len(jongyus)

# 해당 구간이 몇 개와 충돌하는지 나타냄
crash = [INF] * (h+1)

for i in range(1, h+1):
    # 석순과 부딪히는 갯수 구하기
    crash_suksun = suksun_size - bisect_left(suksuns, i)
    # 종유석과 부딪히는 갯수 구하기
    crash_jongyu = bisect_left(jongyus, i)

    # crash에 저장
    crash[i] = crash_suksun + crash_jongyu

min_val = min(crash)
min_cnt = 0

for i in range(1, h+1):
    if crash[i] == min_val:
        min_cnt += 1

print(min_val, min_cnt)