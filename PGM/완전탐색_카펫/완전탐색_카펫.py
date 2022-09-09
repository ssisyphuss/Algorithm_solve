def solution(brown, yellow):
    whole = brown + yellow
    lst = []
    for n in range(1, whole):
        for m in range(1, (whole//n) + 1):
            if 2*n+ 2*m - 4 == brown and (n-2) * (m-2) == yellow and n >= m:
                lst.append(n)
                lst.append(m)

    return lst

print(solution(8, 1))