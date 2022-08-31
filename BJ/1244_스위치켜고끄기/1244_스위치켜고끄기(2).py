import sys


sys.stdin = open('input.txt')


N = int(input())
switches = [0] + list(map(int, input().split()))
stu_number = int(input())
stu_info = [list(map(int, input().split())) for _ in range(stu_number)]


for student in stu_info:
    if student[0] == 1:
        num = student[1]
        for i in range(num, len(switches), num):
            if i % num == 0:
                switches[i] = 1 - switches[i]
    else:
        num = student[1]
        i = 0
        while num + i <= len(switches) and num - i >= 1:
            if switches[num + i] == switches[num - i]:
                switches[num + i], switches[num - i] = 1 - switches[num + i], 1 - switches[num - i]
                i += 1
            else:
                break

switches.pop(0)

for k in range(0, len(switches), 20):
    print(*switches[k:k+20])







