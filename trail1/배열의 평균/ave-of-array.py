arr = [
    list(map(int,input().split()))
    for _ in range(2)
]

for i in range(len(arr)):
    print(round(sum(arr[i])/len(arr[0]),1), end=" ")

print()
for i in range(len(arr[0])):
    print(round(sum(arr[j][i] for j in range(len(arr))) / len(arr),1), end=" ")

print()
print(round(sum(sum(row) for row in arr)/ sum(map(len,arr)),1))
        