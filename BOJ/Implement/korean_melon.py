# BOJ 2477, 참외밭
import sys
input = sys.stdin.readline

melon_num = int(input().rstrip())

arr = []
# 가로, 세로 길이
horizontal, vertical = 0, 0
for _ in range(6):
    direction, length = map(int, input().rstrip().split())
    if direction == 2:
        # 서쪽 방향의 모든 것을 더함 -> 가로
        horizontal += length
    elif direction == 4:
        # 북쪽 방향의 모든 것을 더함 -> 세로
        vertical += length
    arr.append((direction, length))

# 끊어지지 않은 세로 변, 가로 변의 방향
ver_dir, hor_dir = 0, 0

for side in arr:
    direction, length = side

    # 세로 변 중 끊어지지 않은 방향 찾기(해당 변의 길이만으로 세로 길이를 모두 차지할 수 있는 것)
    if (direction == 4 or direction == 3) and length == vertical:
        ver_dir = direction

    # 가로 변 중 끊어지지 않은 방향 찾기(해당 변의 길이만으로 가로 길이를 모두 차지할 수 있는 것)
    if (direction == 1 or direction == 2) and length == horizontal:
        hor_dir = direction

side = []
# 잘려 나간 변의 길이들은 항상 끼어있다는 점을 활용해, 앞뒤로 모두 ver_dir이나 hor_dir이 아닐 경우의 변의 길이를 찾음
for i in range(6):
    backward = i - 1
    forward = i + 1

    # i가 마지막 인덱스일 때 앞 방향의 인덱스를 조절
    if i == 5:
        forward = 0

    if arr[i][0] != ver_dir and arr[i][0] != hor_dir:
        # 끊기지 않은 변들과 인접하지 않은 변 찾기
        if arr[backward][0] != ver_dir and arr[backward][0] != hor_dir and arr[forward][0] != ver_dir and arr[forward][0] != hor_dir:
            side.append(arr[i][1])

result = (horizontal * vertical - side[0] * side[1]) * melon_num
print(result)