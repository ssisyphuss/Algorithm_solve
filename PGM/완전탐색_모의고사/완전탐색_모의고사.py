def solution(answers):
    answer = []
    pattern_one = [1, 2, 3, 4, 5]
    pattern_two = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern_three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    counts = [0, 0, 0]

    for i in range(len(answers)):
        if answers[i] == pattern_one[(i%5)]:
            counts[0] += 1
        if answers[i] == pattern_two[(i%8)]:
            counts[1] += 1
        if answers[i] == pattern_three[(i%10)]:
            counts[2] += 1

    for i in range(len(counts)):
        if counts[i] == max(counts):
            answer.append(i+1)

    return answer




print(solution([1, 3, 2, 4, 2]))
