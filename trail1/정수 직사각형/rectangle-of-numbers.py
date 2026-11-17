N, M = map(int,input().split())

i = 1
arr = [
    [0 for _ in range(M)]
    for _ in range(N)
]


k = 1
for i in range(N):
    for j in range(M):
        arr[i][j] = k
        k+=1

for i in range(N):
    for j in range(M):
        print(arr[i][j], end =" ")
    print()