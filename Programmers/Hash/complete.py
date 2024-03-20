# Programmers 42576, 완주하지 못한 선수
def solution(participant, completion):
    answer = ''

    # 1. 두 리스트를 모두 dictionary로 변경
    part_dict = {}
    comp_dict = {}

    for part in participant:
        if part not in part_dict:
            part_dict[part] = 0
        part_dict[part] += 1

    for comp in completion:
        if comp not in comp_dict:
            comp_dict[comp] = 0
        comp_dict[comp] += 1

    # 2. part_dict를 순회하며 comp_dict와 비교
    for key, value in part_dict.items():
        if key not in comp_dict:
            answer = key
            break

        if value != comp_dict[key]:
            answer = key
            break

    return answer