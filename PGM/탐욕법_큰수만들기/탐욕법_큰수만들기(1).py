def solution(number, k):
    answer = ''
    cnt = k
    number = list(number)  # 숫자들을 리스트로 받음
    N = len(number)

    i = 0
    while True:
        if number[i] >= number[i+1]:  # 만일 첫 글자가 뒤 글자보다 더 크면
            i += 1  # 살린다
            if i+1 >= N:  # 만일 다음 인덱스가 범위를 넘어서면
                for _ in range(cnt):  # 그때까지 남은 카운트만큼 끝에서 빼줌   # 98765
                    number.pop()
                break
        else:  # number[i] < number[i+1]:  #  만일 뒤 수자가 더 크면
            number.pop(i)  # 해당 숫자는 제거해준다
            cnt -= 1  # 카운트 제거해줌
            if cnt == 0:  # 만일 카운트 다 소모했다면
                break  # 브레이크

            if i != 0:
                i -= 1

    answer = str(''.join(number))
    return answer