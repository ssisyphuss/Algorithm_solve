def sandstorm(x, y, d):
    global di, dj, table

    if d == 0:
        sand = table[x][y-1]
        if sand == 0:
            return
        else:
            table[x-2][y-1] += int(sand * (0.02))
            table[x-1][y-2] += int(sand * (0.1))
            table[x-1][y-1] += int(sand * (0.07))
            table[x-1][y] += int(sand * (0.01))
            table[x][y-3] += int(sand * (0.05))
            table[x+1][y-2] += int(sand * (0.1))
            table[x+1][y-1] += int(sand * (0.07))
            table[x+1][y] += int(sand * (0.01))
            table[x+2][y-1] += int(sand * (0.02))
            sand_away = 2*(int(sand * (0.02))+int(sand * (0.1))+int(sand * (0.07))+int(sand * (0.01))) + int(sand * (0.05))
            table[x][y-2] += (sand - sand_away)
            table[x][y-1] = 0

    elif d == 1:
        sand = table[x+1][y]
        if sand == 0:
            return
        else:
            table[x+1][y-2] += int(sand * (0.02))
            table[x+2][y-1] += int(sand * (0.1))
            table[x+1][y-1] += int(sand * (0.07))
            table[x][y-1] += int(sand * (0.01))
            table[x+3][y] += int(sand * (0.05))
            table[x+2][y+1] += int(sand * (0.1))
            table[x+1][y+1] += int(sand * (0.07))
            table[x][y+1] += int(sand * (0.01))
            table[x+1][y+2] += int(sand * (0.02))
            sand_away = 2*(int(sand * (0.02))+int(sand * (0.1))+int(sand * (0.07))+int(sand * (0.01))) + int(sand * (0.05))
            table[x+2][y] += (sand - sand_away)
            table[x+1][y] = 0

    elif d == 2:
        sand = table[x][y + 1]
        if sand == 0:
            return
        else:
            table[x-2][y+1] += int(sand * (0.02))
            table[x-1][y+2] += int(sand * (0.1))
            table[x-1][y+1] += int(sand * (0.07))
            table[x-1][y] += int(sand * (0.01))
            table[x][y+3] += int(sand * (0.05))
            table[x+1][y+2] += int(sand * (0.1))
            table[x+1][y+1] += int(sand * (0.07))
            table[x+1][y] += int(sand * (0.01))
            table[x+2][y+1] += int(sand * (0.02))
            sand_away = 2*(int(sand * (0.02))+int(sand * (0.1))+int(sand * (0.07))+int(sand * (0.01))) + int(sand * (0.05))
            table[x][y+2] += (sand - sand_away)
            table[x][y+1] = 0

    else:
        sand = table[x-1][y]
        if sand == 0:
            return
        else:
            table[x-1][y-2] += int(sand * (0.02))
            table[x-2][y-1] += int(sand * (0.1))
            table[x-1][y-1] += int(sand * (0.07))
            table[x][y-1] += int(sand * (0.01))
            table[x-3][y] += int(sand * (0.05))
            table[x-2][y+1] += int(sand * (0.1))
            table[x-1][y+1] += int(sand * (0.07))
            table[x][y+1] += int(sand * (0.01))
            table[x-1][y+2] += int(sand * (0.02))
            sand_away = 2*(int(sand * (0.02))+int(sand * (0.1))+int(sand * (0.07))+int(sand * (0.01))) + int(sand * (0.05))
            table[x-2][y] += (sand - sand_away)
            table[x-1][y] = 0


di = [0, 1, 0, -1]
dj = [-1, 0, 1, 0]


N = int(input())
table = ([[0 for _ in range(N+6)] for _ in range(3)] +
        [[0, 0, 0] + list(map(int, input().split())) + [0, 0, 0] for _ in range(N)] +
        [[0 for _ in range(N+6)] for _ in range(3)])

i = (N//2) + 3
j = (N//2) + 3
k = 0
for m in range(1, N):
    for _ in range(2):
        for _ in range(m):
            sandstorm(i, j, k%4)
            i += di[k%4]
            j += dj[k%4]
        k += 1

for _ in range(N-1):
    sandstorm(i, j, k%4)
    i += di[k%4]
    j += dj[k%4]

answer = 0
for p in range(N+6):
    for q in range(N+6):
        if 0 <= p <= 2 or N+3 <= p <= N+5:
            answer += table[p][q]
        else:
            if 0 <= q <= 2 or N+3 <= q <= N+5:
                answer += table[p][q]


print(answer)






