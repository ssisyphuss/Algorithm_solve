'''
전략: 따로 스택을 만들지는 않고,
numbers에 index를 통해 접근하고
counts를 통해 진행 상황을 파악함
'''

def solution(numbers, target):  # [4, 1, 0, 1], 4
    answer = 0
    N = len(numbers)
    counts = [0] * N

    i = 0
    temp_sum = 0
    while i >= 0:
        if i == N-1:
            counts[i] += 1
            if counts[i] == 3:
                counts[i] = 0
                i -= 1
            else:
                if counts[i] == 1:
                    temp_sum += numbers[i]
                    if temp_sum == target:
                        answer += 1
                    temp_sum -= numbers[i]

                elif counts[i] == 2:
                    temp_sum -= numbers[i]
                    if temp_sum == target:
                        answer += 1
                    temp_sum += numbers[i]
            continue
        else:
            counts[i] += 1
            if counts[i] == 1:
                temp_sum += numbers[i]
                i += 1
            elif counts[i] == 2:
                temp_sum -= numbers[i]
                temp_sum -= numbers[i]
                i += 1
            else:
                temp_sum += numbers[i]
                counts[i] = 0
                i -= 1

    return answer


print(solution([4, 1, 0, 1], 4))