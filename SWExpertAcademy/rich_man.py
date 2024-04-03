# SW Expert Academy 1859, 백만장자 프로젝트
T = int(input().rstrip())
answer = []
for _ in range(T):
    n = int(input().rstrip())
    arr = list(map(int, input().rstrip().split()))
    ans = 0
    while arr:
        max_val = max(arr)
        tg_idx = 0
        for idx, num in enumerate(arr):
            if num == max_val:
                tg_idx = idx
                break

            ans += (max_val - num)

        if tg_idx == len(arr) - 1:
            arr = []
        else:
            arr = arr[tg_idx+1:]

    answer.append(ans)

for i, ans in enumerate(answer):
    print("#" + str(i+1), ans)