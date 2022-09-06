def solution(progresses, speeds):
    answer = []
    while progresses != []:
        cnt = 0
        # add speed on each progress
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        # if first elements fully developed,
        if progresses[0] >= 100:
            while progresses != [] and progresses[0] >= 100:
                progresses.pop(0)
                speeds.pop(0)
                cnt += 1
            answer.append(cnt)

    return answer

print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))