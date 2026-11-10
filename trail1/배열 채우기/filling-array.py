arr =list(map(int,input().split()))

new_arr = []
for i in range(len(arr)):
    if arr[i] !=0:
        new_arr.append(arr[i])
    elif arr[i] == 0:
        break
print(*new_arr[i::-1])