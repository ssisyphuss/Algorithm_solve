def solution(citations):
    for h in range(1, len(citations)+1):
        h_count = 0
        for citation in citations:
            if citation >= h:
                # h_count는 인용수가 h 이상인 논문의 횟수
                h_count += 1
        if h_count <= h:  # h_count <= h 이면 실패 사례를 커버할 수 있지 않을까? (원민석)
            h_index = h  # [33, 66], [5, 5, 5, 5, 5]
            return h_index



# 결과: tc9 실패, 나머지 성공

