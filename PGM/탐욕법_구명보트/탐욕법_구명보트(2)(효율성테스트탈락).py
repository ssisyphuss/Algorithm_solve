def solution(people, limit):  # [70, 50, 80, 50], 100
    people.sort(reverse=True)  # [80, 70, 50, 50]
    N = len(people)
    answer = 0



    while people:  # 만일 people이 남아 있다면         # [80, 70, 60, 20, 10], limit == 100
        answer += 1  # 배를 띄우고
        if len(people) == 1:  #  만일 한 명만 남아 있었다면
            man = people.pop()  #  그 사람을 태우고 끝
            break
        else:  #  한 명 이상 남아 있었다면
            man = people.pop(0)  #  남은 사람 중 가장 무거운 사람 태우고,
            if man + people[-1] <= limit:  #  가장 가벼운 사람을 태웠을 때 한계가 넘지 않으면 또 태움
                people.pop()

    return answer

   # list.pop()  -> O(1)
   # list.pop(0) -> O(N)
#  list.pop(k) 할 때, 인덱스 k로 접근해서 빼줌 -> k 뒤에 있는 애들을 다 하나씩 땡김  ->  O(N-k)
#     list.pop(0)  => 0으로 접근해서 빼주고, 나머지 모든 애들을 다 원래보다 하나씩 땡김 -> O(N)

print(solution([70, 50, 80, 50], 100))


