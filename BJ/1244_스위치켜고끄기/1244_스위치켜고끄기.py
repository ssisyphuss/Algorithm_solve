import sys


sys.stdin = open('input.txt')


N = int(input())
switches = [0] + list(map(int, input().split()))
stu_number = int(input())
stu_info = [list(map(int, input().split())) for _ in range(stu_number)]

def switch_boy(switches, num):
    for i in range(num, len(switches), num):
        if i % num == 0:
            switches[i] = 1 - switches[i]

    return switches

def switch_girl(switches, num):
    i = 0
    while num+i < len(switches) and num-i >= 1:
        if switches[num+i] == switches[num-i]:
            switches[num+i], switches[num-i]  = 1 - switches[num+i], 1 - switches[num-i]
            i += 1
        else:
            break

    return switches

for student in stu_info:
    if student[0] == 1:
        switches = switch_boy(switches, student[1])
    else:
        switches = switch_girl(switches, student[1])

switches.pop(0)

for k in range(0, len(switches), 20):
    print(*switches[k:k+20])







