def solution(priorities, location):
    priorities = list(enumerate(priorities))  # e.g. [(0, 2), (1, 1), (2, 3), (3, 2)]

    answer = 0
    while True:
        if priorities[0][1] < max([q for i, q in priorities]):  # 대기열 맨 앞의 문서열의 중요도가 남은 가장 높은 중요도보다 낮으면
            priorities.append(priorities.pop(0))  # 해당 요소를 pop하여 맨 뒤로 보냄
        else:
            if priorities[0][0] == location:  # 만일 첫 문서가 가장 높은 중요도를 가지고 그것이 우리가 원하는 문서라면,
                answer += 1  # 순서에 1을 추가하고
                return answer  # 지금까지 누적된 순서를 출력함

            else:
                answer += 1  # 첫 문서가 우리가 원하는 문서가 아니라면,
                priorities.pop(0)  # 해당 문서를 제거함


print(solution([1, 1, 9, 1, 1, 1], 0))  # -> 5
