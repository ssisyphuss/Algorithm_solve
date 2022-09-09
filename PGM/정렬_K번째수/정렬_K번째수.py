def solution(array, commands):
    answer = []

    for i in commands:
        sliced = array[i[0] - 1:i[1]]
        new_num = sorted(sliced)[i[2] - 1]
        answer.append(new_num)

    return answer


# 결과: 성공