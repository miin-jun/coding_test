

N = int(input())

sum = 0
for i in range(N):
    num = int(input())
    sum += num

mean = round(sum / N, 1)
print(sum,mean )