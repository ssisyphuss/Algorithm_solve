import sys

sys.stdin = open("input.txt")

def bubble(iter):
    for i in range(len(iter)-1, 0, -1):
        for j in range(i):
            if iter[j] > iter[j+1]:
                iter[j], iter[j+1] = iter[j+1], iter[j]
    return iter

for _ in range(10):
    N = int(input())
    floor_list = list(map(int, input().split()))
    cnt = 0
    for idx in range(2, N-2):
        neighbor_floors = [floor_list[idx-2], floor_list[idx-1], floor_list[idx], floor_list[idx+1], floor_list[idx+2]]
        if floor_list[idx] == bubble(neighbor_floors)[-1]:
            cnt += bubble(neighbor_floors)[-1] - bubble(neighbor_floors)[-2]

    print(f'#{_+1} {cnt}')