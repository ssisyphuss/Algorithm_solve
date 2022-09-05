def solution(numbers, target):
    answer = 0
    def DFS(numbers, temp_sum, depth, target):
        nonlocal answer
        if depth == len(numbers):
            if temp_sum == target:
                answer += 1
        else:
            DFS(numbers, temp_sum + numbers[depth], depth + 1, target)
            DFS(numbers, temp_sum - numbers[depth], depth + 1, target)


    DFS(numbers, 0, 0, target)

    return answer


print(solution([4,1,2,1], 4))

