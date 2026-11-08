num = []

sum = 0
cnt = 0
for i in range(10):
    A = int(input())
    if A >=0 and A <=200:
        sum += A
        cnt += 1
mean = sum/cnt
print(sum, round(mean,1))

