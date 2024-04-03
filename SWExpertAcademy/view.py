# SW Expert Academy 1206. [S/W 문제해결 기본] 1일차 - View
answer = []
for _ in range(10):
    size = int(input().rstrip())
    buildings = list(map(int, input().rstrip().split()))
    ans = 0
    for i in range(2, size-2):
        # i번째 건물을 의미
        # 좌우 양쪽 2개의 건물을 살피며 최대 층수를 구함
        max_val = max(max(buildings[i-2:i]), max(buildings[i+1:i+3]))

        cur_view = buildings[i] - max_val
        if cur_view > 0:
            ans += cur_view
    answer.append(ans)

for i, ans in enumerate(answer):
    print("#" + str(i+1), ans)