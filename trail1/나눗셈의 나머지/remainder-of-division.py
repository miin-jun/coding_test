A, B = map(int,input().split())

arr = [0] * 10
while A > 1:
    remainder = A % B
    A = A//B
    arr[remainder] +=1

sum = 0
for i in arr:
    sum += i**2
print(sum)
