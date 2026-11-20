N = int(input())

arr = [
    [0 for _ in range(N)]
    for _ in range(N)
]

Base_value = (N-1) % 2 
cnt = 1
for col in range(N-1,-1,-1):

    if (col %2) == Base_value:
        for i in range(N-1,-1,-1):
            arr[i][col] = cnt
            cnt += 1
    
    else:
        for i in range(N):
            arr[i][col] = cnt
            cnt +=1

for i in range(N):
    for j in range(N):
        print(arr[i][j], end=" ")
    print()

