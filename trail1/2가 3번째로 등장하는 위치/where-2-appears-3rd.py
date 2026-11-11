N = int(input())
number = list(map(int,input().split()))

cnt = 0
for i in range(len(number)):
    if number[i] == 2:
        cnt += 1
        if cnt == 3:
            print(i+1)
            
