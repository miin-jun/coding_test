arr = list(map(int,input().split()))


for i in range(len(arr)):
    if arr[i] == 999 or arr[i] == -999:
        break
print(max(arr[:i]), min(arr[:i]))