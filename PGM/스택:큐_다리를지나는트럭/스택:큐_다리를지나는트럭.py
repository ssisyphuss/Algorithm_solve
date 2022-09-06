def solution(bridge_length, weight, truck_weights):  # e.g. 2, 10, [7,4,5,6]
    seconds = 0  # 총 시
    trucks = [[t, 0] for t in truck_weights]  # 트럭에 트럭들의 [무게, 다리 위 시간]를 저장해줌.

    on_bridge = []
    while True:
        seconds += 1
        # 다리 위의 모든 차의 시간을 하나 더하고 다 건넜으면 내림.
        if on_bridge != []:  # 만일 다리 위에 트럭이 있으면
            for i in range(len(on_bridge)):
                on_bridge[i][1] += 1  # 트럭들의 다리 위의 시간을 1초씩 늘림
            if on_bridge[0][1] == bridge_length:  # 만일 도착했으면
                on_bridge.pop(0)  # 다리에서 내림

        # 새로운 트럭 탑승시킴
        if trucks != []:  # 남은 트럭이 있으면
            if trucks[0][0] + sum([weight for [weight, time] in on_bridge]) <= weight:
                on_bridge.append(trucks.pop(0))
        # 만일 새로운 트럭이 없고 다리에도 없다면,
        else:
            if on_bridge == []:  # 만일 다리가 비어 있으면
                return seconds   # 지금까지 걸린 시간 반환



print(solution(2, 10, [7,4,5,6]))  # -> 8