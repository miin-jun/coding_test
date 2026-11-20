n, m = map(int, input().split())

# Please write your code here.
cnt = 1
col = 0

arr = [
    [0 for _ in range(m)]
    for _ in range(n)
]

for j in range(m):
    col = j
    if j == m-1:
        row_start = 0
        
        while row_start <n:
            col = j
            for i in range(row_start,n):
                row = i
                arr[row][col] = cnt
                col -= 1
                cnt += 1
                if col < 0:
                    break
            row_start += 1
            

    elif j < m-1:
        row = 0
        while col >=0 and row <n:
            arr[row][col] = cnt
            col -= 1
            row += 1
            cnt += 1
for i in range(n):
    for j in range(m):
        print(arr[i][j], end=" ")
    print()