# BOJ 1049, 기타줄

import sys
input = sys.stdin.readline

string, pack_num = list(map(int, input().split()))

min_pack = 1001
min_sep = 1001
for _ in range(pack_num):
    pack, sep = list(map(int, input().split()))
    min_pack = min(pack, min_pack)
    min_sep = min(sep, min_sep)

if min_pack > min_sep * 6:
    print(min_sep * string)
else:
    div_six = string // 6
    spare = string % 6

    result = div_six * min_pack
    result += min(spare * min_sep, min_pack)
    print(result)