def solution(n, lost, reserve):
    answer = 0
    helped = []  # 체육복을 친구에게 받은 사람
    lost.sort()  # 잃어버린 사람을 정렬해줌
    reserve.sort()  # 여분을 갖고 있는 사람을 정렬해줌

    copy_lost = lost[::]  #  잃어버린 사람의 목록을 복사함

    for i in lost:  # 잃어버린 사람 중에서
        if i in reserve:  #  만일 여분이 있는 사람이었다면
            copy_lost.remove(i)  # 잃어버린 사람의 목록에서 제거함
            reserve.remove(i)  # 여분을 가진 사람의 목록에서도 제거함

    lost = copy_lost  # 결과적으로 체육복이 없는 lost에, 여분이 있는 사람은 reserve에 남음

    for i in lost:  # 잃어버린 사람들에 대하여
        if i - 1 in reserve:  # 앞 사람이 여분이 있으면
            helped.append(i)  #
            reserve.remove(i - 1)
            continue

        if i + 1 in reserve:  # 뒷 사람의 여분이 있으면
            helped.append(i)
            reserve.remove(i + 1)

    answer = n - len(lost) + len(helped)

    return answer

print(solution(5, [2,4], [1,3,5]))
