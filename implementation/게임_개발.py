n, m = map(int, input().split())
a, b, d = map(int, input().split())

gmap = []
for i in range(n):
    gmap.append(list(map(int,input().split())))

left = [[-1,0], [0,-1], [1,0], [0,1]]
back = [[0,1], [-1,0], [0,-1], [1,0]]
gmap[a][b] = 1

turn = 0
count = 0
while(True):
    
    next_x = a + left[d][0]
    next_y = b + left[d][1]

    #왼쪽으로 방향 전환
    d -= 1
    if d == -1:
        d = 3
    
    #왼쪽 방향으로 이동 가능하면
    if gmap[next_y][next_x] == 0 and (next_x>=0 or next_x<m or next_y>=0 or next_y<n):
        turn = 0
        count += 1
        a, b = next_x, next_y
        gmap[next_x][next_y] = 1
    #왼쪽 방향으로 이동이 불가능하면
    else:
        turn += 1

    #네 방향 모두 이동이 불가능하면
    if turn == 4:
        next_x = a + back[d][0]
        next_y = b + back[d][1]

        if gmap[next_y][next_x] == 0 and (next_x>=0 or next_x<m or next_y>=0 or next_y<n):
            a, b = next_x, next_y
            turn = 0
        else:
            break
        

print(count)
    
    
    
    

    

