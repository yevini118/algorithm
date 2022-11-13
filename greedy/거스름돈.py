def solution(n):

    change = [500,100,50,10]
    answer = 0

    for c in change:
        
        answer += (n//c) # 해당 화폐로 거슬러 줄 수 있는 동전의 개수
        n %= c

    return answer

n = 1260
print(solution(n))
