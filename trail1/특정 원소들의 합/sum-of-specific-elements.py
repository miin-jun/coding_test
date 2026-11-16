
arr = [
    list(map(int,input().split()))
    for _ in range(4)
]

total = 0
for i in range(4):
    for j in range(i+1):
        total += arr[i][j]

print(total)



# 0,0
# 1,0 1,1
# 2,0 2,1 2,2
# 3,0 3,1 3,2 3,3