start = input()

column = 'abcdefgh'
move = [[2,1],[1,2]]
direction = [[1,1],[-1,1],[1,-1],[-1,-1]]


count = 0
now = [ord(start[0])-96, int(start[1])]
for d in direction:
    for m in move:
        next_column = now[0] + m[0] * d[0]
        next_row = now[1] + m[1]*d[1]

        if next_column >= 1 and next_column <= 8 and next_row >= 1 and next_row <= 8:
            count += 1

print(count)
