def solution(numbers):
    for i in range(len(numbers)-1, 0, -1):
        for idx in range(i):
           if int(str(numbers[idx])+str(numbers[idx+1])) < int(str(numbers[idx+1])+str(numbers[idx])):
               numbers[idx], numbers[idx + 1] = numbers[idx + 1], numbers[idx]
    return ''.join(list(map(str, numbers)))

# 결과: 1,2,3,5,6 시간초과

