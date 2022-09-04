'''
전략을 세워보자:
벽을 미리 어디에 세울지를 고려하는 대원칙을 찾는 것은 어려울 것 같다.
그렇기 때문에 가능한 모든 경우에 벽을 세워주면서,
해당 경우에 바이러스가 어디까지 퍼질 수 있는지를 카운트하여
그 경우 바이러스가 가장 적게 퍼진다면 결과에 등록하는 방법을 사용해야될 것 같다.

그렇다면 문제 풀이의 순서는 다음이 되어야 한다:
(1) 우선은 가능한 모든 경우에 벽을 세워준다.
(2) 벽을 3개 세운 상태에서 바이러스를 퍼뜨린다.
  (2-1) 바이러스를 돌릴 때는 DFS로 하면 누락되는 경우가 발생할 수 있다. BFS로 돌리자.
'''

import copy
from itertools import combinations

def virus(place):
    global where_virus, dx, dy

    contaminated = copy.deepcopy(place)
    virus_now = where_virus[:]

    while virus_now:
        x, y = virus_now.pop(0)
        place[x][y] = 2
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx <= N-1 and 0 <= ny <= M-1 and contaminated[nx][ny] == 0:
                contaminated[nx][ny] = 2
                virus_now.append((nx, ny))


N, M = map(int, input().split())
place = list(list(map(int, input().split())) for _ in range(N))
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
safe_place = 0

where_virus = []
where_path = []

for i in range(N):
    for j in range(M):
        if place[i][j] == 2:
            where_virus.append((i, j))
        elif place[i][j] == 0:
            where_path.append((i, j))


wall_combination = list(combinations(where_path, 3))
W = len(wall_combination)

for i in range(0, W):
    temp_place = copy.deepcopy(place)
    for (m, n) in wall_combination[i]:
        temp_place[m][n] = 1

    virus(temp_place)

    temp_safe = 0
    for p in range(N):
        for q in range(M):
            if temp_place[p][q] == 0:
                temp_safe += 1
    if temp_safe > safe_place:
        safe_place = temp_safe

print(safe_place)





