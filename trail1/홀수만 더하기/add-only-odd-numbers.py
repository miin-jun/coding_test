A = int(input())

sum = 0
for i in range(A):
    B = int(input())
    if B % 2 ==1 and B % 3 ==0:
        sum += B
print(sum)