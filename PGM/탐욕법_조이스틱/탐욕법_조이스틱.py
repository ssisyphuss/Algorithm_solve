'''
[풀이]
1. 각각의 문자에서 아래로 갈지 위로 갈지 정하는 것은 간단함.
ord('A') == 65, ord('Z') == 90 이므로
만일 ord(char) == 78이면 A에서 위로 갈 때 13만큼, 아래로 갈 때 13만큼 간다.
즉 ord(char) <= 78일 때 ord(char) - 65, 아닐 때 90 - ord(char) + 1 만큼 이동해야한다.

2. 어려운 부분은 문자열을 이동할 때 오른쪽으로 갈지, 왼쪽으로 갈지, 아니면 한 쪽으로 갔다가 꺾어야할지의 여부.

(i) 문자열을 원형으로 생각했을 때 첫 글자가 제일 긴 연속된 A 문자열 중에 있는 경우
  --> 전체 문자열 길이 N에서 다른 글자까지 가는 게 먼 방향으로의 A 개수를 빼고 1을 더 빼줌
       e.g. AAABBCDA 라면, 좌측으로 가는 게 더 빠르고, 우측으로 A가 두개 있으므로 8 - 2 - 1 = 5
(ii) 아닌 경우
  --> 만일 해당 A 문자열 전까지 갔다가 다시 되돌아서 시작점으로 오는 게 A 개수보다 적으면 A를 통과하는 게 나으므로 N -1 번
      아니라면, A 직전까지 갔다가 다시 방향을 틀어서 끝까지 가기. 이 경우 A 문자열 직전 문자까지의 클릭을 M이라고 하면
      2M + (N - M - A연속수 -1) = M + N - A연속수 - 1

'''



def solution(name):
    answer = 0
    move = 0
    change_letter = 0
    N = len(name)

    max_cnt = 0
    start_idx = 0

    temp = 0
    for i in range(-N, N):
        if name[i] == 'A':
            temp += 1
        else:
            if temp >= max_cnt:
                max_cnt = temp
                start_idx = i - temp
                temp = 0
            else:
                temp = 0


    # 만일 문자열 안에 'A'가 없다면
    if max_cnt == 0:
        move = N-1
    # 만일 모든 문자열이 'A'로 이루어져 있다면
    elif max_cnt == N:
        move = 0

    else:  # 만일 문자열 안에 'A'가 있다면   # BAABBBBBAA
        if start_idx < 0:  # start_idx가 0보다 작다는 것은, 시작점이 가장 긴 연속된 A의 한 부분임을 의미함.
            if start_idx + max_cnt >= -1 * (start_idx - 1):  # 만일 우측으로 가는 게 더 길다면
                move = N - (start_idx + max_cnt)
            else:
                move = N - (-1) * (start_idx - 1)
        elif start_idx >= 0:  # 시작점이 가장 긴 연속된 A의 한 부분이 아님.
            P = start_idx - 1  # P는 오른쪽으로 가서 가장긴 문자열을 만나기 직전까지의 거리
            Q = N - (start_idx + max_cnt)  # Q는 왼쪽으로 가서 가장긴 문자열을 만나기 직전까지의 거리

            if N-1 <= 2*min(P, Q) + max(P, Q):
                move = N-1
            else:
                move = 2*min(P, Q) + max(P, Q)


    # 아래는 문자열을 바꾸는 데 드는 최소 회수
    for i in range(N):
        if ord(name[i]) <= 78:
            change_letter += ord(name[i]) - 65
        else:
            change_letter += 91 - ord(name[i])

    answer = move + change_letter

    return answer

print(solution('BBAAAFFFFADDAAA'))   # BBBBAAAB  -> 10
                              # ABABAAAAAAABA -> 10
                            #BBAAABBBBABBAAA

#  'ABABAAAAAB'

