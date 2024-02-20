# BOJ 14500, 테트로미노
import sys, copy
input = sys.stdin.readline

# 도형을 위아래로 뒤집는 함수
def reverse_fig(figure):
    new_figure = copy.deepcopy(figure)

    # x좌표를 기준으로 정렬
    new_figure.sort()

    # 마지막 지점의 x좌표를 기준점으로 함
    fix_point = new_figure[-1][0]

    # x좌표를 업데이트(위 아래 뒤집기)
    for pos in new_figure:
        pos[0] = fix_point - pos[0]

    new_figure.sort()
    return new_figure


def rotate_fig(figure):
    new_figure = copy.deepcopy(figure)

    for pos in new_figure:
        pos[0], pos[1] = (3 - pos[1]), pos[0]

    # x좌표를 기준으로 정렬
    new_figure.sort()

    # 가장 상단의 x좌표를 기준점으로 설정
    fix_point = new_figure[0][0]

    # 가장 위쪽으로 좌표를 끌어올림
    if fix_point != 0:
        for pos in new_figure:
            pos[0] = pos[0] - fix_point

    return new_figure


n, m = map(int, input().rstrip().split())
arr = []
for _ in range(n):
    row_data = list(map(int, input().rstrip().split()))
    arr.append(row_data)

figure_arr = [
    [[0,0], [0,1], [0,2], [0,3]], # 테트로미노 1
    [[0,0], [0,1], [1,0], [1,1]], # 테트로미노 2
    [[0,0], [1,0], [2,0], [2,1]], # 테트로미노 3
    [[0,0], [1,0], [1,1], [2,1]], # 테트로미노 4
    [[0,0], [0,1], [0,2], [1,1]], # 테트로미노 5
]

# 최댓값을 기록하기 위한 변수
max_val = -1

# 테트로미노 도형을 순회
for figure in figure_arr:

    # 정확한 비교를 위한 sorting
    figure.sort()

    # 해당 도형을 변형시키며 실행 시키는 과정에서 중복 된 것이 있다면 건너뛰기 위한 중복 제거용 리스트
    fig_temp = []

    # 뒤집기는 최대 2회, 회전은 최대 4회 수행 가능
    for _ in range(2):
        # 뒤집어가면서 진행
        figure = reverse_fig(figure)

        for _ in range(4):
            # 회전시켜가며 진행
            figure = rotate_fig(figure)

            # 그동안 나온 것들과 중복되는 것이 있다면 수행하지 않음
            is_dup = False
            for temp in fig_temp:
                if figure == temp:
                    is_dup = True
                    break

            if is_dup:
                continue

            # 중복되지 않았다면, 중복 체크 리스트에 넣어줌
            fig_temp.append(figure)

            # 맵 전체를 순회하며 크기를 증가시키고, 필요없는 것은 걸러내는 형태로 수행
            for i in range(n):
                for j in range(m):

                    # 현재 놓여 있는 도형 위치로부터 숫자들의 합을 구함
                    is_out = False
                    sum = 0
                    for pos in figure:
                        # 도형의 위치 변경
                        x, y = pos[0] + i, pos[1] + j

                        # 만약 하나라도 판을 벗어났다면 해당 위치는 제대로 놓인 것이 아님으로 다음 도형으로 넘어감
                        if x < 0 or x >= n or y < 0 or y >= m:
                            is_out = True
                            break

                        sum += arr[x][y]

                    # 유효한 위치의 도형에 한해, max_val과 비교하여 더 크다면 업데이트
                    if not is_out and sum > max_val:
                        max_val = sum

print(max_val)