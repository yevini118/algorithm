n = int(input())
part = list(map(int, input().split()))
m = int(input())
find = list(map(int, input().split()))

part.sort()

for f in find:
    start, end = 0, n-1
    
    while(True):

        if start > end:
            print("no", end=" ")
            break

        mid = (start + end) // 2

        if part[mid] == f:
            print("yes", end=" ")
            break
        elif part[mid] > f:
            end = mid - 1
        else:
            start = mid + 1

