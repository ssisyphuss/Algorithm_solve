def solution(n, computers):
    answer = 0
    visited = [0] * n

    def DFS(v, computers, depth):
        nonlocal answer, visited
        if visited[v] == 1:
                return
        else:
            visited[v] = 1
            for j in range(n):
                if computers[v][j] == 1 and v != j and visited[j] != 1:
                    DFS(j, computers, depth + 1)

        if depth == 0:
            answer += 1

    for i in range(n):
        DFS(i, computers, 0)

    return answer

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))