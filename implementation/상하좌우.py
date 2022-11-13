
n = int(input())
moves = input().split()

direction = {'L':[-1,0], 'R':[1,0], 'U':[0,-1], 'D':[0,1]}

now = [1,1]
for m in moves:
    next_x = now[0] + direction[m][0]
    next_y = now[1] + direction[m][1]

    if next_x < 1 or next_x > n or next_y < 1 or next_y > n:
        continue

    now = [next_x, next_y]

print(now[1], now[0])


