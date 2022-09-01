import sys

sys.stdin = open("/Users/huijaeshin/Desktop/Programming/pycharm-algorithm/BJ/2163-포도주시식/input.txt")

def wine(A):  # A는 포도주 배열
    M = len(A)   # [6, 10, 13, 9, 8, 1]
    memo = [0 for _ in range(M)]

    for i in range(M):
        if i == 0:
            memo[i] = A[i]
        elif i == 1:
            memo[i] = A[i - 1] + A[i]
        elif i == 2:
            memo[i] = max(A[0]+A[1], A[0]+A[2], A[1]+A[2])
        else:
            memo[i] = max(memo[i-3]+A[i-1]+A[i], memo[i-2]+A[i], memo[i-1])

    return memo[-1]


N = int(input())

numbers = [int(input()) for _ in range(N)]

print(wine(numbers))

