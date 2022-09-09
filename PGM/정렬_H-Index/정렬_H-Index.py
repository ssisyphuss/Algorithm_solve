def solution(citations):
    for i in range(len(citations)-1, 0, -1):
        for k in range(i):
            if citations[k] < citations[k+1]:
                citations[k], citations[k+1] = citations[k+1], citations[k]

    for h in range(1, len(citations)):
        if citations[h-1] <= h:
            return h


# 결과: 제대로 도출되나 모든 경우에서 런타임 에러