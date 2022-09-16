from collections import deque

def solution(people, limit):  # [70, 50, 80, 50], 100
    people.sort(reverse=True)
    people = deque(people)  # deque [80, 70, 50, 50]

    N = len(people)
    answer = 0

    while people:  # 만일 people이 남아 있다면
        answer += 1  # 배를 띄우고
        if len(people) == 1:  #  만일 한 명만 남아 있었다면
            man = people.pop()  #  그 사람을 태우고 끝
            break
        else:  #  한 명 이상 남아 있었다면
            man = people.popleft()  #  남은 사람 중 가장 무거운 사람 태우고,
            if man + people[-1] <= limit:  #  가장 가벼운 사람을 태웠을 때 한계가 넘지 않으면 또 태움
                people.pop()

  # .popleft()  -> O(1)
    return answer



print(solution([70, 50, 80, 50], 100))

# https://leonkong.cc/posts/python-deque.html (데크(deque) 언제, 왜 사용해야 하는가?)