import sys

sys.stdin = open('/Users/huijaeshin/Desktop/Programming/pycharm-algorithm/BJ/10942팰린드롬/input.txt')

N = int(input())
numbers = list(map(int, input().split()))
M = int(input())

palindrome = [[-1 for _ in range(N)] for _ in range(N)]

def check(s, e):
    global palindrome, numbers
    N = len(numbers)

    for length in range(numbers):
        for start in range(numbers-length):
            if numbers[s] != numbers[e]:
                palindrome[s][e] = 0
            else:
                if s == e:  # 한 글자인 경우
                    palindrome[s][e] = 1
                elif s+1 == e:  # 두 글자인 경우
                    if numbers[s] == numbers[e]:
                        palindrome[s][e] = 1
                    else:
                        palindrome[s][e] = 0
                else:  # 세 글자 이상인 경우
                    if palindrome[s+1][e-1] == 0:
                        palindrome[s][e] = 0
                    else:
                        palindrome[s][e] = 1

for _ in range(M):
    S, E = map(int, input().split())
    if palindrome[S-1][E-1]:
        print(1)
    else:
        print(0)


