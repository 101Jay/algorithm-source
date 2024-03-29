# Programmers 87946, 피로도
from itertools import permutations
def solution(k, dungeons):
    dun_size = len(dungeons)

    temp = [i for i in range(dun_size)]
    combs = list(permutations(temp, dun_size))

    max_explore = 0
    # 모든 순열을 순회하며 수행 가능한 던전의 최댓값 구함
    for comb in combs:
        # 순서대로 던전을 탐험하며 해당 조합에서 몇 개나 탐험할 수 있는지 파악
        cur_pi = k
        cnt = 0
        for j in comb:
            tg_dun = dungeons[j]
            if cur_pi >= tg_dun[0]:
                cur_pi -= tg_dun[1]
                cnt += 1
            else:
                break

        # max_explore보다 더 많다면 갱신
        if cnt > max_explore:
            max_explore = cnt

    return max_explore