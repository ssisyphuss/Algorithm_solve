def solution(prices):
    answer = []
    N = len(prices)

    for i in range(N):  # for each price,
        for j in range(i+1, N):  # if some price after the price is lower,
            if prices[i] > prices[j]:
                answer.append(j-i)
                break
        else:
            answer.append(j-i)  # else, the price lasts til the end
    return answer



print(solution([1, 2, 3, 2, 3]))