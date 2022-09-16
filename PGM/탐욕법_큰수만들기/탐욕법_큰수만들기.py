def solution(number, k):
    answer = ''
    N = len(number)
    cnt = k
    i = 0
    stack = []

    while True:
        if stack == []:  #  스택이 비어 있으면
            stack.append(number[i])   # 스택에 추가해줌
            i += 1
        else: # 만일 스택에 숫자가 이미 있다면      # 4177252841
            if stack[-1] < number[i]:   # 스택의 마지막 숫자보다 현재 숫자가 더 크다면 마지막 숫자를 팝아웃
                stack.pop()
                cnt -= 1
            else:  #  만일 현재 숫자가 더 작다면
                stack.append(number[i])   #  append 해줌
                i += 1

        if cnt == 0:  # 만일 카운트가 다 떵러지면
            for k in range(i, N):
                stack.append(number[k])  #  나머지 숫자들을 모두 스택에 넣어줌
            break
        if i >= N:  # 만일 카운트가 남아있지만  인덱스를 벗어나는 경우
            for _ in range(cnt):
                stack.pop()  #  남은 만큼 스택에서 빼내줌
            break

    answer = str(''.join(stack))
    return answer

print(solution('4177252841', 4))
# i = 3  cnt = 3
# '77262841'