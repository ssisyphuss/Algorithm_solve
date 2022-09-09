def solution(numbers):
    numbers_copy = numbers[::]

    for i in range(len(numbers_copy)):
        if len(str(numbers[i])) == 1:
            numbers_copy[i] = f'{numbers[i]}**'
        if len(str(numbers[i])) == 2:
            numbers_copy[i] = f'{numbers[i]}*'
        if len(str(numbers[i])) >= 3:
            numbers_copy[i] = f'{numbers[i]}'
    # 이제 numbers_copy는 ['7**', '72*', '362', '3**' ...] 등이 요소로 들어가 있음

    for i in range(len(numbers) - 1, 0, -1):
        for idx in range(i):
            # 붙어있는 두 숫자를 비교하여 첫자리가 큰 것을 앞으로 재정
            if str(numbers[idx])[0] != str(numbers[idx + 1])[0]:
                if int(str(numbers[idx])[0]) < int(str(numbers[idx+1])[0]):
                    numbers[idx], numbers[idx + 1] = numbers[idx + 1], numbers[idx]
            # 숫자의 첫글자가 만일 같다면, 두 번째 문 비교로 넘어감
            if str(numbers[idx])[0] == str(numbers[idx + 1])[0]:
                if numbers_copy[idx][1] == '*' and numbers_copy[idx+1][1] != '*':
                    if str(numbers[idx])[0] < str(numbers[idx+1])[1]:
                        numbers[idx], numbers[idx + 1] = numbers[idx + 1], numbers[idx]
                if numbers_copy[idx][1] != '*' and numbers_copy[idx+1][1] == '*':
                    if str(numbers[idx])[1] < str(numbers[idx+1])[0]:
                        numbers[idx], numbers[idx + 1] = numbers[idx + 1], numbers[idx]
                # 만일 두 숫자가 모두 두자리수 이상이라면
                if numbers_copy[idx][1] != "*" and numbers_copy[idx] != '*':
                    # 세 번째 자리 비교 후 큰 것을 앞으로
                    if numbers_copy[idx][2] == '*' and numbers_copy[idx+1][2] == '*':
                        if numbers[idx] < numbers[idx+1]:
                            numbers[idx], numbers[idx + 1] = numbers[idx + 1], numbers[idx]
                    if numbers_copy[idx][2] == '*' and numbers_copy[idx+1][2] != '*':
                        if str(numbers[idx])[1] < str(numbers[idx+1])[2]:
                            numbers[idx], numbers[idx + 1] = numbers[idx+1], numbers[idx]
                    if numbers_copy[idx][2] != '*' and numbers_copy[idx+1][2] == '*':
                        if str(numbers[idx])[2] < str(numbers[idx+1])[1]:
                            numbers[idx], numbers[idx + 1] = numbers[idx + 1], numbers[idx]
                    if '*' not in [numbers_copy[idx][2], numbers_copy[idx + 1][2]]:
                        if numbers[idx] < numbers[idx + 1]:
                            numbers[idx], numbers[idx + 1] = numbers[idx + 1], numbers[idx]

    return ''.join(list(map(str, numbers)))


print(solution([3, 30, 34, 5, 9]))


# 결과: 1, 2, 3, 4, 5, 6, 14 런타임 에러, 7, 10, 11 실패