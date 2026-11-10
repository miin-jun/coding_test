arr = list(input().split())

a = []
for i in range(len(arr)):
    if i == 1 or i ==4 or i==7:
        a.append(arr[i])
print(*a)