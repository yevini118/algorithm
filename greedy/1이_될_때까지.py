def solution():

    n, k = map(int, input().split())

    count = 1
    while(True):
        
        if (n <= k ** count):
            break

        count += 1

    answer = count + (n - k ** count)

    return answer

print(solution())