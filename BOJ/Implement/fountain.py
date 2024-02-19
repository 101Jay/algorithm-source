# BOJ 1193, 분수찾기
import sys
input = sys.stdin.readline

n = int(input().rstrip())

num_tup = [1, 1]
direction = True # 오른쪽
cur_side = 1
cross_side = 0

cnt = 1
while cnt < n:

    # 반대 방향이 1이 되었는지 확인
    if num_tup[cross_side] == 1:
        num_tup[cur_side] += 1
        # 방향 전환
        direction = not direction
        if cur_side == 1:
            cur_side = 0
            cross_side = 1
        else:
            cur_side = 1
            cross_side = 0
        cnt += 1
        continue

    # 남은 스텝의 수가 반대 방향의 수를 1로 만드는데 필요한 수보다 크다면, 반대 방향이 1이 되도록 한 번에 빼버림
    if num_tup[cross_side] - 1 <= (n - cnt):
        num_tup[cur_side] += (num_tup[cross_side] - 1)
        cnt += (num_tup[cross_side] - 1)
        num_tup[cross_side] = 1

    # 그렇지 않다면, 방향에 맞춰 기본 이동
    num_tup[cur_side] += 1
    num_tup[cross_side] -= 1
    cnt += 1

# 포맷에 맞춰 출력
print(str(num_tup[0]) + "/" + str(num_tup[1]))