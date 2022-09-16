def solution(people, limit):  # [70, 50, 80, 50], 100
    people.sort(reverse=True)  # [80, 70, 50, 50]
    N = len(people)
    answer = 0
    escaped = [0] * N


    for i in range(N):
        if escaped[i] != 0:  # 만일 i가 탈출했다면 다음 사람으로 넘어감
            continue
        else:  # 만일 i가 탈출하지 못했다면
            answer += 1 # 배를 띄우고
            escaped[i] = 1  # i를 배에 태움

            if 0 not in escaped:  # i가 마지막 탈출자였다면
                break
            else:
                for j in range(N-1, i, -1):
                    if escaped[j] == 0 and people[i] + people[j] <= limit:
                        escaped[j] = 1
                        break
                if 0 not in escaped:
                    break

    return answer



print(solution([70, 50, 80, 50], 100))

