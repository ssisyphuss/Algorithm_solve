def solution(citations):
    for h in range(len(citations)-1, 0, -1):
        h_count = 0
        for citation in citations:
            if citation >= h:
                # h_count는 인용수가 h 이상인 논문의 횟수
                h_count += 1
        if h_count > h:
            h_index = h+1
            return h_index

# 결과: tc 11, 16 실패
