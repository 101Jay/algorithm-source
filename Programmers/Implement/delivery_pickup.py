# Programmers 150369, 택배 배달과 수거하기 (2023 카카오 공채)
def solution(cap, n, deliveries, pickups):
    answer = 0

    # 초기 길이 파악
    while deliveries:
        if deliveries[-1] == 0:
            deliveries.pop()
        else:
            break

    while pickups:
        if pickups[-1] == 0:
            pickups.pop()
        else:
            break

    del_len = len(deliveries)
    pick_len = len(pickups)

    while del_len > 0 or pick_len > 0:  # 둘 중 하나라도 0보다 커야 실행
        del_cap = 0
        pick_cap = 0

        # 최장거리로 왕복 길이 업데이트
        answer += 2 * max(del_len, pick_len)

        # cap을 최대로 채우면서 deliveries와 pickups를 pop

        # 배달이 완료되지 않았을 때만 수행
        if deliveries:
            # 1회 최대 배달 가능 용량을 채움
            while del_cap < cap:

                # 배달이 중간에 끝났다면 탈출
                if not deliveries:
                    break

                del_cap += deliveries.pop()
                if del_cap > cap:
                    # 넘치는 부분은 해당 위치에 다시 넣어줌
                    deliveries.append(del_cap - cap)
                    break

                # 넘치지 않는다면, 길이 감소시키기
                del_len -= 1

        # 수거가 완료되지 않았을 때만 수행
        if pickups:
            # 1회 최대 수거 가능 용량 채우기
            while pick_cap < cap:

                # pickup이 중간에 끝났다면 탈출
                if not pickups:
                    break

                pick_cap += pickups.pop()
                if pick_cap > cap:
                    pickups.append(pick_cap - cap)
                    break

                # 넘치지 않는다면, 길이 감소시키기
                pick_len -= 1

        # 최소 길이로 만들어주기(중간에 있는 0 제거)
        while deliveries:
            if deliveries[-1] == 0:
                deliveries.pop()
                del_len -= 1  # 길이 감소
            else:
                break

        while pickups:
            if pickups[-1] == 0:
                pickups.pop()
                pick_len -= 1  # 길이 감소
            else:
                break

    return answer