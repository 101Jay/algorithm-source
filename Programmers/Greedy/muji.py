# 프로그래머스 42891, 무지의 먹방 라이브
def solution(food_times, k):

    length = len(food_times)

    answer = -1
    while k >= 1:

        # 음식 종류 개수 (food_type) 업데이트
        food_type = 0
        for i in range(length):
            if food_times[i] != 0:
                food_type += 1

        # 최솟값 업데이트
        min_elem = 1001
        for j in range(length):
            if food_times[j] != 0 and food_times[j] < min_elem:
                min_elem = food_times[j]


        # k가 1보다 큰 상태에서 먹을 음식이 남지 않았다면 -1 리턴
        if food_type == 0:
            break

        # k를 남은 음식의 종류 수로 나눈 몫
        share = k // food_type

        if share >= 1:
            # 순회할 필요가 있음

            # 몫이 최솟값보다 작아지도록 줄임 (min_elem은 0보다 클 수밖에 없음 -> share가 갖게 될 수 있는 가장 작은 수는 1)
            if share > min_elem:
                while share > min_elem:
                    share -= 1
            else:
                # share을 최대한 min_elem에 가깝게 증가시켜 효율 증진
                while share <= min_elem:
                    share += 1
                    if share * food_type > k:
                        share -= 1
                        break


            # 원소를 돌며 share만큼 값 줄이기(음식 먹기)
            for t in range(length):
                if food_times[t] != 0:
                    food_times[t] -= share

            # 먹은만큼 k의 값 줄이기
            k -= share * (food_type)

            # 음식 종류 개수 (food_type) 업데이트
            food_type = 0
            for i in range(length):
                if food_times[i] != 0:
                    food_type += 1

            # k와 food_type가 동일했다면 k가 0이 될 수 있어서 체크
            if k == 0:
                if food_type == 0:
                    break # -1을 리턴하는 것과 동일

                # 먹을 음식이 남았다면, 무엇을 먹을 차례인지 확인
                for i in range(length):
                    if food_times[i] != 0:
                        answer = i
                        break
        else:
            # 더 이상 순회 불가
            # 남은 것을 털어낸 뒤, 무엇을 먹을 차례인지 확인
            for i in range(length):
                if food_times[i] == 0:
                    continue
                if k == 0:
                    answer = i
                    break
                k -= 1

    if answer == -1:
        return answer
    else:
        return answer + 1