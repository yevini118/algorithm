def solution():

    answer = 0
    n, m = map(int, input().split())

    for i in range(n):
        
        line = list(map(int, input().split()))
        min_card = min(line)

        answer = max(min_card, answer)

    return answer

print(solution())
