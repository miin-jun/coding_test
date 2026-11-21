N, M = map(int,input().split())

placed = [
    [0 for _ in range(N)]
    for _ in range(N)
]

for _ in range(M):
    r,c = tuple(map(int,input().split()))
    placed[r-1][c-1] = 1

for i in range(N):
    for j in range(N):
        print(placed[i][j], end=" ")
    print()
