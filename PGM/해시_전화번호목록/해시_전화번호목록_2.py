def solution(phone_book):
    answer = True
    for i in range(len(phone_book)-1, 0, -1):
        for j in range(i):
            if len(phone_book[j]) > len(phone_book[j+1]):
                phone_book[j], phone_book[j+1] = phone_book[j+1], phone_book[j]

    for i in range(len(phone_book)):
        for j in range(i+1, len(phone_book)):
            if phone_book[j][:len(phone_book[i])] == phone_book[i]:
                answer = False
                break
    return answer