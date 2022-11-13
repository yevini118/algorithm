def solution(n,m,k, data):

    data.sort()

    first = data[-1]
    second = data[-2]
    count = (m // (k+1)) * k + m % (k+1)

    num = 0
    num += first * count
    num += second * (m - count)

    return num

n, m, k = 5, 8, 3
data = [2, 4, 5, 4, 6]
print(solution(n,m,k,data))