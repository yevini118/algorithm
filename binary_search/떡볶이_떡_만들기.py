n, m = map(int, input().split())
ricecake = list(map(int, input().split()))


start, end = 0, max(ricecake)
while(start <= end):
    
    sum = 0
    mid = (start + end) //2

    for r in ricecake:
        if r > mid:
            sum += r - mid
    

    if sum < m:
        end = mid - 1
    else:
        answer = mid
        start = mid + 1

print(answer)
