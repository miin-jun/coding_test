A, B = map(int,input().split())

sum = 0
count = 0
for i in range(A,B+1):
    # if i % 5 == 0:
    #     sum += i
    #     count += 1
    # if i % 7 == 0:
    #     sum += i
    #     count += 1
    # if i % 5 ==0 and i & 7 ==0:
    #     sum = sum - i
    #     count -= 1
    if i % 5 ==0 or i % 7 ==0:
        sum += i
        count += 1
mean = (sum / count)
print(sum, round(mean,1))
    