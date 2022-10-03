def solution(clothes):
    answer = 0
    clothes_dict = {}

    for cloth in clothes:
        clothes_dict.setdefault(cloth[1], 0)
        clothes_dict[cloth[1]] += 1

    for cloth in clothes_dict:
        clothes_dict[cloth] += 1

    combi = 1
    for num in clothes_dict.values():
        combi *= num

    answer = combi - 1

    return answer


print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))