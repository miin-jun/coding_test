A = int(input())

sum =0
for i in range(1, A):
    if A %i==0:
        sum += i
if sum == A:
    print("P")
else:
    print("N")