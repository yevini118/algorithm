n = int(input())
scores = []
for i in range(n):
    name, score = input().split()
    scores.append([name, int(score)])

scores.sort(key = lambda x : x[1])

for i in range(n):
    print(scores[i][0], end=' ')