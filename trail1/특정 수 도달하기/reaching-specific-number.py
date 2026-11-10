arr = list(map(int,input().split()))

sum = 0
cnt = 0
for i in range(len(arr)):
    if arr[i] >= 250:
        break
    else:
        sum += int(arr[i])
        cnt += 1
avg = sum / cnt
print(sum, f"{avg:.1f}")