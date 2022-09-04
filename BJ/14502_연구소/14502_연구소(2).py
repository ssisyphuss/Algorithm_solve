'''
전략을 세워보자:
벽을 미리 어디에 세울지를 고려하는 대원칙을 찾는 것은 어려울 것 같다.
그렇기 때문에 가능한 모든 경우에 벽을 세워주면서,
해당 경우에 바이러스가 어디까지 퍼질 수 있는지를 카운트하여
그 경우 바이러스가 가장 적게 퍼진다면 결과에 등록하는 방법을 사용해야될 것 같다.

그렇다면 문제 풀이의 순서는 다음이 되어야 한다:
(1) 우선은 가능한 모든 경우에 벽을 세워준다.
(2) 해당 경우(벽의 개수가 3개가 되는 경우)에 바이러스를 돌린다.
  (2-1) 바이러스를 돌릴 때는 DFS로 하면 누락되는 경우가 발생할 수 있다. BFS로 돌리자.
'''

import sys
from pprint import pprint


sys.stdin = open('input.txt')


n, m = map(int, input().split(' '))
# print(n, m)

result = 0
matrix = []

for i in range(n):
    matrix.append(list(map(int, input().split(' '))))

# input 그리기
pprint(matrix)

virus = []
load = []

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 2:
            virus.append((i, j))
        if matrix[i][j] == 0:
            load.append((i, j))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 바이러스 감염 (bfs)
def spread_virus(temp_map):
    check = [[0 for _ in range(m)] for _ in range(n)]
    cnt = 0
    temp_virus = virus[:]  # temp_virus는 virus 근원지를 복사한
    while temp_virus:
        x, y = temp_virus.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (
                0 <= nx < n
                and 0 <= ny < m
                and temp_map[nx][ny] == 0  # 만일 빈 공간이면
                and check[nx][ny] == 0  # 만일 바이러스가 아직 돌지 않았다면
            ):
                check[nx][ny] = 1  # 바이러스가 돌았음
                temp_virus.append((nx, ny))  # 바이러스에 추가함
                temp_map[nx][ny] = 2

    for i in range(n):
        for j in range(m):
            if temp_map[i][j] == 0:
                cnt += 1
    return cnt


check_load = [0 for _ in range(len(load))]
temp_wall = []


# DFS(벽을 세우는 자리 모두 확인)
def get_wall(idx, cnt):
    global result

    # 벽의 개수가 3이면 바이러스 기준으로 BFS(spread_virus())
    if cnt == 3:
        temp_map = []
        for i in matrix:
            temp_map.append(i[:])
        for x, y in temp_wall:
            temp_map[x][y] = 1
        result = max(result, spread_virus(temp_map))
        # pprint(result)
        return

    for i in range(idx, len(load)):
        if check_load[i] == 1:
            continue
        temp_wall.append(load[i])
        check_load[i] = 1
        get_wall(i, cnt + 1)
        temp_wall.pop()
        check_load[i] = 0


# 처음 인덱스부터 시작
get_wall(0, 0)

print(result)