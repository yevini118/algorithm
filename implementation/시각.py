import datetime

n = int(input())

start = datetime.datetime(2022,1,1,0,0,0)
end = datetime.datetime(2022,1,1,n,59,59)
second = datetime.timedelta(seconds = 1)

count = 0
time = start
while(time <= end):
    if '3' in time.strftime('%H%M%S'):
        count += 1
    time += second

print(count)
