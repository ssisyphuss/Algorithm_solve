def solution(phone_book):
    answer = True
    phone_book.sort()

    print(phone_book)
    N = len(phone_book)

    for i in range(N-1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            answer = False
            break

    return answer

print(solution(["118", "1189", "11951"]))

