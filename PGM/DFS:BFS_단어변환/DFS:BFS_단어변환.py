def solution(begin, target, words):
    N = len(words)
    long = len(words[0])
    visited = {}
    count_list = []
    least_num = long - len(set(begin) & set(target))

    for i in range(N):
        visited[words[i]] = 0

    cnt = 0  # 최적은 hit -> hot -> dot -> dog-> cog

    if target not in words:
        return 0

    def DFS(begin, target, words):
        nonlocal cnt
        if begin == target:
            count_list.append(cnt)
            if cnt == least_num:
                return
        else:
            visited[begin] = 1
            for j in range(N):
                if words[j] != begin and visited[words[j]] == 0:
                    temp_cnt = 0
                    for k in range(long):
                        if begin[k] == words[j][k]:
                            temp_cnt += 1
                    if temp_cnt == long - 1:
                        cnt += 1  # 넘어가기 전에 카운트를 더해줌
                        DFS(words[j], target, words)  # 빠졌다가 나오면 카운트에서 하나 빼줌
                        cnt -= 1
            visited[begin] = 0

    DFS(begin, target, words)


    answer = min(count_list) if count_list != [] else 0

    return answer



print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))