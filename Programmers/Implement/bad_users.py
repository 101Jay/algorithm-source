# Programmers 64064, 불량 사용자
from itertools import permutations
def solution(user_id, banned_id):
    answer = 0

    # user_id 목록에서 banned_id 목록의 크기만큼 순열 구하기
    banned_size = len(banned_id)
    select_id = list(permutations(user_id, banned_size))

    mapped_col = []

    # 각 조합을 순회하며 banned_id와 매핑되는지 확인
    for id_tup in select_id:
        is_map = True
        # 순서대로 id_tup이 banned_id와 매핑되는지 확인
        for i in range(banned_size):
            tg_id = id_tup[i]
            ban_id = banned_id[i]
            tg_size = len(tg_id)

            # 길이가 다르면 out
            if tg_size != len(ban_id):
                is_map = False
                break

            # 문자를 하나씩 순회하며 일치여부 확인
            for j in range(tg_size):
                # ban_id[j]가 * 이면 건너뜀
                if ban_id[j] == '*':
                    continue

                # 해당 문자가 다르면 탈출
                if ban_id[j] != tg_id[j]:
                    is_map = False
                    break

            # 매핑되지 않는 조합이라면 탈출
            if not is_map:
                break

        # 매핑이 되었고, 조합과 동일한 set이 없을 경우 저장
        if is_map and set(id_tup) not in mapped_col:
            mapped_col.append(set(id_tup))
            answer += 1

    return answer