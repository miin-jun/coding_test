N, M = map(int,input().split())

arr = [
    [0 for _ in range(N)]
    for _ in range(N)
]

for i in range(M):
    r,c = tuple(map(int,input().split()))
    arr[r-1][c-1] = (r) * (c)

for i in range(N):
    for j in range(N):
        print(arr[i][j], end =" ")
    print()