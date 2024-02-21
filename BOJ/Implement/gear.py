# BOJ 14891, 톱니바퀴
import sys
from collections import deque
input = sys.stdin.readline

def gear_rotate(gear, direction):
    if direction == 1:
        # 시계 방향 회전
        end = gear.pop()
        gear.appendleft(end)
    else:
        # 반시계 방향 회전
        start = gear.popleft()
        gear.append(start)

def need_rotate(t1, t2):
    if t1[2] == t2[6]:
        # 회전하지 않음
        return False
    return True

def rev_dir(direct):
    if direct == 1:
        return -1
    return 1

# 톱니 데이터 입력 받기
gears = []
for _ in range(4):
    data = deque(list(map(int,list(input().rstrip()))))
    gears.append(data)

k = int(input().rstrip())

# k번 반복하며 회전 명령을 수행
for _ in range(k):
    num, direct = map(int, input().rstrip().split())
    cur_gear = num - 1 # 인덱스로 변경

    # 회전해야할 요소들과, 방향을 저장한 배열
    temp_rotate = [(cur_gear, direct)]

    left, right = cur_gear - 1, cur_gear + 1

    # 양쪽으로 펼쳐가며 각 톱니들이 회전해야 하는지 판단
    while left >= 0 or right <= 3:
        # 만약 회전해야 한다면 지금의 방향과 반대가 되어야 함으로 방향을 바꿔줌
        direct = rev_dir(direct)

        # 왼쪽으로 가는 범위를 벗어나지 않았을 때
        if left >= 0:
            # 회전해야 한다면
            if need_rotate(gears[left], gears[left+1]):
                temp_rotate.append((left, direct))
                left -= 1
            # 회전하지 않아도 된다면
            else:
                # -1로 설정하여 해당 방향은 더 이상 회전하지 않도록 함
                left = -1

        # 오른쪽으로 가는 범위를 벗어나지 않았을 때
        if right <= 3:
            # 회전해야 한다면
            if need_rotate(gears[right-1], gears[right]):
                temp_rotate.append((right, direct))
                right += 1
            # 회전하지 않아도 된다면
            else:
                # 4로 설정하여 더 이상 회전하지 않도록 함
                right = 4

    # 회전해야 할 것들을 한 번에 회전
    for tup in temp_rotate:
        i, direction = tup
        gear_rotate(gears[i], direction)

# 출력 형식에 맞게 출력
more_point = 1
result = 0
for gear in gears:
    result += gear[0] * more_point
    more_point *= 2

print(result)