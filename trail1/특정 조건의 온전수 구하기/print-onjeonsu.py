N = int(input())

num = []
for i in range(1,N+1):
    if i % 2 != 0 and i % 5 != 0:
        if not (i %3==0 and i % 9 !=0):
            num.append(i)
    else:
        continue
for i in range(len(num)):
    print(num[i], end=' ')

